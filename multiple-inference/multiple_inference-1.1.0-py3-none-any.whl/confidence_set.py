"""Simultaneous confidence sets and multiple hypothesis testing.

References:

    .. code-block::

        @article{storey2003statistical,
            title={Statistical significance for genomewide studies},
            author={Storey, John D and Tibshirani, Robert},
            journal={Proceedings of the National Academy of Sciences},
            volume={100},
            number={16},
            pages={9440--9445},
            year={2003},
            publisher={National Acad Sciences}
        }

        @article{romano2005stepwise,
            title={Stepwise multiple testing as formalized data snooping},
            author={Romano, Joseph P and Wolf, Michael},
            journal={Econometrica},
            volume={73},
            number={4},
            pages={1237--1282},
            year={2005},
            publisher={Wiley Online Library}
        }

        @techreport{mogstad2020inference,
            title={Inference for ranks with applications to mobility across neighborhoods and academic achievement across countries},
            author={Mogstad, Magne and Romano, Joseph P and Shaikh, Azeem and Wilhelm, Daniel},
            year={2020},
            institution={National Bureau of Economic Research}
        }
"""
from __future__ import annotations

import warnings
from itertools import combinations
from typing import Any, Sequence, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.optimize import minimize
from scipy.stats import multivariate_normal, norm

from multiple_inference.base import ColumnsType, ModelBase, ResultsBase


