import numpy as np
import pandas as pd
import os
import sys
sys.path.insert(1, os.path.dirname(__file__))
import cis
from core import *


def trc(genotypes_t, counts_t, covariates_t=None, select_covariates=True,
        count_threshold=0, imputation='offset', mode='standard', return_af=False):
    """
    Inputs
      genotypes_t: dosages (variants x samples)
      counts_t: DESeq size factor-normalized read counts
      covariates_t: covariates matrix, first column must be intercept
      mode: if 'standard', parallel regression for each variant in genotypes_t
            if 'multi', multiple regression for all variants in genotypes_t

    Outputs:
      t-statistic, beta, beta_se {af, ma_samples, ma_counts}  (mode='standard')
      beta, beta_se  (mode='multi')
    """
    nonzero_t = counts_t != 0

    if imputation == 'offset':
        log_counts_t = counts_t.log1p()
    elif imputation == 'half_min':
        log_counts_t = counts_t.clone()
        log_counts_t[~nonzero_t] = log_counts_t[nonzero_t].min() / 2
        log_counts_t = log_counts_t.log()

    if covariates_t is not None:
        if select_covariates:
            # select significant covariates
            b_t, b_se_t = linreg(covariates_t[nonzero_t, :], log_counts_t[nonzero_t], dtype=torch.float32)
            tstat_t = b_t / b_se_t
            m = tstat_t.abs() > 2
            m[0] = True  # keep intercept
            sel_covariates_t = covariates_t[:, m]
        else:
            sel_covariates_t = covariates_t

        # Regress out covariates from non-zero counts, and keep zeros.
        # This follows the original mixQTL implementation, but may be
        # problematic when count_threshold is 0.
        residualizer = Residualizer(sel_covariates_t[nonzero_t, 1:])  # exclude intercept
        y_t = counts_t.clone()
        y_t[nonzero_t] = residualizer.transform(log_counts_t[nonzero_t].reshape(1,-1), center=True)
    else:
        y_t = log_counts_t

    m_t = counts_t >= count_threshold

    if mode == 'standard':
        res = cis.calculate_cis_nominal(genotypes_t[:, m_t] / 2, y_t[m_t], return_af=False)
        if return_af:
            af, ma_samples, ma_counts = get_allele_stats(genotypes_t)
            return *res, af, ma_samples, ma_counts
        else:
            return res

    elif mode.startswith('multi'):
        X_t = torch.cat([torch.ones([m_t.sum(), 1], dtype=bool).to(genotypes_t.device), genotypes_t[:, m_t].T / 2], axis=1)
        b_t, b_se_t = linreg(X_t, y_t[m_t], dtype=torch.float32)
        return b_t[1:], b_se_t[1:]


# def map_trc(genotype_df, variant_df, counts_df, counts_pos_df, covariates_df,
#             maf_threshold=0, count_threshold=0,
#             window=1000000, verbose=True):
#     """Standalone function for total read counts, e.g., for computing allelic fold-change."""
#
#     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#
#     if logger is None:
#         logger = SimpleLogger()
#
#     logger.write('mixQTL: total read counts')
#     # logger.write(f'  * {phenotype_df.shape[1]} samples')
#     # logger.write(f'  * {phenotype_df.shape[0]} phenotypes')
#
#     assert phenotype_df.columns.equals(covariates_df.index)
#     logger.write(f'  * {covariates_df.shape[1]} covariates')
#     # residualizer = Residualizer(torch.tensor(covariates_df.values, dtype=torch.float32).to(device))
#     # dof = phenotype_df.shape[1] - 2 - covariates_df.shape[1]
#
#     logger.write(f'  * {genotype_df.shape[0]} variants')
#     if maf_threshold > 0:
#         logger.write(f'  * applying in-sample {maf_threshold} MAF filter')
#
#     genotype_ix = np.array([genotype_df.columns.tolist().index(i) for i in phenotype_df.columns])
#     genotype_ix_t = torch.from_numpy(genotype_ix).to(device)
#
#     # res_df = []
#     igc = genotypeio.InputGeneratorCis(genotype_df, variant_df, phenotype_df, phenotype_pos_df, group_s=group_s, window=window)
#     if igc.n_phenotypes == 0:
#         raise ValueError('No valid phenotypes found.')
#     start_time = time.time()
#
#     for k, (phenotype, genotypes, genotype_range, phenotype_id) in enumerate(igc.generate_data(verbose=verbose), 1):
#         # copy genotypes to GPU
#         genotypes_t = torch.tensor(genotypes, dtype=torch.float).to(device)
#         genotypes_t = genotypes_t[:,genotype_ix_t]
#         impute_mean(genotypes_t)
#
#         if maf_threshold > 0:
#             maf_t = calculate_maf(genotypes_t)
#             mask_t = maf_t >= maf_threshold
#             genotypes_t = genotypes_t[mask_t]
#             mask = mask_t.cpu().numpy().astype(bool)
#             genotype_range = genotype_range[mask]
#
#     #     # filter monomorphic variants
#     #     mono_t = (genotypes_t == genotypes_t[:, [0]]).all(1)
#     #     if mono_t.any():
#     #         genotypes_t = genotypes_t[~mono_t]
#     #         genotype_range = genotype_range[~mono_t.cpu()]
#     #         if warn_monomorphic:
#     #             logger.write(f'    * WARNING: excluding {mono_t.sum()} monomorphic variants')
#     #
#     #     if genotypes_t.shape[0] == 0:
#     #         logger.write(f'WARNING: skipping {phenotype_id} (no valid variants)')
#     #         continue
#     #
#     #     phenotype_t = torch.tensor(phenotype, dtype=torch.float).to(device)
#     #
#     #     res = calculate_cis_permutations(genotypes_t, phenotype_t, permutation_ix_t,
#     #                                      residualizer=residualizer, random_tiebreak=random_tiebreak)
#     #     r_nominal, std_ratio, var_ix, r2_perm, g = [i.cpu().numpy() for i in res]
#     #     var_ix = genotype_range[var_ix]
#     #     variant_id = variant_df.index[var_ix]
#     #     tss_distance = variant_df['pos'].values[var_ix] - igc.phenotype_tss[phenotype_id]
#     #     res_s = prepare_cis_output(r_nominal, r2_perm, std_ratio, g, genotypes_t.shape[0], dof, variant_id, tss_distance, phenotype_id, nperm=nperm)
#     #     if beta_approx:
#     #         res_s[['pval_beta', 'beta_shape1', 'beta_shape2', 'true_df', 'pval_true_df']] = calculate_beta_approx_pval(r2_perm, r_nominal*r_nominal, dof)
#     #     res_df.append(res_s)
#
#     # res_df = pd.concat(res_df, axis=1, sort=False).T
#     # res_df.index.name = 'phenotype_id'
#     # logger.write(f'  Time elapsed: {(time.time()-start_time)/60:.2f} min')
#     # logger.write('done.')
#     # return res_df.astype(output_dtype_dict).infer_objects()
