#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: CC
# @Time  : 2022/7/7 19:04
import time

import fire
import pymysql.cursors


def mysql_connection(host, user, password, database=None, port=3306):
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database,
                                 port=port,
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        print('数据库连接成功')


if __name__ == '__main__':
    fire.Fire(mysql_connection)