import numpy as np


class Region2D:
    def __init__(self, bottom_left_coord, top_right_coord):
        """
        Construct a region using given parameters, i.e., bottom_left_coord and top_right_coord

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

        Args:
            bottom_left_coord: array_like (x, y)
            top_right_coord: array_like, (x, y)
        """
        super(Region2D, self).__init__()
        # Infer all coordinates using bottom_left_coord and top_right_coord
        self.bottom_left_corner = np.array([bottom_left_coord[0], bottom_left_coord[1]])
        self.bottom_right_corner = np.array([top_right_coord[0], bottom_left_coord[1]])
        self.top_right_corner = np.array([top_right_coord[0], top_right_coord[1]])
        self.top_left_corner = np.array([bottom_left_coord[0], self.top_right_corner[1]])

        # Width and depth in civil engineering
        # (开间)    (进深)
        self.width = self.bottom_right_corner[0] - self.bottom_left_corner[0]
        self.depth = self.top_left_corner[1] - self.bottom_left_corner[1]

    def get_random_point(self):
        """Get the coordinate of a given point within the region."""
        x = np.random.uniform(self.bottom_left_corner[0], self.bottom_right_corner[0])
        y = np.random.uniform(self.bottom_left_corner[1], self.top_left_corner[1])
        return np.array([x, y])

    def get_center_point(self):
        x = np.mean([self.bottom_left_corner[0], self.bottom_right_corner[0]])
        y = np.mean([self.bottom_left_corner[1], self.top_left_corner[1]])
        return np.array([x, y])

    def get_control_coords(self, num_control_points):
        """Separate all axes equally using a given num_control_points

        Examples
            return: np.array([
                [2, 4],
                [3, 5],
                x, y
            ])
        """
        x = np.linspace(
            self.bottom_left_corner[0],
            self.bottom_right_corner[0],
            num=num_control_points + 2,
        )[1:-1]
        y = np.linspace(
            self.bottom_left_corner[0],
            self.top_left_corner[1],
            num=num_control_points + 2,
        )[1:-1]
        return np.array([x, y]).transpose()  # [num_control_points, 2]

    def __repr__(self):
        return f"width: {self.width:.1f}, depth: {self.depth:.1f}"
