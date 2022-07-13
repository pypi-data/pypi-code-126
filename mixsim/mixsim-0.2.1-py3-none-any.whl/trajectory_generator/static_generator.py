import numpy as np

from mixsim.trajectory_generator.base_generator import BaseGenerator


class StaticGenerator(BaseGenerator):
    def __init__(
        self,
        region,
        speaker_height,
    ) -> None:
        super().__init__(region)
        self.region = region
        self.speaker_height = speaker_height

    def generate(self):
        static_position = self.region.get_random_point()  # [x, y]
        trajectory_point = np.concatenate((static_position, self.speaker_height))  # [x, y, z]
        return trajectory_point
