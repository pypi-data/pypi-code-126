import numpy as np

import logging

import westpa.core.binning
from rich.logging import RichHandler

import msm_we.msm_we

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(RichHandler())
log.propagate = False


def solve_discrepancy(tmatrix, pi, B):
    """
    Given a transition matrix, solves for the discrepancy function.

    The Poisson equation for the discrepancy function is
    .. math::
        (I - K)h = 1_B - \pi(B), \:\: h \cdot \pi = 0

    however, since :math:`I-K` is singular, we instead solve
    .. math::
        (I - K + \pi \pi^T / || \pi ||^2_2)h = 1_B - \pi(B), \:\: h \cdot \pi = 0
    where :math:`h` is a volumn vector, `1_B` is an indicator function which is 1 in B and 0 everywhere
    else, :math:`\pi` is the steady-state solution of :math:`K`, and `\pi(B)` is a column vector with
    the steady-state value of :math:`\pi(B)` in every element.

    Parameters
    ----------
    tmatrix, 2D array-like: Transition matrix
    pi, array-like: Steady-state distribution for the input transition matrix
    B, array-like: Indices of target states B

    Returns
    --------
    (discrepancy, variance)
    """

    log.info("Computing pi matrix")
    norm = np.dot(pi, pi.T)
    pi_matrix = pi @ pi.T / norm

    b_indicator = np.zeros_like(pi)
    b_indicator[B] = 1.0

    pi_b = np.ones_like(pi)
    pi_b[:] = sum(pi[B])

    discrepancy = np.linalg.solve(np.identity(tmatrix.shape[0]) - tmatrix + pi_matrix,
                                  b_indicator - pi_b)

    variance = np.sqrt(
        np.dot(tmatrix, discrepancy**2) -
        np.dot(tmatrix, discrepancy)**2
    )

    return discrepancy, variance


def get_mfpt_bins(variance, steady_state, n_bins):
    """
    Implements the MFPT-binning strategy described in [1], where bins are groups of microstates that are uniformly
    spaced in the integral of pi * v

    Parameters
    ----------
    variance, array-like: Variance function
    steady_state, array-like: Steady-state distribution
    n_bins int: Number of macrobins

    Returns
    -------

    References
    ----------
    [1] Aristoff, D., Copperman, J., Simpson, G., Webber, R. J. & Zuckerman, D. M.
    Weighted ensemble: Recent mathematical developments. Arxiv (2022).

    """

    pi_v = steady_state * variance

    spacing = sum(pi_v) / n_bins

    bin_states = {}
    for i in range(n_bins):
        lower, upper = spacing * i, spacing * i+1

        states_in_bin = np.argwhere(
            (lower < np.cumsum(pi_v)) &
            (np.cumsum(pi_v) <= upper)
        )

        bin_states[i] = states_in_bin

    return bin_states


# class MinimalModel:
#     """
#     Serializable model containing necessary data for stratified clustering
#     """
#
#     n_clusters = None
#
#     # For is_WE_target/basis functions
#     pcoord_ndim = None
#     target_pcoord_bounds = None
#     basis_pcoord_bounds = None
#
#     # These require self.target_pcoord_bounds and self.basis_pcoord_bounds to be set
#     is_WE_target = msm_we.msm_we.modelWE.is_WE_target
#     is_WE_basis = msm_we.msm_we.modelWE.is_WE_basis
#
#     # List of the pcoords for the data being clustered
#     pcoord1List = None


class OptimizedBinMapper(westpa.core.binning.FuncBinMapper):

    def __init__(self,
                 nbins: int,
                 n_original_pcoord_dims: int,
                 cluster_centers,
                 previous_binmapper,
                 microstate_mapper: dict
                 ):
        """
        Creates an OptimizedBinMapper, suitable for use with the optimization workflow

        Parameters
        ----------
        nbins, int: Number of WE bins
        n_original_pcoord_dims, int: Number of dimensions in the original user-supplied progress coordinate
        cluster_centers, array-like: Array of microstate cluster centers
        microstate_mapper, dict: Mapping of microstates to WE bins

        TODO
        ----
        - Should we just have a separate dedicated target bin?
        -
        """

        self.func = self.mapper
        self.nbins = nbins
        self.microstate_mapper = microstate_mapper
        self.n_original_pcoord_dims = n_original_pcoord_dims

        # TODO: Create simple model
        self.simple_model = msm_we.msm_we.modelWE()
        self.simple_model.initialize(
            basis_pcoord_bounds=...,
            target_pcoord_bounds=...,
            pcoord_ndim=...,
        )

        # TODO: Set model parameters
        self.simple_model.n_clusters = ...
        clusters_per_bin = ...
        target_bins = 1

        # TODO: These will be static values
        self.target_bin = ...
        self.basis_bin = ...

        # TODO: Initialize StratifiedClustering object's cluster centers
        self.clusterer = msm_we.msm_we.StratifiedClusters(previous_binmapper, self.simple_model, clusters_per_bin,
                                                          target_bins)
        for cluster_model in self.clusterer.cluster_models:
            # TODO: Initialize stratified k-means clusterers
            # Each one of these is a minibatchkmeans object.
            # It can be a regular k-means now (not doing any prediction on this), but
            cluster_model = ...

    def mapper(self, coords, mask, output):

        we_bin_assignments = np.full(len(coords), fill_value=np.nan)

        # To use stratified clustering, first load the ORIGINAL pcoords into stratified.pcoord1List, then call
        #   stratified.predict().
        # Segments in the basis will be assigned to whatever n_clusters is, and targets will be assigned to whatever
        #   n_clusters + 1 is.
        #  This isn't actually used for anything else, and no clustering happens for these, so I can actually
        #  set these arbitrarily.
        original_pcoords = coords[:, :self.n_original_pcoord_dims]
        basis_bin_idx = self.clusterer.model.n_clusters
        target_bin_idx = self.clusterer.model.n_clusters + 1
        self.clusterer.model.pcoord1List = original_pcoords

        # Now, do stratified clustering on the rest of the coordinates.
        # Each segment will be
        #   1. Assigned a WE bin, based on its pcoords and the provided bin mapper
        #   2. Discretized, according to the k-means model associated with that WE bin
        stratified_cluster_assignments = self.clusterer.predict(coords)

        # TODO: Map microstates to new WE bins, and populate we_bin_assignments
