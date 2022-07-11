# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/9 5:32 下午
@Auth ： qiuxiaohui
@File ：sharkReport.py
@IDE ：PyCharm
"""
import datetime
import json
import os
import string
import time
import pytest

class ReplaceTepmlate(string.Template):
    delimiter = "${}"

base_dir = os.path.dirname(__file__)


test_result = {
    "start_time": 0,
    "failed": 0,
    "passed": 0,
    "skipped": 0,
    "error": 0,
    "begin_time":0,
    "total":0,
    "total_time":0,
    "tester":"",
    "case_pass_rate":0,
    "case_do_rate":[],

}

test_case_info = []
early_day = []
early_data = []
early_fail_data = []
test_case_history = []

early_pass_rate = {

}
early_fail_rate = {

}

def make_report(name, path, **kwargs):
    with open(base_dir + '/reports/' + 'sharkreport.html', 'r', encoding="utf-8") as f:
        template_html_str = f.read()


    filename = os.path.join(path, name)
    with open(filename, 'w', encoding="utf-8") as f:
        html_str = string.Template(template_html_str).substitute(kwargs)
        f.write(html_str)

def make_case_history(test_result):

    try:
        with open(os.path.join(base_dir, 'historyCaseData.json'), 'r', encoding='utf-8') as f:
            history = json.load(f)
    except :
        history = []
    history.append({'success': test_result['passed'],
                    "total": test_result['total'],
                    'fail': test_result['failed'],
                    'skip': test_result['skipped'],
                    'error': test_result['error'],
                    'runtime': test_result['total_time'],
                    'begin_time': test_result['begin_time'],
                    'begin_times': test_result['begin_times'],
                    'pass_rate': test_result['case_pass_rate'],
                    })

    with open(os.path.join(base_dir, 'historyCaseData.json'), 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=True)
    return history




def pytest_addoption(parser):
    parser.addoption(
        "--sharkreport",
        action="store",
        default="{}.html".format(datetime.datetime.now().strftime("%Y%m%d %H:%M")),
        help="Can your print report name ?"
    )
    parser.addoption(
        "--tester",
        action="store",
        default="shark",
        help="add tester"
    )

def pytest_sessionstart(session):
    start_case = datetime.datetime.now()
    test_result["start_time"] = start_case.timestamp()
    test_result["begin_time"] = start_case.strftime("%Y%m%d %H:%M")
    test_result["begin_times"] = start_case.strftime("%Y%m%d")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield

    sharkReport = out.get_result()

    if sharkReport.when == "call":

        longrepr = str(sharkReport.longrepr) if sharkReport.longrepr else ""
        logs = "\n".join(["\n".join(section) for section in sharkReport.sections]) + "\n" + longrepr  # 用例执行日志
        logs = "\n | INFO |".join(logs.split("| INFO |"))  # 换行处理


        try:
            case_info = {
                "case_class": item.location[2].split('.')[0],
                "case_func": item.location[2].split('.')[1],
                "case_state": str(sharkReport.outcome)[:6],
                "case_cost_time": str(sharkReport.duration)[:6],
                "case_desc":str(item.function.__doc__),
                "case_log":  "successed" if logs == "\n" else logs
            }
            test_case_info.append(case_info)
        except Exception as e:
            case_info = {
                "case_class": 'None',
                "case_func": item.location[2],
                "case_state": str(sharkReport.outcome)[:6],
                "case_cost_time": str(sharkReport.duration)[:6],
                "case_desc": str(item.function.__doc__),
                "case_log": logs
            }
            test_case_info.append(case_info)


def pytest_sessionfinish(session):

    test_result['tester'] = session.config.getoption("--tester")
    test_result['report_name'] = session.config.getoption("--sharkreport")




def pytest_terminal_summary(terminalreporter, exitstatus, config):

    test_result['total'] = terminalreporter._numcollected
    test_result['passed'] = len(terminalreporter.stats.get('passed', []))
    test_result['failed'] = len(terminalreporter.stats.get('failed', []))
    test_result['error'] = len(terminalreporter.stats.get('error', []))
    test_result['skipped'] = len(terminalreporter.stats.get('skipped', []))
    test_result['total_time'] = str(time.time() - terminalreporter._sessionstarttime)[:6]
    test_result['case_pass_rate'] = str(test_result['passed'] / test_result['total'] * 100)[:5]+"%"

    case_success_rate = {

        "value":str(test_result['passed'] / test_result['total'] * 100),
        "name": "成功"
    }
    case_fail_rate = {

        "value": str((test_result['failed'] + test_result['error']) / test_result['total'] * 100),
        "name": "失败"
    }

    test_result["case_do_rate"].append(case_success_rate)
    test_result["case_do_rate"].append(case_fail_rate)
    test_case_history = make_case_history(test_result=test_result)


    for i in range(7):
        today = datetime.date.today() - datetime.timedelta(days=i)
        early_day.append(today.strftime("%Y%m%d"))

    for day in sorted(early_day):
        early_pass_rate[day] = 0
        early_fail_rate[day] = 0

    for case in test_case_history:

        for i in early_day:

            if i == case["begin_times"]:

                early_pass_rate[i] += case['success']
                early_fail_rate[i] += case['fail']

    for k,v in early_pass_rate.items():
        early_data.append(v)
    for k,v in early_fail_rate.items():
        early_fail_data.append(v)

    make_report(name=test_result['report_name'],path='.',test_result=test_result,test_case_info=test_case_info,test_case_history=test_case_history,early_day=sorted(early_day),early_data=early_data,early_fail_data=early_fail_data)






