import numpy as np
from .rotation2d import Rotation2D

class Pose2D:
    def __init__(self, name) -> None:
        self.name = name
        self.rotation = Rotation2D()
        self.position = np.array([0.0, 0.0])

    def print(self):
        print(f"Pose2D: {self.name.title()}")
        print(f"Position: {self.position} [m]")
        print(f"Rotation: {self.rotation.as_euler(degrees=True)} [deg]\n")

    def random(self):
        self.rotation = Rotation2D.random()
        self.position = np.random.rand(2)
