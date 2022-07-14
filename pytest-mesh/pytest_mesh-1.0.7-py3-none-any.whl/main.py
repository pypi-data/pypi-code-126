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
import logging
from auto_doraemon.util.file_util import write_file, read_file
from auto_doraemon.util.time_util import get_current_time

log = logging.getLogger(__name__)

global test_summary  # 测试结果概要信息
global test_methods  # 需要执行的测试方法list


def get_test_methods(file_path: str):
    """
    根据file_path中内容找到所有需要测试的方法
    :param file_path:
    :return:
    """
    content = read_file(file_path)
    content_json = json.loads(content)
    path_list = []
    for tmp in content_json:
        path_list.append(tmp['path'])
    return path_list


@pytest.mark.optionalhook
def pytest_addoption(parser, pluginmanager):
    """
    给pytest 增加自定义参数
    :param parser:
    :param pluginmanager:
    :return:
    """
    parser.addoption("--file", action="store",
                     default="None",
                     help="将自定义命令行参数 ’--file' 添加到 pytest 配置中")
    parser.addoption("--lane", action="store",
                     default='main',
                     help="将自定义命令行参数 ’--lane' 添加到 pytest 配置中")
    parser.addoption("--notify", action="store",
                     default=0,
                     help="将自定义命令行参数 ’--notify' 添加到 pytest 配置中")


@pytest.mark.optionalhook
def pytest_cmdline_preparse(config, args):
    """
    遍历--file 对应的文件，提取出需要执行的测试方法
    :param config:
    :param args:
    :return:
    """
    for index, value in enumerate(args):
        if '--file' in value:
            path = value.split('=')[1]
            global test_methods
            test_methods = get_test_methods(path)
            break


@pytest.mark.optionalhook
def pytest_collection_finish(session):
    """
    过滤收集测试item,只保留指定需要进行测试的方法
    :param session:
    :return:
    """
    global test_methods
    new_items = []
    for item in session.items:
        if item.nodeid in test_methods:
            new_items.append(item)
    session.items = new_items


@pytest.mark.optionalhook
def pytest_collection_modifyitems(config, items):
    test_list = [{'module': item.location[0], 'method': item.location[2], 'path': item.nodeid,
                  'desc': item.own_markers[0].args[0]} for item in items]
    json_str = json.dumps(test_list, ensure_ascii=False, indent=4)
    # 将所有发现的的测试方法及相关信息写入到当前工程目录下的all_methods.json中
    write_file(os.getcwd(), 'all_methods.json', json_str)


@pytest.mark.optionalhook
def pytest_sessionstart(session):
    """
    测试流程的会话启动
    :param session: 测试会话
    :return:
    """
    log.info('{} session start'.format(session.name))
    global test_summary
    test_summary = {
        'start_time': get_current_time("%Y-%m-%d %H:%M:%S")
    }


@pytest.mark.optionalhook
def pytest_sessionfinish(session, exitstatus):
    """
    测试流程的会话结束
    :param session:
    :param exitstatus:
    :return:
    """
    log.info('{} session finish'.format(session.name))
    # 生成测试概要数据文件
    global test_summary
    terminal_reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    stats_keys = terminal_reporter.stats.keys()
    test_summary['testcase_pass'] = len(terminal_reporter.stats.get('passed')) if 'passed' in stats_keys else 0
    test_summary['testcase_fail'] = len(terminal_reporter.stats.get('failed')) if 'failed' in stats_keys else 0
    test_summary['testcase_skip'] = len(terminal_reporter.stats.get('skipped')) if 'skipped' in stats_keys else 0
    test_summary['end_time'] = get_current_time("%Y-%m-%d %H:%M:%S")
    test_summary['total_test_case'] = session.testscollected
    write_file(os.getcwd(), 'test_summary.json', json.dumps(test_summary, indent=4))


@pytest.mark.optionalhook
def pytest_runtest_setup(item):
    log.info('test method {} setup'.format(item.name))


@pytest.mark.optionalhook
def pytest_runtest_call(item):
    log.info('test method {} call to run'.format(item.name))


@pytest.mark.optionalhook
def pytest_runtest_teardown(item):
    log.info('test method {} teardown'.format(item.name))


if __name__ == '__main__':
    pass
