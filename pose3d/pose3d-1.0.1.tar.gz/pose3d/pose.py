import numpy as np
from scipy.spatial.transform import Rotation

class Pose:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rotation = Rotation.identity()
        self.position = np.array([0.0, 0.0, 0.0])

    def print(self):
        print(f"Pose: {self.name.title()}")
        print(f"Position: {self.position} [m]")
        print(f"Rotation: {self.rotation.as_euler('xyz', degrees=True)} [deg]\n")

    def random(self):
        self.rotation = Rotation.random()
        self.position = np.random.rand(3)
