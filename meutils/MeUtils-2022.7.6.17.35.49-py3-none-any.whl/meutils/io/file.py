#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : MeUtils.
# @File         : file
# @Time         : 2022/7/5 下午3:31
# @Author       : yuanjie
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 


# 新增一行
data = 'NEW\n'
with open('untitled.txt', "r+") as f:
    old = f.read()

    f.seek(0)
    f.write(data)
    f.write(old)
