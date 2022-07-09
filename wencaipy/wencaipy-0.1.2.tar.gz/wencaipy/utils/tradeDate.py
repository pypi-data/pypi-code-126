#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
交易日历处理
"""
import os
import datetime
from typing import Union, List
import numpy
import pandas as pd
import requests
from sqlalchemy import false
from wencaipy.common.wcParameter import  TRADE_TIMES

rest_days_df = None
chinese_holidays_range = None


def today():
    return datetime.date.today()


def date2str(cursor_date):
    """
    explanation:
        对输入日期进行格式化处理，返回格式为 "%Y-%m-%d" 格式字符串
        支持格式包括:
        1. str: "%Y%m%d" "%Y%m%d%H%M%S", "%Y%m%d %H:%M:%S",
                "%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H%M%S"
        2. datetime.datetime
        3. pd.Timestamp
        4. int -> 自动在右边加 0 然后转换，譬如 '20190302093' --> "2019-03-02"
    params:
        * cursor_date->
            含义: 输入日期
            类型: str
            参数支持: []
    """
    if isinstance(cursor_date, datetime.datetime):
        cursor_date = str(cursor_date)[:10]
    elif isinstance(cursor_date, numpy.datetime64):
        cursor_date = str(cursor_date)[:10]
    elif isinstance(cursor_date, str):
        try:
            cursor_date = str(pd.Timestamp(cursor_date))[:10]
        except:
            raise ValueError('请输入正确的日期格式, 建议 "%Y-%m-%d"')
    elif isinstance(cursor_date, int):
        cursor_date = str(pd.Timestamp("{:<014d}".format(cursor_date)))[:10]
    else:
        raise ValueError('请输入正确的日期格式，建议 "%Y-%m-%d"')
    return cursor_date


def _init_chinese_rest_days(headers=None):
    global rest_days_df, chinese_holidays_range
    if rest_days_df is None:
        url = os.getenv("TQ_CHINESE_HOLIDAY_URL", "https://files.shinnytech.com/shinny_chinese_holiday.json")
        rsp = requests.get(url, timeout=30, headers=headers)
        chinese_holidays = rsp.json()
        _first_day = datetime.date(int(chinese_holidays[0].split('-')[0]), 1, 1)  # 首个日期所在年份的第一天
        _last_day = datetime.date(int(chinese_holidays[-1].split('-')[0]), 12, 31)  # 截止日期所在年份的最后一天
        chinese_holidays_range = (_first_day, _last_day)
        rest_days_df = pd.DataFrame(data={'date': pd.Series(pd.to_datetime(chinese_holidays, format='%Y-%m-%d'))})
        rest_days_df['trading_restdays'] = False  # 节假日为 False
    return chinese_holidays_range


def get_trading_calendar(start_dt=None, end_dt=None, headers=None):
    """
    获取一段时间内，每天是否是交易日
    :return: DataFrame
        date  trading
    2019-12-05  True
    2019-12-06  True
    2019-12-09  True
    """
    _init_chinese_rest_days(headers=headers)
    df = pd.DataFrame()
    df['date'] = pd.Series(pd.date_range(start=start_dt, end=end_dt, freq="D"))
    df['trading'] = df['date'].dt.dayofweek.lt(5)
    result = pd.merge(rest_days_df, df, sort=True, how="right", on="date")
    result.fillna(True, inplace=True)
    df['trading'] = result['trading'] & result['trading_restdays']
    return df


def trade_date_sse(start_dt='1990-01-01', end_dt='2030-12-31'):
    if not end_dt:
        end_dt = today()
    #print(type(end_dt))
    df = get_trading_calendar(start_dt, end_dt)
    td = df[df.trading == True]["date"].values
    td = list(map(lambda x: date2str(x), td))
    return td

trade_date_cn = trade_date_sse() 


def get_last_tradedate():
    _now =  datetime.datetime.now()
    _hour = _now.hour
    _date = _now.strftime('%Y-%m-%d')
    #print(_now, _hour, _date)
    if  _date in trade_date_cn:
        if _hour > 17:
            return trade_date_cn[trade_date_cn.index(_date)]
        else:
            return trade_date_cn[trade_date_cn.index(_date) - 1]
    while _date not in trade_date_cn:
        _date = pd.to_datetime(str(_date)) + pd.Timedelta(days=-1)
        _date = _date.strftime('%Y-%m-%d')
    #print(_date) 
    #print(trade_date_sse[trade_date_sse.index(_date)])
    return trade_date_cn[trade_date_sse.index(_date)]


def if_trade_date(date):
    if str(date) in trade_date_sse():
        return True
    else:
        return False


def if_traded_now():
    """
    '日期是否交易 and time > 9:30'
    """
    _now = datetime.datetime.now()
    _now_time =  str(datetime.datetime.strptime(str(_now)[0:19],  "%Y-%m-%d %H:%M:%S"))[11:]
    if (today() in trade_date_cn) and (str(_now_time) >  TRADE_TIMES().TRADE_TIME_AM[0]):
        return True
    else:
        return False


def if_trade_datetime(_time=datetime.datetime.now()):
    """  时间是否交易 """
    _time = datetime.datetime.strptime(str(_time)[0:19], "%Y-%m-%d %H:%M:%S")
    if if_trade_date(str(_time.date())[0:10]):
        if _time.hour in [10, 13, 14]:
            return True
        elif (
           _time.hour in [9] and _time.minute >= 15
            ):
            return True
        elif _time.hour in [11] and _time.minute <= 30:
            return True
        else:
                return False
    else:
        return False


def get_real_trade_date(date, trade_list=trade_date_cn, towards=-1):
    """
    explanation:
        获取真实的交易日期
    params:
        * date->
            含义: 日期
            类型: date
            参数支持: []
        * trade_list->
            含义: 交易列表
            类型: List
            参数支持: []
        * towards->
            含义: 方向， 1 -> 向前, -1 -> 向后
            类型: int
            参数支持: [1， -1]
    """
    date = str(date)[0:10]
    if towards == 1:
        if pd.Timestamp(date) >= pd.Timestamp(trade_list[-1]):
            return trade_list[-1]
        while date not in trade_list:
            date = str(
                datetime.datetime.strptime(str(date)[0:10], "%Y-%m-%d")
                + datetime.timedelta(days=1)
            )[0:10]
        else:
            return str(date)[0:10]
    elif towards == -1:
        if pd.Timestamp(date) <= pd.Timestamp(trade_list[0]):
            return trade_list[0]
        while date not in trade_list:
            date = str(
                datetime.datetime.strptime(str(date)[0:10], "%Y-%m-%d")
                - datetime.timedelta(days=1)
            )[0:10]
        else:
            return str(date)[0:10]


if __name__ == "__main__":
    print(today())
    #end_dt = str(datetime.now().date())
    #df = get_trading_calendar("2022-01-01",end_dt)
    #print(df)
    #tradedate = trade_date_sse(start_dt='2022-07-01', end_dt=end_dt)
    #print(type(tradedate))
    #print(tradedate)
    #print(trade_date_sse()[:5])
    #print(datetime.datetime.now())
    #print(datetime.time(9,25,0))
    #print(type(trade_date_cn[-1]))
    #print(trade_date_cn[-1])
 
    print(if_traded_now())
    print(if_trade_date("2022-07-08"))
    print(if_trade_datetime())
    
    print(get_real_trade_date("2022-07-08"))
    
    
    
    
   
    
    
    
 
   