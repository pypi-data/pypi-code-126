#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   date_test.py
@Time    :   2022/07/11 17:37:35
@Author  :   Desire
@Version :   1.0
@Desc    :   None
"""

import os
import sys

sys.path.insert(1, os.getcwd())
# here put the import lib


from operate_tools import DateTools


class TestDate(object):

    def test_get_days_date_before(self):
        days_date_before = DateTools.get_days_date_before(days=31)
        print(days_date_before)

    def test_get_days_date_after(self):
        days_date_before = DateTools.get_yesterday_date()
        print(days_date_before)

    def test_get_now_date(self):
        now_date = DateTools.get_now_date(fmt="%Y-%m-%d %H:%M:%S")
        print(now_date)

    def test_date(self):
        print(DateTools.get_week_after())
        print(DateTools.get_week_before())
        print(DateTools.get_tomorrow_date())
        print(DateTools.get_yesterday_date())
