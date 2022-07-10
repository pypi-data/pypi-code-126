import gpuRIR
import numpy as np


class Room:
    """Room class stores the room parameters.

    Args:
        size: Room size with the shape of [3].
        abs_weights: Room absorption weights with the shape of [6].
        rt60: reverberation time (in seconds).
        sr: sampling rate, default is 16000 Hz.
    """

    def __init__(self, size: np.ndarray, abs_weights: np.ndarray, rt60, sr=16000):
        """Initialize the room parameters."""
        self.size = size
        self.rt60 = rt60
        self.sr = sr
        self.abs_weights = abs_weights
        self.att_ism = 15.0  # Attenuation when start using diffuse model [dB]
        self.att_max = 60.0  # Attenuation when start using max model [dB]

        if self.rt60 == 0:
            time_max = 0.1  # in second
            time_ism = 0.1
            num_images = [1, 1, 1]
        else:
            # Attenuation when start using the diffuse reverberation model [dB]
            time_ism = gpuRIR.att2t_SabineEstimator(self.att_ism, self.rt60)
            # Time to stop the simulation [s]
            time_max = gpuRIR.att2t_SabineEstimator(self.att_max, self.rt60)
            if self.rt60 < 0.15:
                time_max = time_ism
            num_images = gpuRIR.t2n(time_max, self.size)

        self.reflection_coeff = gpuRIR.beta_SabineEstimation(self.size, self.rt60, self.abs_weights)
        self.num_images = num_images
        self.time_ism = time_ism
        self.time_max = time_max


class RoomLoader:
    """Generate room class using the given room parameters."""

    def __init__(
        self,
        t60_range: tuple[float, float],
        size_range: tuple[float, float],
        abs_weights_range: tuple[list[float], list[float]],
        min_distance_from_wall_range: float,
    ):
        self.t60_range = t60_range

    def generate(self, num_spks) -> None:
        pass
