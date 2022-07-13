import numpy as np
import pkg_resources

DATA_PATH = pkg_resources.resource_filename('ocr_weighted_levenshtein', 'data/')

def get_distances_params():
    return {
        "substitute_costs": np.load(DATA_PATH + "/subs.npy"), 
        "insert_costs": np.load(DATA_PATH + "/insert.npy"),
        "delete_costs": np.load(DATA_PATH + "/delete.npy")
    }
        