from SpatialCluster.utils.data_structures  import IncrementalCOOMatrix
from SpatialCluster.utils.data_format import position_data_format
from scipy import spatial
import numpy as np

def adjacencyMatrix(features_position, r = 300, k = 5, min_k = 2, criteria = "k", leafsize = 10):
    meter_to_degree_equivalence = 9.090909091e-6
    r = r*meter_to_degree_equivalence # Se transforma de metros a grados
    features_position = position_data_format(features_position)
    points = list(zip(features_position.lon, features_position.lat))

    # --------------------------------------------------------------------------
    len_points = len(points)
    shape = (len_points, len_points)
    mat = IncrementalCOOMatrix(shape, np.int64)

    tree = spatial.KDTree(data = points, leafsize = leafsize)
    if(criteria == "k"):
        k_neighbours = tree.query(points, k = k)[1] # k vecinos
        for i, neighbourhood in enumerate(k_neighbours):
            for neighbour in neighbourhood:
                mat.append(i, neighbour, 1)
    elif(criteria == "r"):
        nearest_neighbours = tree.query_ball_tree(tree, r) # vecinos dentro de radio r
        for i, neighbourhood in enumerate(nearest_neighbours):
            for neighbour in neighbourhood:
                mat.append(i, neighbour, 1)
    elif(criteria == "rk"):
        nearest_neighbours = tree.query_ball_tree(tree, r) # vecinos dentro de radio r
        k_neighbours = tree.query(points, k = k)[1] # k vecinos
        for i, neighbourhood in enumerate(nearest_neighbours):
            if len(neighbourhood) < min_k: # si la cantidad de vecinos dentro del radio es menor que min_k
                neighbourhood = k_neighbours[i] # se usan los k vecinos
            for neighbour in neighbourhood:
                mat.append(i, neighbour, 1)
    else:
        raise ValueError("Valor inválido para el parámetro 'criteria' ('r', 'k', 'rk')")

    A = mat.tocoo() # adjacency matrix
    A = A.tocsr()

    return A
