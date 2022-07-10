import itertools

import numpy as np
import pyroomacoustics as pra
from joblib import Parallel, delayed
from numpy import ndarray

from mixsim.rir_simulator.base_rir_simulator import BaseRIRSimulator


class PyroomacousticsRIRSimulator(BaseRIRSimulator):
    def __init__(
        self,
        t60: float,
        room_size: list,
        num_mics: int,
        reflection_coeff: list[float],
        mic_position: list[float],
        trajectory_points: ndarray,
        sr: int = 16000,
    ) -> None:
        self.t60 = t60
        self.room_size = room_size
        self.num_mics = num_mics
        self.reflection_coeff = reflection_coeff
        self.mic_position = mic_position
        self.trajectory_points = trajectory_points
        self.sr = sr

    def _simulate_rirs_gpuRIR(self):
        e_absorption, max_order = pra.inverse_sabine(self.t60, self.room_size)
        n_jobs = 40  # Extract it to __init__ later

        def sub_simulator(source_position):
            room = pra.ShoeBox(
                self.room_size,
                fs=self.sr,
                materials=pra.Material(e_absorption),
                max_order=max_order,
            )
            room.add_microphone_array(np.transpose(self.mic_position))  # [3, 15]
            room.add_source(source_position, signal=None)
            room.compute_rir()
            rir = np.array(
                list(itertools.zip_longest(*[room.rir[m][0] for m in range(len(room.rir))], fillvalue=0))  # type: ignore
            ).T
            return rir  # [num_mics, rir_len]

        # Run simulator in parallel
        rir_list = Parallel(n_jobs=n_jobs)(delayed(sub_simulator)(i) for i in self.trajectory_points)

        # Different RIR channels have different lengths.
        max_len = np.max([len(rir[0]) for rir in rir_list])
        rirs = np.array(
            [
                np.pad(
                    rir,
                    np.array((0, 0), (0, max_len - len(rir[0]))),
                    "constant",
                    constant_values=0,
                )
                for rir in rir_list
            ],
            dtype=np.float32,
        )
        return rirs
