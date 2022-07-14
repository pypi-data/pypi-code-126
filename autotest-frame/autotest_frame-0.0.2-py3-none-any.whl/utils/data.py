# -*- coding:utf-8 -*-
import random
import time


def get_current_time() -> tuple:
    """获取当前时间，文件名后可使用-如：20220519111454"""
    time_stamp = time.strftime("%Y%m%d%H%M%S")
    """获取当前时间，如：2022-05-19 11:15:15"""
    time_format = time.strftime("%Y-%m-%d %H:%M:%S")
    return time_stamp, time_format


def get_timestamp(n=None) -> str:
    """生成n位数的时间戳"""
    timestamp = str(time.time()).replace('.', '')[:n]  # 把小数点去掉，并取13位数
    # timestamp = timestamp.ljust(n, '6')  # n位数，左对齐，不足n位右边补6
    return timestamp


def get_phone() -> str:
    """通过时间戳生成手机号"""
    # 移动手机号前几位
    cm = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
    # 联通手机号前几位
    cu = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
    # 手机号前几位
    ct = [133, 153, 180, 181, 189, 177, 1700]
    phone = str(random.choice(cm + cu + ct)) + get_timestamp()
    phone = phone[:11]
    return phone


def get_time_interval(function_name, n=None) -> str:
    """获取某个功能运行时间，如：function_name()；n为小数点后位数"""
    time_a = time.time()
    function_name()
    time_b = time.time()
    interval = time_b - time_a
    interval_integer = str(interval).split('.')[0]
    interval_mantissa = str(interval).split('.')[1][:n]
    return interval_integer + '.' + interval_mantissa



