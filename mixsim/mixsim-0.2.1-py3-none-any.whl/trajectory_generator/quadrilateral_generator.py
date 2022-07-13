import numpy as np

from mixsim.trajectory_generator.base_generator import BaseDynamicGenerator
from mixsim.trajectory_generator.region_2d import Region2D


class QuadrilateralGenerator(BaseDynamicGenerator):
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
        """
        Notes:
            Top Left            Top Right
                +------+-----+------+
                |  1-1 | 1-2 | 1-3  |
                +------+-----+------+
                |  2-1 | 2-2 | 2-3  | (Depth)
                +------+-----+------+
                |  3-1 | 3-2 | 3-3  |
                +------+-----+------+
            bottom left       Bottom Right
                      (Width)
        """
        # Example:
        # Region((0.5, 0.5), (6.5, 8.5))
        # width: 6, depth: 8
        # width_interval: [0.5, 2.5, 4.5, 6.5], depth_interval: [0.5, 3.2, 5.8, 8.5]
        width_interval = np.linspace(self.region.bottom_left_corner[0], self.region.bottom_right_corner[0], 4)
        depth_interval = np.linspace(self.region.bottom_left_corner[1], self.region.top_left_corner[1], 4)

        region_11 = Region2D(
            (width_interval[0], depth_interval[-2]),
            (width_interval[1], depth_interval[-1]),
        )
        # region_12 = Region2D((width_interval[1], depth_interval[-2]), (width_interval[2], depth_interval[-1]))
        region_13 = Region2D(
            (width_interval[2], depth_interval[-2]),
            (width_interval[3], depth_interval[-1]),
        )

        # region_21 = Region2D((width_interval[0], depth_interval[-3]), (width_interval[1], depth_interval[-2]))
        # region_22 = Region2D((width_interval[1], depth_interval[-3]), (width_interval[2], depth_interval[-2]))
        # region_23 = Region2D((width_interval[2], depth_interval[-3]), (width_interval[3], depth_interval[-2]))

        region_31 = Region2D(
            (width_interval[0], depth_interval[-4]),
            (width_interval[1], depth_interval[-3]),
        )
        # region_32 = Region2D((width_interval[1], depth_interval[-4]), (width_interval[2], depth_interval[-3]))
        region_33 = Region2D(
            (width_interval[2], depth_interval[-4]),
            (width_interval[3], depth_interval[-3]),
        )

        random_point_11 = region_11.get_random_point()
        random_point_13 = region_13.get_random_point()
        random_point_33 = region_33.get_random_point()
        random_point_31 = region_31.get_random_point()

        feasible_duration_11_13 = self.distance2duration(
            self.euclidean_distance(random_point_11, random_point_13), self.moving_speed
        )
        feasible_duration_13_33 = self.distance2duration(
            self.euclidean_distance(random_point_13, random_point_33), self.moving_speed
        )
        feasible_duration_33_31 = self.distance2duration(
            self.euclidean_distance(random_point_33, random_point_31), self.moving_speed
        )
        feasible_duration_31_11 = self.distance2duration(
            self.euclidean_distance(random_point_31, random_point_11), self.moving_speed
        )

        feasible_num_trajectory_points_11_13 = np.ceil(feasible_duration_11_13 / self.rir_interval).astype(int)
        feasible_num_trajectory_points_13_33 = np.ceil(feasible_duration_13_33 / self.rir_interval).astype(int)
        feasible_num_trajectory_points_33_31 = np.ceil(feasible_duration_33_31 / self.rir_interval).astype(int)
        feasible_num_trajectory_points_31_11 = np.ceil(feasible_duration_31_11 / self.rir_interval).astype(int)

        feasible_trajectory_11_13 = np.linspace(
            random_point_11, random_point_13, num=feasible_num_trajectory_points_11_13
        )
        feasible_trajectory_13_33 = np.linspace(
            random_point_13, random_point_33, num=feasible_num_trajectory_points_13_33
        )
        feasible_trajectory_33_31 = np.linspace(
            random_point_33, random_point_31, num=feasible_num_trajectory_points_33_31
        )
        feasible_trajectory_31_11 = np.linspace(
            random_point_31, random_point_11, num=feasible_num_trajectory_points_31_11
        )

        feasible_trajectory_list = [
            feasible_trajectory_11_13,
            feasible_trajectory_13_33,
            feasible_trajectory_33_31,
            feasible_trajectory_31_11,
        ]
        feasible_trajectory = np.concatenate(feasible_trajectory_list)

        random_edge_idx = np.random.randint(0, 4)  # randomly select an edge
        edge_start_idx = np.sum([len(traj) for traj in feasible_trajectory_list[:random_edge_idx]])
        edge_end_idx = edge_start_idx + len(feasible_trajectory_list[random_edge_idx])

        random_trajectory_start = (
            np.max(
                [
                    len(feasible_trajectory_list[random_edge_idx]) - self.num_trajectory_points,
                    0,
                ]
            )
            + edge_start_idx
        )
        start_idx = np.random.randint(
            random_trajectory_start, edge_end_idx
        )  # Notice: no "end +1", throughout the ending point
        end_idx = start_idx + self.num_trajectory_points

        if end_idx > (len(feasible_trajectory) - start_idx):  # clean length is too long
            pad_width = int(self.num_trajectory_points // len(feasible_trajectory) + 1) * len(feasible_trajectory)
            padded_feasible_trajectory = np.pad(feasible_trajectory, np.array((0, pad_width), (0, 0)), mode="wrap")
            trajectory = padded_feasible_trajectory[start_idx:end_idx]
        else:
            trajectory = feasible_trajectory[start_idx:end_idx]

        if self.random_reverse and (np.random.random(1) > 0.5):
            trajectory = trajectory[::-1]

        return trajectory, feasible_trajectory, {}
