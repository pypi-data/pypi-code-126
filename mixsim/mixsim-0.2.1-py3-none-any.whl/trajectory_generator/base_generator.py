import numpy as np
from geomdl import BSpline, knotvector

from mixsim.trajectory_generator.region_2d import Region2D


class BaseGenerator:
    def __init__(self, region) -> None:
        super().__init__()
        self.region = Region2D(region[0], region[1])

    def generate(self):
        raise NotImplementedError

    @staticmethod
    def distance2duration(distance, moving_speed):
        """Convert a distance to the fpath based on a giving moving speed.

        Args:
            distance: the unit is meter
            moving_speed: the unit is meter per second

        Returns:
            The fpath for a given distance. The unit is second.
        """
        return distance / moving_speed

    @staticmethod
    def euclidean_distance(x, y):
        return np.sqrt(np.sum(np.power(x - y, 2)))


class BaseDynamicGenerator(BaseGenerator):
    def __init__(self, region) -> None:
        super().__init__(region)

    @staticmethod
    def reverse_trajectory(trajectory):
        return trajectory[::-1]

    def generate(self):
        raise NotImplementedError

    @staticmethod
    def get_curved_trajectory(
        start: np.ndarray,
        control_points: np.ndarray,
        end: np.ndarray,
        num_trajectory_points,
    ):
        start = start.tolist()
        end = end.tolist()
        control_points = control_points.tolist()

        crv = BSpline.Curve()
        crv.degree = 2
        crv.ctrlpts = [start, *control_points, end]
        crv.knotvector = knotvector.generate(crv.degree, crv.ctrlpts_size)
        # geomdl not depends on numpy. you should provide python int
        crv.sample_size = int(num_trajectory_points)
        trajectory = np.array(crv.evalpts)  # [L, 2]

        return trajectory

    @staticmethod
    def sort_control_points_along_axis(control_points):
        control_points = np.array(control_points)

        # sort along x coordinate
        return control_points[control_points[:, 0].argsort()]
