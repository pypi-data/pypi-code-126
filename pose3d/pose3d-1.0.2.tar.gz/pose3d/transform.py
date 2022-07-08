import numpy as np
from scipy.spatial.transform import Rotation

from .pose import Pose


class Transform:
    def __init__(self, name: str, orig: str = None, dest: str = None) -> None:
        # Set strings
        self.name = name

        if orig is None and dest is None:
            self.orig = 'origin'
            self.dest = 'destination'
        else:
            self.orig = orig
            self.dest = dest

        # Init translation and orientation
        self.translation = np.zeros(3)
        self.orientation = Rotation.identity()

    def print(self):
        print(f"Transformation: {self.name.title()}")
        print(f"Translation: {self.translation} [m]")
        print(f"Orientation: {self.orientation.as_euler('xyz', degrees=True)} [deg]\n")

    def inv(self):
        inv_transform = Transform(name=f"{self.name} (Inverse)")
        inv_transform.orientation = self.orientation.inv()
        inv_transform.translation = -inv_transform.orientation.apply(self.translation)

        return inv_transform

    def apply(self, input):
        
        # If input is pose
        if type(input) is Pose:
            input.rotation.from_matrix(np.matmul(self.orientation.as_matrix(), input.rotation.as_matrix()))
            input.position += self.translation

        # If input is 3D vector
        elif type(input) is np.ndarray and np.size(input) == 3:
            input = self.orientation.apply(input) + self.translation

        return input

    def matrix(self, homogeneous: bool = True):

        matrix = np.eye(4)
        
        if self.orig != self.dest:
            matrix[:3, :3] = self.orientation.as_matrix()
            matrix[:3, 3] = self.translation

        if not homogeneous:
            return matrix[:3, :]
        
        return matrix

    def random(self):
        self.translation = np.random.rand(3)
        self.orientation = Rotation.random()
