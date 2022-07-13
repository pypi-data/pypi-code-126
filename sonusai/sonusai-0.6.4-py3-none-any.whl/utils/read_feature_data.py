import h5py
import numpy as np

from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.mixdb import mixdb_from_str


def read_feature_data(filename: str) -> (MixtureDatabase, np.ndarray, np.ndarray, np.ndarray):
    """Read mixdb, feature, truth_f, and segsnr data from given HDF5 file and return them as a tuple."""
    with h5py.File(name=filename, mode='r') as f:
        return (mixdb_from_str(f.attrs['mixdb']),
                np.array(f['feature']),
                np.array(f['truth_f']),
                np.array(f['segsnr']))
