import joblib
import numpy as np
import pandas as pd
from tsfresh.feature_extraction import extract_features

from . import PACKAGEDIR

MODEL_PATH = PACKAGEDIR / "data" / "model.dat"
RFC_MODEL = joblib.load(MODEL_PATH)

CANDIDATES_COLUMNS = [
    "i_start",
    "i_peak",
    "i_stop",
    "t_start",
    "t_peak",
    "t_stop",
    "sso",
    "flare_prob",
    "amp",
    "duration",
    "ed",
]

FC_PARAMETERS = {
    "abs_energy": None,
    "first_location_of_maximum": None,
    "index_mass_quantile": [{"q": 0.3}, {"q": 0.5}, {"q": 0.7}],
    "length": None,
    "maximum": None,
    "mean": None,
    "mean_abs_change": None,
    "median": None,
    "root_mean_square": None,
    "kurtosis": None,
    "skewness": None,
    "variance": None,
    "variation_coefficient": None,
}


def get_flare_probability(time, flux):
    time *= 1440
    data = pd.DataFrame({"time": time - time.min(), "flux": flux})
    data_id = np.ones(len(data), dtype=int)
    data.insert(0, "id", data_id)
    feature = extract_features(
        data,
        column_id="id",
        column_sort="time",
        default_fc_parameters=FC_PARAMETERS,
        disable_progressbar=True,
        n_jobs=0,
    )

    return RFC_MODEL.predict_proba(feature)[0][0]


def extend(flux, i_start, i_stop, n_sigma=1):
    n_left, n_right = 1, 2

    # left
    try:
        while (flux[i_start - n_left : i_start] > n_sigma).any() and flux[i_start - n_left] > -5:
            i_start -= 1
    except IndexError:
        pass

    i_start_ext = max(0, i_start - 1)
    if np.isnan(flux[i_start_ext]):
        i_start_ext += 1

    # right
    try:
        while (flux[i_stop + 1 : i_stop + 1 + n_right] > n_sigma).any() and flux[i_stop + n_right] > -5:
            i_stop += 1
    except IndexError:
        pass

    i_stop_ext = min(flux.size - 1, i_stop + 1)
    if np.isnan(flux[i_stop_ext]):
        i_start_ext -= 1

    return i_start_ext, i_stop_ext


def find_consecutive(indexes, n_consecutive, gap=1, data=None):
    if data is None:
        grouped_data = np.split(indexes, np.nonzero(np.diff(indexes) > gap)[0] + 1)
    else:
        grouped_data = np.split(indexes, np.nonzero(np.diff(data[indexes]) > gap)[0] + 1)

    grouped_consecutive_data = [x for x in grouped_data if x.size >= n_consecutive]

    if len(grouped_consecutive_data):
        i_start_array = np.array([x[0] for x in grouped_consecutive_data], dtype=int)
        i_stop_array = np.array([x[-1] for x in grouped_consecutive_data], dtype=int)
        return i_start_array, i_stop_array
    else:
        return None, None


def fill_gaps(time, flux, cadenceno):
    """Fill gaps in the data by interpolation."""

    newdata = {}

    dt = time - np.median(np.diff(time)) * cadenceno
    ncad = np.arange(cadenceno[0], cadenceno[-1] + 1, 1)
    in_original = np.in1d(ncad, cadenceno)
    ncad = ncad[~in_original]
    ndt = np.interp(ncad, cadenceno, dt)

    ncad = np.append(ncad, cadenceno)
    ndt = np.append(ndt, dt)
    ncad, ndt = ncad[np.argsort(ncad)], ndt[np.argsort(ncad)]
    ntime = ndt + np.median(np.diff(time)) * ncad
    newdata["cadenceno"] = ncad

    nflux = np.zeros(len(ntime))
    nflux[in_original] = flux
    nflux[~in_original] = np.interp(ntime[~in_original], time, flux)

    return ntime, nflux
