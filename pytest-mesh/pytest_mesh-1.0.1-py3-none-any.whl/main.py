#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
pytest_mesh 插件
完成和mesh的交互

@author:zhaojiajun
@file:main.py
@time:2022/07/13
"""
import pytest
import json
import os
from auto_doraemon.util.file_util import write_file


@pytest.mark.optionalhook
def pytest_collection_modifyitems(config, items):
    test_list = [{'module': item.location[0], 'method': item.location[2], 'path': item.nodeid,
                  'desc': item.own_markers[0].args[0]} for item in items]
    json_str = json.dumps(test_list, ensure_ascii=False, indent=4)
    # 将所有发现的的测试方法及相关信息写入到当前工程目录下的all_methods.json中
    write_file(os.getcwd(), 'all_methods.json', json_str)


if __name__ == '__main__':
    pass
