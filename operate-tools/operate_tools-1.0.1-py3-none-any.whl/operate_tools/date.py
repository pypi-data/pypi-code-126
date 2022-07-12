#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   date.py
@Time    :   2022/07/11 17:37:35
@Author  :   Desire
@Version :   1.0
@Desc    :   None
"""

import os
import sys

sys.path.insert(1, os.getcwd())
# here put the import lib

__all__ = ["DateTools"]

from datetime import datetime, timedelta


class DateTools(object):

    @staticmethod
    def get_now_date(fmt='%Y-%m-%d'):
        """获取当前日期

        Args:
            fmt (str, optional): 日期格式. Defaults to '%Y-%m-%d'.

        Returns:
            str: 格式化后的日期
        """
        now = datetime.now()
        return now.strftime(fmt)

    @staticmethod
    def get_days_date_before(days=31, fmt="%Y-%m-%d %H:%M:%S"):
        """获取前几天的日期

        Args:
            days (int, optional): 前n天. Defaults to 31.
            fmt (str, optional): 日期格式. Defaults to "%Y-%m-%d %H:%M:%S".

        Returns:
            str: 格式化后的日期
        """
        time_data = datetime.now() - timedelta(days=days)
        return time_data.strftime(fmt)

    @staticmethod
    def get_every_day_date(begin_date: str, end_date: str, fmt="%Y-%m-%d"):
        """获取开始到结束日期的每一天日期

        Args:
            begin_date (str): 开始日期
            end_date (str): 结束日期
            fmt (str): 输入的日期格式. Defaults to "%Y-%m-%d".

        Returns:
            list: 日期列表
        """
        date_list = []
        begin_date = datetime.strptime(begin_date, fmt)
        end_date = datetime.strptime(end_date, fmt)
        while begin_date <= end_date:
            date_str = begin_date.strftime(fmt)
            date_list.append(date_str)
            begin_date += timedelta(days=1)
        return date_list

    @staticmethod
    def time_difference(start_time: str, end_time: str):
        """计算时间差

        Args:
            start_time (str): 开始时间（e:2022-03-17 16:15:38）
            end_time (str): 结束时间（e:2022-03-17 16:15:40）

        Returns:
            timedelta : 时间间隔对象（e:0:00:02）
        """

        t1 = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        t2 = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        return t2 - t1
