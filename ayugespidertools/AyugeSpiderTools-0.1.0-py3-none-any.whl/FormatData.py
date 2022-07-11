#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    :  format_data.py
@Time    :  2022/7/8 10:33.py
@Author  :  Ayuge
@Version :  1.0
@Contact :  ayuge.s@qq.com
@License :  (c)Copyright 2022-2023
@Desc    :  None
"""
from urllib.parse import urljoin


def get_full_url(domain_name: str, deal_url: str) -> str:
    """
    根据域名 domain_name 拼接 deal_url 来获得完整链接
    Args:
        domain_name: 域名链接
        deal_url: 需要拼接的 url

    Returns:
        full_url: 拼接完整的链接
    """
    full_url = urljoin(domain_name, deal_url)
    return full_url


def click_point_deal(decimal: float, decimal_places=2) -> float:
    """
    将小数 decimal 保留小数点后 decimal_places 位，结果四舍五入
    Args:
        decimal: 需要处理的小数
        Decimal_places: 需要保留的小数点位数

    Returns:
        decimal(float): 四舍五入后的小数点
    """
    # 先拼接需要保留的位数
    decimal_deal = "%.{}f".format(decimal_places)
    return float(decimal_deal % float(decimal))


if __name__ == '__main__':
    from loguru import  logger


    res = get_full_url(domain_name="https://static.geetest.com", deal_url="/captcha_v3/batch/v3/2021-04-27T15/word/4406ba6e71cd478aa31e0dca37601cd4.jpg")
    logger.debug(f"完整的链接 get_full_url 为: {res}")

    res = click_point_deal(13.32596516, 3)
    logger.debug(f"小数点保留 3 位后的 click_point_deal 为: {res}")

