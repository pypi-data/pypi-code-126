import numpy as np

from mixsim.trajectory_generator.base_generator import BaseDynamicGenerator


class CurveGenerator(BaseDynamicGenerator):
    def __init__(
        self,
        region: list[list[float]],
        moving_speed: float,
        rir_interval: float,
        num_trajectory_points: int,
        speaker_height: float,
        random_reverse: bool = True,
    ) -> None:
        super().__init__(region)
        self.moving_speed = moving_speed
        self.rir_interval = rir_interval
        self.random_reverse = random_reverse
        self.speaker_height = speaker_height
        self.num_trajectory_points = num_trajectory_points

    def generate(self):
        if np.random.random(1) > 0.5:
            # random x-axis
            start = np.array([self.region.get_random_point()[0], self.region.bottom_left_corner[1]])
            end = np.array([self.region.get_random_point()[0], self.region.top_left_corner[1]])
        else:
            # random y-axis
            start = np.array([self.region.bottom_left_corner[0], self.region.get_random_point()[1]])
            end = np.array([self.region.bottom_right_corner[0], self.region.get_random_point()[1]])

        feasible_duration = self.distance2duration(self.euclidean_distance(start, end), self.moving_speed)
        feasible_num_trajectory_points = np.ceil(feasible_duration / self.rir_interval).astype(int)
        feasible_trajectory = np.linspace(start, end, num=feasible_num_trajectory_points)

        if self.num_trajectory_points > feasible_num_trajectory_points:
            pad_width = (
                int(self.num_trajectory_points // feasible_num_trajectory_points) * feasible_num_trajectory_points
            )
            padded_trajectory = np.pad(feasible_trajectory, ((0, pad_width), (0, 0)), mode="reflect")
            start_idx = np.random.randint(0, len(padded_trajectory) - self.num_trajectory_points + 1)
            trajectory = padded_trajectory[start_idx : start_idx + self.num_trajectory_points]
        else:
            start_idx = np.random.randint(0, len(feasible_trajectory) - self.num_trajectory_points + 1)
            trajectory = feasible_trajectory[start_idx : start_idx + self.num_trajectory_points]

        if self.random_reverse and (np.random.random(1) > 0.5):
            trajectory = self.reverse_trajectory(trajectory)

        # [num_trajectory_points, 3] has a fixed z-axis
        trajectory = np.concatenate(
            (
                trajectory,
                np.repeat(self.speaker_height, self.num_trajectory_points)[:, None],
            ),
            axis=-1,
        )

        return trajectory