class ConfidenceSetResults(ResultsBase):
    """Results for simultaneous confidence sets.

    Subclasses :class:`multiple_inference.base.ResultsBase`.

    Args:
        n_samples (int, optional): Number of samples to draw when approximating the
            confidence set. Defaults to 10000.
    """

    _default_title = "Confidence set results"

    def __init__(self, *args: Any, n_samples: int = 10000, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.params = self.model.mean.copy()

        # draw random values for confidence set approximation
        self._std_diagonal = np.sqrt(self.model.cov.diagonal())
        rvs = multivariate_normal.rvs(
            np.zeros(self.model.n_params),
            self.model.cov,
            size=n_samples,
            random_state=self.model.random_state,
        )
        rvs /= self._std_diagonal
        self._rvs = np.hstack([rvs, -rvs])
        self._set_pvalues()
        self._set_qvalues()

    def _set_pvalues(self):
        if self.model.n_params == 1:
            self.pvalues = 2 * np.atleast_1d(
                norm.cdf(-abs(self.model.mean[0]), 0, np.sqrt(self.model.cov[0, 0]))
            )
        else:
            params = np.expand_dims(self.params, -1)
            arr = self._rvs.max(axis=1) * np.expand_dims(self._std_diagonal, -1)
            self.pvalues = np.array(
                [(params - arr < 0).mean(axis=1), (params + arr > 0).mean(axis=1)]
            ).min(axis=0)

    def _set_qvalues(self):
        if self.model.n_params == 1:
            self.qvalues = self.pvalues.copy()
        else:
            # get conventional pvalues
            pvalues = norm.cdf(self.params / self._std_diagonal)
            # convert to 2-sided pvalues
            pvalues = 2 * np.min([pvalues, 1 - pvalues], axis=0)
            argsort = (-pvalues).argsort()
            pvalues = pvalues[argsort]
            # define x over (0, .9 * max pvalue)
            # extending x too close to the max pvalue introduces noise
            x = np.linspace(0, 0.9 * pvalues[0])
            pi0 = (pvalues > np.expand_dims(x, 1)).mean(axis=1) / (1 - x)
            # fit an exponential smoothing spline to estimate the true null rate
            spline = lambda x, params: params[0] + params[1] * np.exp(
                -params[1] * x / params[2]
            )
            params = minimize(
                lambda params: ((spline(x, params) - pi0) ** 2).sum(), [0, 1, 1]
            ).x
            true_null_rate = np.clip(spline(pvalues[0], params), 0, 1)
            # compute qvalues
            qvalues = [1]
            for i, pvalue in enumerate(pvalues):
                qvalues.append(
                    min(
                        true_null_rate * pvalue * len(pvalues) / (len(pvalues) - i),
                        qvalues[-1],
                    )
                )
            self.qvalues = np.array(qvalues[1:])[argsort.argsort()]

    def _conf_int(self, alpha: float, indices: np.ndarray) -> np.ndarray:
        if self.model.n_params == 1:
            return np.atleast_2d(
                norm.ppf(
                    [alpha / 2, 1 - alpha / 2],
                    self.model.mean[0],
                    np.sqrt(self.model.cov[0, 0]),
                )
            )

        params = self.params[indices]
        arr = (
            np.quantile(self._rvs.max(axis=1), 1 - alpha) * self._std_diagonal[indices]
        )
        return np.array([params - arr, params + arr]).T

    def test_hypotheses(
        self, alpha: float = 0.05, columns: ColumnsType = None, two_tailed: bool = True
    ) -> Union[pd.DataFrame, pd.Series]:
        """Test the null hypothesis that the parameter is equal to 0.

        Args:
            alpha (float, optional): Significance level. Defaults to 0.05.
            columns (ColumnsType, optional): Selected columns. Defaults to None.
            two_tailed (bool, optional): Run two-tailed hypothesis tests. Set to False
                to run one-tailed hypothesis tests. Defaults to True.

        Returns:
            Union[pd.DataFrame, pd.Series]: Results dataframe (if two-tailed) or series
                (if one-tailed).
        """
        # use pvalues to reject hypotheses to control the familywise error rate
        if two_tailed:
            params = np.concatenate([self.params, -self.params])
            rvs = self._rvs
            std_diagonal = np.concatenate([self._std_diagonal, self._std_diagonal])
        else:
            params = self.params
            rvs = self._rvs[:, : self.model.n_params]
            std_diagonal = self._std_diagonal

        rejected, newly_rejected = np.full(rvs.shape[1], False), None
        while newly_rejected is None or (newly_rejected.any() and not rejected.all()):
            quantile = np.quantile(rvs[:, ~rejected].max(axis=1), 1 - alpha)
            newly_rejected = (params - quantile * std_diagonal > 0) & ~rejected
            rejected = rejected | newly_rejected

        indices = self.model.get_indices(columns, self.exog_names)
        if two_tailed:
            return pd.DataFrame(
                rejected.reshape(2, -1).T[indices],
                columns=["param>0", "param<0"],
                index=self.exog_names[indices],
            )
        return pd.Series(
            rejected[indices], name="param>0", index=self.exog_names[indices]
        )

    def _make_summary_header(self, alpha: float) -> list[str]:
        return [
            "coef (conventional)",
            "pvalue",
            "qvalue",
            f"{1-alpha} CI lower",
            f"{1-alpha} CI upper",
        ]

    def _make_summary_data(
        self, alpha: float, indices: np.ndarray, **kwargs: Any
    ) -> np.ndarray:
        if not hasattr(self, "params"):
            raise AttributeError("Results object does not have `params` attribute.")

        return np.hstack(
            (
                np.array([self.params, self.pvalues, self.qvalues]).T[indices],
                self.conf_int(alpha, indices, **kwargs),
            )
        )


class ConfidenceSet(ModelBase):
    """Model for simultaneous confidence sets.

    Examples:

        .. testcode::

            import numpy as np
            from multiple_inference.confidence_set import ConfidenceSet

            x = np.arange(-1, 2)
            cov = np.identity(3) / 10
            model = ConfidenceSet(x, cov)
            results = model.fit()
            print(results.summary())

        .. testoutput::
            :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

            Confidence set results
            ================================================================
               coef (conventional) pvalue qvalue 0.95 CI lower 0.95 CI upper
            ----------------------------------------------------------------
            x0              -1.000  0.004  0.002        -1.755        -0.245
            x1               0.000  1.000  1.000        -0.755         0.755
            x2               1.000  0.004  0.002         0.245         1.755
            ===============
            Dep. Variable y
            ---------------

        .. testcode::

            print(results.test_hypotheses())

        .. testoutput::
            :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

                param>0  param<0
            x0    False     True
            x1    False    False
            x2     True    False
    """

    _results_cls = ConfidenceSetResults


class AverageComparison(ConfidenceSet):
    """Compare each parameter to the average value across all parameters.

    Subclasses :class:`ConfidenceSet`.

    Args:
        *args (Any): Passed to :class:`ConfidenceSet`.
        **kwargs (Any): Passed to :class:`ConfidenceSet`.

    Examples:

        .. testcode::

            import numpy as np
            from multiple_inference.confidence_set import AverageComparison

            x = np.arange(-1, 2)
            cov = np.identity(3) / 10
            model = AverageComparison(x, cov)
            results = model.fit()
            print(results.summary())

        .. testoutput::
            :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

            Confidence set results
            ================================================================
               coef (conventional) pvalue qvalue 0.95 CI lower 0.95 CI upper
            ----------------------------------------------------------------
            x0              -1.000  0.000  0.000        -1.603        -0.397
            x1               0.000  1.000  1.000        -0.603         0.603
            x2               1.000  0.000  0.000         0.397         1.603
            ===============
            Dep. Variable y
            ---------------
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        identity = np.identity(self.n_params)
        cov_inv = np.linalg.inv(self.cov)
        projection = (
            self.X @ np.linalg.inv(self.X.T @ cov_inv @ self.X) @ self.X.T @ cov_inv
        )
        self.mean = (identity - projection) @ self.mean
        cov = (identity - projection) @ self.cov @ (identity - projection).T
        if np.isnan(cov).all():
            warnings.warn(
                f"Error encountered in recomputing covariance matrix. "
                "Using original covariance matrix instead.",
                RuntimeWarning,
            )
        else:
            self.cov = cov


class BaselineComparison(ConfidenceSet):
    """Compare parameters to a baseline parameter.

    Subclasses :class:`ConfidenceSet`.

    Args:
        baseline (Union[int, str]): Index or name of the baseline parameter.

    Examples:

        .. testcode::

            import numpy as np
            from multiple_inference.confidence_set import BaselineComparison

            x = np.arange(-1, 2)
            cov = np.identity(3) / 10
            model = BaselineComparison(x, cov, exog_names=["x0", "x1", "x2"], baseline="x0")
            results = model.fit()
            print(results.summary())

        .. testoutput::
            :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

            Confidence set results
            ================================================================
               coef (conventional) pvalue qvalue 0.95 CI lower 0.95 CI upper
            ----------------------------------------------------------------
            x1               1.000  0.045  0.012         0.022         1.978
            x2               2.000  0.000  0.000         1.022         2.978
            ===============
            Dep. Variable y
            ---------------
    """

    def __init__(self, *args, baseline: Union[int, str], **kwargs):
        super().__init__(*args, **kwargs)
        index = int(
            baseline
            if isinstance(baseline, (float, int))
            else list(self.exog_names).index(baseline)
        )
        self.n_params -= 1
        self.mean = np.delete(self.mean, index) - self.mean[index]
        self.cov = (
            np.delete(np.delete(self.cov, index, axis=0), index, axis=1)
            + self.cov[index, index]
        )
        if self._exog_names is not None:
            self.exog_names = np.delete(self.exog_names, index)


class PairwiseComparisonResults(ConfidenceSetResults):
    """Results of pairwise comparisons.

    Subclasses :class:`ConfidenceSetResults`.

    Args:
        n_samples (int, optional): Number of samples to draw to obtain critical
            values. Defaults to 10000.
        groups (np.ndarray, optional): (# params,) array of parameter groups.
            Defaults to None.

    Raises:
        ValueError: Length of ``groups`` must match the number of parameters.
    """

    _default_title = "Pairwise comparisons"

    def __init__(
        self,
        *args: Any,
        n_samples: int = 10000,
        groups: np.ndarray = None,
        **kwargs: Any,
    ):

        super().__init__(*args, **kwargs)
        self._groups = (
            np.zeros(self.model.n_params) if groups is None else np.array(groups)
        )
        if len(self._groups) != self.model.n_params:
            raise ValueError(
                "Length of groups must equal the number of parameters. Got "
                f"{self.model.n_params} parameters and groups of length "
                f" {len(self._groups)}."
            )

        variance = self.model.cov.diagonal()
        rvs = multivariate_normal.rvs(
            self.model.mean,
            self.model.cov,
            size=n_samples,
            random_state=self.model.random_state,
        )
        exog_names, params, delta_variance, delta_rvs = [], [], [], []
        pairwise_groups = []
        for group in np.unique(self._groups):
            mask = self._groups == group
            pairwise_groups += int(0.5 * mask.sum() * (mask.sum() - 1)) * [group]
            group_exog_names, group_params, group_variance, group_rvs = (
                self.exog_names[mask],
                self.params[mask],
                variance[mask],
                rvs[:, mask],
            )
            for i in range(mask.sum()):
                exog_names.append(
                    [
                        f"{name} - {group_exog_names[i]}"
                        for name in group_exog_names[i + 1 :]
                    ]
                )
                params.append(group_params[i + 1 :] - group_params[i])
                # variance of the differences between x_i and x_j
                delta_variance.append(group_variance[i + 1 :] + group_variance[i])
                # random sample of the differences between x_i and x_j
                delta_rvs.append(
                    group_rvs[:, i + 1 :] - np.expand_dims(group_rvs[:, i], -1)
                )

        self.exog_names = np.concatenate(exog_names)
        self.params = np.concatenate(params)
        self._std_diagonal = np.sqrt(np.concatenate(delta_variance))
        rvs = (np.hstack(delta_rvs) - self.params) / self._std_diagonal
        self._rvs = np.hstack([rvs, -rvs])
        self._pairwise_groups = np.array(pairwise_groups)
        self._set_pvalues()
        self._set_qvalues()

    def test_hypotheses(
        self,
        alpha: float = 0.05,
        columns: ColumnsType = None,
        criterion: str = "fwer",
        groups: Sequence = None,
        wide: bool = True,
    ) -> Union[pd.DataFrame, dict[Any, pd.DataFrame]]:
        """Test pairwise hypotheses.

        Args:
            alpha (float, optional): Significance level. Defaults to .05.
            columns (ColumnsType, optional): Selected columns. In wide format, these are
                the original column names (e.g., "x0"). In long format, these are the
                names of the differences (e.g., "x1 - x0"). Defaults to None.
            criterion (str, optional): "fwer" to control for the family-wise error rate
                (using pvalues), "fdr" to control for the false discovery rate (using
                qvalues). Defaults to "fwer".
            groups (Sequence, optional). Selected groups of parameters. Defaults to None.
            wide (bool, optional): Return the results is wide (square) format. Ignored
                when controlling for the false discovery rate. Defaults to True.

        Raises:
            ValueError: ``criterion`` must be one of "fwer" or "fdr".

        Returns:
            Union[pd.DataFrame, dict[Any, pd.DataFrame]]: Results dataframe if only one
                group is used, mapping of group name to results dataframe if multiple
                groups are used.

        Notes:
            When controlling for the familywise error rate, the null hypotheses are
            $$mu_k \leq \mu_j$$. When controlling for the false discovery rate, the null
            hypotheses are $$\mu_k = \mu_j$$.
        """
        if criterion not in ("fwer", "fdr"):
            raise ValueError(f"criterion should be in 'fwer', 'fdr', got {criterion}.")

        if criterion == "fwer":
            if not wide:
                return super().test_hypotheses(alpha, columns)
            rejected = super().test_hypotheses(alpha).values
        else:
            rejected = self.qvalues < alpha
            rejected = np.vstack([rejected, rejected]).T

        # reshape rejected array into a square matrix
        return_value = {}
        for group in groups or np.unique(self._groups):
            mask = self._groups == group
            pairwise_mask = self._pairwise_groups == group
            n_params = mask.sum()
            tri = np.full((n_params, n_params), False)
            indices = np.triu_indices(n_params, 1)
            tri[indices] = rejected[pairwise_mask, 0]
            tri[(indices[1], indices[0])] = rejected[pairwise_mask, 1]

            exog_names = self.model.exog_names[mask]
            indices = self.model.get_indices(columns, exog_names)
            column_names = exog_names[indices]
            return_value[group] = pd.DataFrame(
                tri[indices][:, indices], index=column_names, columns=column_names
            )

        return (
            list(return_value.values())[0] if len(return_value) == 1 else return_value
        )

    def hypothesis_heatmap(
        self,
        *args: Any,
        title: str = None,
        axes=None,
        triangular: bool = False,
        **kwargs: Any,
    ):
        """Create a heatmap of pairwise hypothesis tests.

        Args:
            title (str, optional): Title.
            axes (Union[AxesSubplot, Sequence[AxesSubplot]], optional): Axes to write
                on. Defaults to None.
            triangular (bool, optional): Display the results in a triangular (as opposed
                to square) output. Usually, you should set this to True if and only if
                your columns are sorted. Defaults to False.

        Returns:
            np.ndarray: Array of axes.
        """

        def write_heatmap(group, matrix, ax):
            if triangular:
                mask = np.zeros_like(matrix)
                mask[np.triu_indices_from(mask)] = True
            else:
                mask = None

            sns.heatmap(
                matrix,
                cbar=False,
                ax=ax,
                yticklabels=matrix.index,
                xticklabels=matrix.columns,
                mask=mask,
                square=True,
                cmap=sns.color_palette()[3:1:-1],
                center=0.5,
            )
            ax.set_title(
                (title or self.title) + ("" if group is None else f" group = {group}")
            )
            ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

        results = self.test_hypotheses(*args, **kwargs)
        if isinstance(results, dict):
            if axes is None:
                fig, axes = plt.subplots(len(results))
                fig.tight_layout()
            for (group, matrix), ax in zip(results.items(), axes):
                write_heatmap(group, matrix, ax)
        else:
            if axes is None:
                _, axes = plt.subplots()
            write_heatmap(None, results, axes)

        return axes

    def _make_summary_header(self, alpha: float) -> list[str]:
        return [
            "delta (conventional)",
            "pvalue",
            "qvalue",
            f"{1-alpha} CI lower",
            f"{1-alpha} CI upper",
        ]


class PairwiseComparison(ConfidenceSet):
    """Compute pairwise comparisons.

    Examples:

        .. testcode::

            import numpy as np
            from multiple_inference.confidence_set import PairwiseComparison

            x = np.arange(-1, 2)
            cov = np.identity(3) / 10
            model = PairwiseComparison(x, cov)
            results = model.fit()
            print(results.summary())

        .. testoutput::
            :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

            Pairwise comparisons
            ======================================================================
                    delta (conventional) pvalue qvalue 0.95 CI lower 0.95 CI upper
            ----------------------------------------------------------------------
            x1 - x0                1.000  0.061  0.017        -0.031         2.031
            x2 - x0                2.000  0.000  0.000         0.969         3.031
            x2 - x1                1.000  0.061  0.017        -0.031         2.031
            ===============
            Dep. Variable y
            ---------------

        .. testcode::

            print(results.test_hypotheses())

        .. testoutput::
            :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

                   x0     x1     x2
            x0  False  False   True
            x1  False  False  False
            x2  False  False  False

        This means that parameter x2 is significantly greater than x0.
    """

    _results_cls = PairwiseComparisonResults


class MarginalRankingResults(ResultsBase):
    """Marginal ranking results."""

    _default_title = "Marginal ranking"

    def __init__(
        self, model: MarginalRanking, *args: Any, n_samples: int = 10000, **kwargs: Any
    ):
        super().__init__(model, *args, **kwargs)
        self.params = (-self.model.mean).argsort().argsort() + 1
        self._baseline_comparisons = [
            BaselineComparison(model.mean, model.cov, baseline=i).fit(
                n_samples=n_samples
            )
            for i in range(model.n_params)
        ]

    def _conf_int(self, alpha: float, indices: np.ndarray) -> np.array:
        def get_rank_ci(results):
            hypotheses_count = results.test_hypotheses(alpha).sum(axis=0)
            return [hypotheses_count[0], self.model.n_params - hypotheses_count[1] - 1]

        return (
            np.array([get_rank_ci(self._baseline_comparisons[i]) for i in indices]) + 1
        )

    def _make_summary_header(self, alpha: float) -> list[str]:
        return [
            "rank (conventional)",
            "pvalue",
            f"{1-alpha} CI lower",
            f"{1-alpha} CI upper",
        ]


class MarginalRanking(ConfidenceSet):
    """Estimate rankings with marginal confidence intervals.

    Subclasses :class:`ConfidenceSet`.

    Examples:

        .. testcode::

            import numpy as np
            from multiple_inference.confidence_set import MarginalRanking

            x = np.arange(-1, 2)
            cov = np.diag([1, 2, 3]) / 10
            model = MarginalRanking(x, cov)
            results = model.fit()
            print(results.summary())

        .. testoutput::
            :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

                              Marginal ranking
            =========================================================
               rank (conventional) pvalue 0.95 CI lower 0.95 CI upper
            ---------------------------------------------------------
            x0               3.000    nan         2.000         3.000
            x1               2.000    nan         1.000         3.000
            x2               1.000    nan         1.000         2.000
            ===============
            Dep. Variable y
            ---------------

    """

    _results_cls = MarginalRankingResults


class SimultaneousRankingResults(ResultsBase):
    """Simultaneous ranking results."""

    _default_title = "Simultaneous ranking"

    def __init__(
        self,
        model: SimultaneousRanking,
        *args: Any,
        n_samples: int = 10000,
        **kwargs: Any,
    ):
        super().__init__(model, *args, **kwargs)
        self.params = (-model.mean).argsort().argsort() + 1
        pairwise_model = PairwiseComparison(model.mean, model.cov)
        self._pairwise_comparison = pairwise_model.fit(n_samples=n_samples)

        # compute test statistics for finding the top tau parameters
        # self._test_stats is a (# params, # params) matrix where
        # `self._test_stats[tau, k]`` is the test statistic for the null hypothesis that
        # the parameter k is not in the top tau parameters
        indices = np.triu_indices(model.n_params, 1)
        self._test_stats = np.full((model.n_params, model.n_params), 0.0)
        test_stats = (
            self._pairwise_comparison.params / self._pairwise_comparison._std_diagonal
        )
        self._test_stats[indices] = -test_stats
        self._test_stats[(indices[1], indices[0])] = test_stats
        self._test_stats = np.sort(self._test_stats, 0)[::-1]

        # compute random values to find the critical values for finding the top tau
        # parameters
        # self._rvs is a (# samples, # params, # params) matrix where
        # `self._rvs[n, k, l]`` is the nth sample of the studentized param_k - param_l
        def reshape(arr):
            arr = arr[: int(len(arr) / 2)]
            matrix = np.zeros((model.n_params, model.n_params))
            matrix[indices] = arr
            matrix[(indices[1], indices[0])] = -arr
            return matrix

        self._rvs = np.apply_along_axis(reshape, -1, self._pairwise_comparison._rvs)

    def _conf_int(self, alpha: float, indices: np.ndarray) -> np.ndarray:
        hypothesis_matrix = self._pairwise_comparison.test_hypotheses(alpha).values
        return (
            np.array(
                [
                    hypothesis_matrix.sum(axis=1),
                    self.model.n_params - hypothesis_matrix.sum(axis=0) - 1,
                ]
            ).T[indices]
            + 1
        )

    def compute_best_params(
        self, n_best_params: int = 1, alpha: float = 0.05, superset: bool = True
    ) -> pd.Series:
        """Compute the set of best (largest) parameters.

        Find the set of parameters such that the truly best ``n_best_params`` parameters
        are in this set with probability ``1-alpha``. Or, find the set of parameters
        such that these parameters are in the truly best ``n_best_params`` parameters
        with probability ``1-alpha``.

        Args:
            n_best_params (int, optional): Number of best parameters. Defaults to 1.
            alpha (float, optional): Significance level. Defaults to 0.05.
            superset (bool, optional): Indicates that the returned set is a superset of
                the truly best n parameters. If False, the returned set is a subset of
                the truly best n parameters. Defaults to True.

        Returns:
            pd.Series: Indicates which parameters are in the selected set.
        """
        if superset:
            test_stats = self._test_stats[n_best_params - 1]
        else:
            test_stats = -self._test_stats[n_best_params]
            n_best_params = self.model.n_params - n_best_params

        subsets = []
        for indices in combinations(np.arange(self.model.n_params), n_best_params - 1):
            arr = np.full(self.model.n_params, True)
            if len(indices) > 0:
                arr[list(indices)] = False

            subsets.append(arr)

        compute_critical_value = lambda subset: np.quantile(
            rvs[:, :, subset].max(axis=(1, 2)), 1 - alpha
        )
        rejected, newly_rejected = np.full(self.model.n_params, False), None
        while newly_rejected is None or (newly_rejected.any() and not rejected.all()):
            rvs = self._rvs[:, ~rejected]
            critical_value = max([compute_critical_value(subset) for subset in subsets])
            newly_rejected = (test_stats > critical_value) & ~rejected
            rejected = newly_rejected | rejected

        return pd.Series(
            ~rejected if superset else rejected, index=self.model.exog_names
        )

    def _make_summary_header(self, alpha: float) -> list[str]:
        return [
            "rank (conventional)",
            "pvalue",
            f"{1-alpha} CI lower",
            f"{1-alpha} CI upper",
        ]


class SimultaneousRanking(ConfidenceSet):
    """Estimate rankings with simultaneous confidence intervals.

    Subclasses :class:`ConfidenceSet`.

    Examples:

        .. testcode::

            import numpy as np
            from multiple_inference.confidence_set import SimultaneousRanking

            x = np.arange(3)
            cov = np.identity(3) / 10
            model = SimultaneousRanking(x, cov)
            results = model.fit()
            print(results.summary())

        .. testoutput::
            :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

                               Simultaneous ranking
            =========================================================
               rank (conventional) pvalue 0.95 CI lower 0.95 CI upper
            ---------------------------------------------------------
            x0               3.000    nan         2.000         3.000
            x1               2.000    nan         1.000         3.000
            x2               1.000    nan         1.000         2.000
            ===============
            Dep. Variable y
            ---------------

        .. testcode::

            print(results.compute_best_params())

        .. testoutput::
            :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

            x0    False
            x1    False
            x2     True
            dtype: bool

        This we can be 95% confident that the best (largest) parameter is x2.
    """

    _results_cls = SimultaneousRankingResults
