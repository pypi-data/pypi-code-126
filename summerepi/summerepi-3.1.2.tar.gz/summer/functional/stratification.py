import numpy as np

def adjust_population_split(model, strat: str, dest_filter: dict, proportions: dict):
    """Adjust the initial population to redistribute the population for a particular
    stratification, over a subset of some other strata

    Args:
        strat (str): The stratification to redistribute over
        dest_filter (dict): Subset of (other) strata to filter the split by
        proportions (dict): Proportions of new split (must have all strata specified)

    """

    msg = f"No stratification {strat} found in model"
    assert strat in [s.name for s in model._stratifications], msg

    model_strat = [s for s in model._stratifications if s.name == strat][0]

    msg = "All strata must be specified in proportions"
    assert set(model_strat.strata) == set(proportions), msg

    msg = "Proportions must sum to 1.0"
    np.testing.assert_allclose(sum(proportions.values()), 1.0, err_msg=msg)

    strat_comps = [c for c in self.compartments if strat in c.strata]
    # Filter by only the subset we're setting in split_map
    strat_comps = filter_by_strata(strat_comps, dest_filter)

    usg = get_unique_strat_groups(strat_comps, strat)

    for g in usg:
        mcomps = self._get_matching_compartments(g.name, g.strata)
        idx = [c.idx for c in mcomps]
        total = self.initial_population[idx].sum()
        for c in mcomps:
            k = c.strata[strat]
            target_prop = proportions[k]
            self.initial_population[c.idx] = total * target_prop