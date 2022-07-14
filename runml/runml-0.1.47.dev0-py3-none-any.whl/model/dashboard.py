#!/usr/bin/env python
# coding: utf-8

from dataclasses import dataclass
from typing import List

from runml.model.widget import BaseWidgetInfo


@dataclass
class DashboardInfo:
    name: str
    widgets: List[BaseWidgetInfo]
