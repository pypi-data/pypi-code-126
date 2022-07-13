from collections import namedtuple

import numpy as np

EPS = np.finfo(np.float32).eps
MAX_INT16 = np.iinfo(np.int16).max

PI = np.pi
SOUND_SPEED = 343  # m/s

ArraySetup = namedtuple("ArraySetup", "arrayType, orV, mic_pos, mic_orV, mic_pattern")

supported_array_setups = {
    "dicit": ArraySetup(
        arrayType="planar",
        orV=np.array([0.0, 1.0, 0.0]),
        mic_pos=np.array(
            (
                (0.96, 0.00, 0.00),
                (0.64, 0.00, 0.00),
                (0.32, 0.00, 0.00),
                (0.16, 0.00, 0.00),
                (0.08, 0.00, 0.00),
                (0.04, 0.00, 0.00),
                (0.00, 0.00, 0.00),
                (0.96, 0.00, 0.32),
                (-0.04, 0.00, 0.00),
                (-0.08, 0.00, 0.00),
                (-0.16, 0.00, 0.00),
                (-0.32, 0.00, 0.00),
                (-0.64, 0.00, 0.00),
                (-0.96, 0.00, 0.00),
                (-0.96, 0.00, 0.32),
            )
        ),
        mic_orV=np.tile(np.array([[0.0, 1.0, 0.0]]), (15, 1)),
        mic_pattern="omni",
    )
}
