#!/usr/bin/env python
# coding: utf-8
from runml.dashboard.tabs.base_tab import Tab, Verbose
from runml.dashboard.widgets.num_output_drift_widget import NumOutputDriftWidget
from runml.dashboard.widgets.num_output_corr_widget import NumOutputCorrWidget
from runml.dashboard.widgets.num_output_values_widget import NumOutputValuesWidget
from runml.dashboard.widgets.num_target_pred_feature_table_widget import NumTargetPredFeatureTable


class NumTargetDriftTab(Tab):
    widgets = [
        (NumOutputDriftWidget("Target Drift"), Verbose.ALWAYS),
        (NumOutputCorrWidget("Target Correlations"), Verbose.FULL),
        (NumOutputValuesWidget("Target Values"), Verbose.FULL),
        (NumOutputDriftWidget("Prediction Drift", "prediction"), Verbose.ALWAYS),
        (NumOutputCorrWidget("Prediction Correlations", "prediction"), Verbose.FULL),
        (NumOutputValuesWidget("Prediction Values", "prediction"), Verbose.FULL),
        (NumTargetPredFeatureTable("Target (Prediction) Behavior By Feature"), Verbose.FULL),
    ]
