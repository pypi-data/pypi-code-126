#!/usr/bin/env python
# coding: utf-8
from runml.dashboard.tabs.base_tab import Tab, Verbose
from runml.dashboard.widgets.data_drift_table_widget import DataDriftTableWidget


class DataDriftTab(Tab):
    widgets = [(DataDriftTableWidget("Data Drift"), Verbose.ALWAYS)]
