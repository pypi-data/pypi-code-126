from sys import path
from os.path import dirname, join, abspath
path.insert(0, abspath(join(dirname(__file__), '..')))

from pose3d.transform_set import TransformSet

def main():
    transforms = TransformSet(cfg_file="demo/frames.toml")

if __name__ == "__main__":
    main()