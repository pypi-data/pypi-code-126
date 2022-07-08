# coding=utf-8
"""
============================
Desc:         功能描述
Author:       xiandongliang
Create Date:  2022/07/07
Pip list:     特殊依赖的第三方库说明
============================
"""
import requests


def say():
    print(requests.get('http://www.baidu.com').content.decode('utf8'))


if __name__ == '__main__':
    say()
