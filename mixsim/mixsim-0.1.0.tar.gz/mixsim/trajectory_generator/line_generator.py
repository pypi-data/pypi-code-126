import numpy as np

from mixsim.trajectory_generator.base_generator import BaseDynamicGenerator


class LineGenerator(BaseDynamicGenerator):
    def __init__(
        self,
        region: list[list[float]],
        moving_speed: float,
        rir_interval: float,
        num_trajectory_points: int,
        speaker_height: float,
        num_control_points: int,
        random_reverse: bool = True,
    ) -> None:
        super().__init__(region)
        self.moving_speed = moving_speed
        self.rir_interval = rir_interval
        self.random_reverse = random_reverse
        self.speaker_height = speaker_height
        self.num_trajectory_points = num_trajectory_points
        self.num_control_points = num_control_points

    def generate(self):
        control_points = []
        control_coords = self.region.get_control_coords(self.num_control_points)
        if np.random.random(1) > 0.5:
            # random x axis
            start = np.array([self.region.get_random_point()[0], self.region.bottom_left_corner[1]])
            end = np.array([self.region.get_random_point()[0], self.region.top_left_corner[1]])
            # random x and controlled y
            for i in range(self.num_control_points):
                control_points.append(np.array([self.region.get_random_point()[0], control_coords[i][1]]))
        else:
            # random y axis
            start = np.array([self.region.bottom_left_corner[0], self.region.get_random_point()[1]])
            end = np.array([self.region.bottom_right_corner[0], self.region.get_random_point()[1]])
            # controlled x and random y
            for i in range(self.num_control_points):
                control_points.append(np.array([control_coords[i][0], self.region.get_random_point()[1]]))

        control_points = np.array(control_points)

        feasible_duration = self.distance2duration(self.euclidean_distance(start, end), self.moving_speed)
        feasible_num_trajectory_points = np.ceil(feasible_duration / self.rir_interval).astype(int)

        feasible_trajectory = self.get_curved_trajectory(start, control_points, end, feasible_num_trajectory_points)

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
            trajectory = trajectory[::-1]

        return (
            trajectory,
            feasible_trajectory,
            {"start": start, "end": end, "control_points": control_points},
        )
