import datetime
import copy
import sys

import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import theano.tensor as tt

try:
    import covid19_inference as cov19
except ModuleNotFoundError:
    sys.path.append("../")
    import covid19_inference as cov19

# Get data from owd
owd = cov19.data_retrieval.OWD(auto_download=True)
jhu = cov19.data_retrieval.JHU(auto_download=True)
new_cases = jhu.get_new(country="Israel")
new_cases_cum = jhu.get_total(country="Israel")
population = owd._filter(value="population", country="Israel")
vacination = owd.get_new(value="vacinations", country="Israel")
vacination_total = owd.get_total(value="vacinations", country="Israel")
vacination_percent = vacination_total / population[-1]


data_begin = datetime.datetime(2020, 11, 15)
data_end = datetime.datetime(2021, 3, 29)
daterange = pd.date_range(data_begin, data_end)
vacination = vacination.reindex(daterange, fill_value=0)


""" Changepoints
We create one slow changepoint and one sharp one
"""
# change points like in the paper
change_points = [
    # smooth
    dict(
        # account for new implementation where transients_day is centered, not begin
        pr_mean_date_transient=vacination_percent[vacination_percent > 0.2].index[0],
        pr_median_transient_len=20,
        pr_sigma_transient_len=0.3,
        pr_sigma_date_transient=1,
        pr_median_lambda=0.12,
        pr_sigma_lambda=0.5,
    ),
    # sharp maybe at 70%
    dict(
        pr_mean_date_transient=vacination_percent[vacination_percent > 0.8].index[0],
        pr_sigma_date_transient=1,
        pr_median_lambda=1 / 8,
        pr_sigma_lambda=0.5,
        pr_sigma_transient_len=0.5,
    ),
]


# set model parameters
params_model = dict(
    new_cases_obs=new_cases.reindex(daterange)[:],
    data_begin=data_begin,
    new_vacinations=vacination,
    fcast_len=0,
    diff_data_sim=16,
    N_population=population[-1],
)


# Median of the prior for the delay in case reporting, we assume 10 days
pr_delay = 10
S_begin = new_cases_cum[data_begin]

with cov19.model.Cov19Model(**params_model) as this_model:
    # Create the an array of the time dependent infection rate lambda
    lambda_t_log = cov19.model.lambda_t_with_sigmoids(
        pr_median_lambda_0=0.4,
        pr_sigma_lambda_0=0.5,
        change_points_list=change_points,  # The change point priors we constructed earlier
        name_lambda_t="lambda_t",  # Name for the variable in the trace (see later)
    )

    # set prior distribution for the recovery rate
    mu = pm.Lognormal(name="mu", mu=np.log(1 / 8), sigma=0.2)

    # This builds a decorrelated prior for I_begin for faster inference.
    # It is not necessary to use it, one can simply remove it and use the default argument
    # for pr_I_begin in cov19.SIR
    prior_I = cov19.model.uncorrelated_prior_I(
        lambda_t_log=lambda_t_log,
        mu=mu,
        pr_median_delay=pr_delay,
        name_I_begin="I_begin",
        name_I_begin_ratio_log="I_begin_ratio_log",
        pr_sigma_I_begin=2,
        n_data_points_used=5,
    )

    # Use lambda_t_log and mu to run the SIR model
    new_cases = cov19.model.SIR_with_vacination(
        lambda_t_log=lambda_t_log,
        vac=tt.constant(this_model.new_vacinations),
        mu=mu,
        name_new_I_t="new_I_t",
        name_I_t="I_t",
        name_I_begin="I_begin",
        pr_I_begin=prior_I,
        pr_S_begin=pm.Normal(
            "S_begin", mu=S_begin, sigma=2.0, shape=this_model.shape_of_regions
        ),
    )
    tt.printing.Print("new_cases")(new_cases.shape)
    # Delay the cases by a lognormal reporting delay
    new_cases = cov19.model.delay_cases(
        cases=new_cases,
        name_cases="delayed_cases",
        name_delay="delay",
        name_width="delay-width",
        pr_mean_of_median=pr_delay,
        pr_sigma_of_median=0.2,
        pr_median_of_width=0.3,
    )

    # Modulate the inferred cases by a abs(sin(x)) function, to account for weekend effects
    # Also adds the "new_cases" variable to the trace that has all model features.
    new_cases = cov19.model.week_modulation(
        cases=new_cases,
        name_cases="new_cases",
        name_weekend_factor="weekend_factor",
        name_offset_modulation="offset_modulation",
        week_modulation_type="abs_sine",
        pr_mean_weekend_factor=0.3,
        pr_sigma_weekend_factor=0.5,
        weekend_days=(6, 7),
    )

    # Define the likelihood, uses the new_cases_obs set as model parameter
    cov19.model.student_t_likelihood(new_cases)

trace = pm.sample(model=this_model, tune=500, draws=500, init="advi+adapt_diag")
cov19.plot.set_rcparams(cov19.plot.get_rcparams_default())
cov19.plot.rcParams.draw_ci_50 = True

fig, axes = cov19.plot.timeseries_overview(
    this_model,
    trace,
    offset=new_cases_cum[0],
    forecast_label="Pessimistic",
    forecast_heading=r"$\bf Scenarios\!:$",
    add_more_later=True,
    color="tab:red",
)
