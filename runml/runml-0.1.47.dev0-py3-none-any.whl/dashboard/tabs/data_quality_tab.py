#!/usr/bin/env python
# coding: utf-8
from runml.dashboard.tabs.base_tab import Tab, Verbose
from runml.dashboard.widgets.data_quality_features_widget import DataQualityFeaturesWidget
from runml.dashboard.widgets.data_quality_summary import DataQualitySummaryWidget
from runml.dashboard.widgets.data_quality_correlations import DataQualityCorrelationsWidget


class DataQualityTab(Tab):
    widgets = [
        (DataQualitySummaryWidget("Data Summary"), Verbose.ALWAYS),
        (DataQualityFeaturesWidget("Features"), Verbose.ALWAYS),
        (DataQualityCorrelationsWidget("Correlations"), Verbose.ALWAYS)
    ]
