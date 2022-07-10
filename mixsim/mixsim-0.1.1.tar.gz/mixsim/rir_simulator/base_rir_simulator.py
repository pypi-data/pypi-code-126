import gpuRIR
import numpy as np

from mixsim.rir_simulator.source import Microphone, Source


class BaseRIRSimulator:
    """Generate RIRs using the given parameters."""

    @staticmethod
    def _simulate_rirs_gpuRIR(traj_points: np.ndarray, room: Room, microphone: Microphone) -> np.ndarray:
        """Simulate RIRs using gpuRIR.

        Args:
            traj_points: 2-D numpy array of trajectory points with the shape of [num_points, 3 or 2]
            room: Room class stores the room parameters.
            microphone: microphone class stores the microphone parameters.

        Returns:
            A 2-D numpy array of RIRs with the shape of [num_points, num_samples].

        Note:
            ``traj_points`` can be a static position, a trajectory, or a combination of different trajectories.
            If you use a combination of trajectories, the output RIRs will be combined. You must separate them.
        """
        num_traj = traj_points.shape[0]
        num_gpu_calls = min(
            int(np.ceil(room.sample_rate * room.time_max * microphone.num_mics * num_traj * np.prod(room.num_images) / 1e9)),
            num_traj,
        )

        traj_point_batch = np.ceil(num_traj / num_gpu_calls * np.arange(0, num_gpu_calls + 1)).astype(int)

        rir_list = []
        for call_index in range(num_gpu_calls):
            rir_list.append(
                # [num_source or num_source_traj, num_mics, time_max]
                gpuRIR.simulateRIR(
                    room_sz=room.size,
                    beta=room.reflection_coeff,
                    pos_src=traj_points[traj_point_batch[call_index] : traj_point_batch[call_index + 1], :],
                    pos_rcv=microphone.position,
                    nb_img=room.num_images,
                    Tmax=room.time_max,
                    fs=room.sample_rate,
                    Tdiff=room.time_max,
                    mic_pattern="omni",
                )
            )
        rirs = np.concatenate(rir_list, axis=0)  # [num_trajectory_points, num_mics, time_diffuse]

        return rirs

    def simulate_rirs(
        self,
        room: Room,
        microphone: Microphone,
        sources: list[Source],
    ):
        """Simulate RIRs using the given parameters of room and microphone.

        Args:
            room: room class stores the room parameters.
            microphone: microphone class stores the microphone parameters.
            sources: list of source objects.

        Returns:
            Null

        Note:
            The generated rir and filtered audio will be stored in the source objects separately.
        """
        # For faster simulation, we combine multiple trajectories.
        merged_traj_points = []
        for source in sources:
            assert source.traj is not None
            merged_traj_points.append(source.traj)
        merged_traj_points = np.concatenate(merged_traj_points, axis=0)

        # Simulate RIRs
        rirs = self._simulate_rirs_gpuRIR(merged_traj_points, room, microphone)

        # Separate RIRs into different sources and store them in the sources.
        for source in sources:
            assert source.traj is not None
            rir = rirs[: len(source.traj), ...]
            source.add_rvb(rir)
