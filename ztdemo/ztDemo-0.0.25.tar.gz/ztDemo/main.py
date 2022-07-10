# -*- coding: utf-8 -*-
import functools
import os
import platform
import shutil
import time
import traceback
from collections import OrderedDict

from ztDemo.common.customize_error import RunTimeTooLong
from ztDemo.common.html_report import generate_html_report
from ztDemo.common.my_logger import MyLogger
from ztDemo.common.test_filter import TestFilter
from ztDemo.common.test_finder import DiscoverTestCases
from ztDemo.common.user_options import parse_options

from ztDemo.settings.global_config import init, set_config, get_config
from multiprocessing.pool import ThreadPool


# 定义测试运行成功、失败、错误、以及忽略的测试用例集
cases_run_success = []
cases_run_fail = []
cases_encounter_error = []
skipped_cases = []

# 初始化日志
log = MyLogger(file_name='debug_info.log')


def group_test_cases_by_class(cases_to_run):
    test_groups_dict = OrderedDict()
    for item in cases_to_run:
        tag_filter, cls, func_name, func, value = item
        test_groups_dict.setdefault(cls, []).append((tag_filter, cls, func_name, func, value))
    test_groups = [(x, y) for x, y in zip(test_groups_dict.keys(), test_groups_dict.values())]
    return test_groups


def main(user_options=None):

    start = time.time()
    # 解析用户输入
    customize_option = parse_options(user_options)

    log.debug("日志开始")
    # init global 变量
    init()

    # 设置global 变量
    set_config('config', customize_option.config)

    # 把环境变量写入配置，供测试报告调用
    set_config(get_config('config').setdefault('env', customize_option.default_env), customize_option.default_env)

    # 设置out_put_folder
    out_put_base_folder = customize_option.report_file
    if not out_put_base_folder:
        raise ValueError("Must provide output base folder")
    out_put_folder = out_put_base_folder + os.sep + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

    set_config('out_put_folder', out_put_folder)

    if os.path.exists(out_put_folder):
        shutil.rmtree(out_put_folder)
    os.makedirs(out_put_folder)

    log.debug("传入的自定义变量为{}".format(customize_option))

    # 从默认文件夹tests开始查找测试用例
    case_finder = DiscoverTestCases(customize_option.test_targets)
    # 查找测试模块并导入
    test_module = case_finder.find_test_module()
    # 查找测试用例
    original_test_cases = case_finder.find_tests(test_module)

    # 根据用户输入参数-i进一步筛选
    # 获取到要运行的测试用例，和被忽略的测试用例
    raw_test_suites, excluded_test_suites = TestFilter(original_test_cases).tag_filter_run(customize_option.include_tags_any_match)

    # 获取到最终的测试用例集，并按class名组织
    test_suites = group_test_cases_by_class(raw_test_suites)
    log.info("获取到的测试用例集为{}".format(repr(test_suites)))
    # 获取到被忽略的测试用例集，并按class名组织
    excluded_test_suites = group_test_cases_by_class(excluded_test_suites)
    log.info("忽略运行的测试用例集为{}".format(excluded_test_suites))

    # 直接解析被忽略的测试用例集，输出各项预设信息供测试报告调用
    for s in excluded_test_suites:
        func_tag, func_list = s
        for item in func_list:
            no_run_cls_group, no_run_cls, no_run_cls_name, no_run_func, value = item
            no_run_dict = dict()
            no_run_dict["testcase_id"] = getattr(no_run_cls, 'test_case_id', None)
            no_run_dict["testcase"] = no_run_cls.__name__ + '.' + no_run_func.__name__
            no_run_dict["execution_time"] = None
            no_run_dict["running_testcase_name"] = None
            no_run_dict["class_name"] = no_run_cls.__name__
            no_run_dict['module_name'] = no_run_cls.__name__
            no_run_dict['re_run'] = None
            no_run_dict['log_list'] = None
            # no_run_dict["testcase_filter_tag"] = getattr(no_run_cls, 'tag', None)
            no_run_dict["exception_type"] = None
            no_run_dict["exception_info"] = None
            no_run_dict["screenshot_list"] = []
            skipped_cases.append(no_run_dict)


    # 传入并发数目
    p = ThreadPool(customize_option.test_thread_number)
    # 使用偏函数固定住并发的数目
    # 使用map将test_suites列表中的测试用例一个个传入class_run中运行
    p.map(functools.partial(class_run, test_thread_number=customize_option.test_thread_number), test_suites)
    p.close()
    p.join()

    end = time.time()
    log.info('本次总运行时间 %s s' % (end - start))

    log.info('\nTotal %s cases were run:' % (len(cases_run_success) + len(cases_run_fail) + len(cases_encounter_error)))

    if cases_run_success:
        log.info('\033[1;32m')
        log.info('%s cases Passed, details info are:\n %s' % (
        len(cases_run_success), list(map(lambda x: x["testcase"], cases_run_success))))
        log.info('\033[0m')

    if cases_run_fail:
        log.info('%s cases Failed, details info are:\n %s' % (
        len(cases_run_fail), list(map(lambda x: x["testcase"], cases_run_fail))))
        log.error('\033[1;31m')
    if cases_encounter_error:
        log.info('%s cases Run error, details info are:\n %s' % (
        len(cases_encounter_error), list(map(lambda x: x["testcase"], cases_encounter_error))))
        log.error('\033[0m')

    if skipped_cases:
        log.info('%s cases Skipped, details info are::\n %s' % (
        len(skipped_cases), list(map(lambda x: x["testcase"], skipped_cases))))

    log.info("\n{pre_fix} Tests done {timer}, total used {c_time:.2f} seconds {pre_fix} ".format(pre_fix='---' * 10,
                                                                                                 timer=time.strftime(
                                                                                                     '%Y-%m-%d %H:%M:%S',
                                                                                                     time.localtime(
                                                                                                         end)),
                                                                                                 c_time=end - start))

    # Generate automation report
    log.info("\n{pre_fix} Starting to generate automation report... {pre_fix} ".format(pre_fix='---' * 10))
    generate_html_report(out_put_folder, cases_run_success, cases_run_fail, cases_encounter_error, skipped_cases,
                         time.time(), platform.system(), False)
    log.info("\n{pre_fix} Generate report done, please check report.html from '{report}'. {pre_fix} ".format(
        pre_fix='---' * 10, report=out_put_folder))




def class_run(case, test_thread_number):
    cls, func_pack = case
    log.debug('类 -{}- 开始运行'.format(cls.__name__))
    p = ThreadPool(test_thread_number)
    p.map(func_run, func_pack)
    p.close()
    p.join()
    log.debug('类 -{}- 结束运行'.format(cls.__name__))


# def func_run(test_case):
#     test_tag,  cls, func_name, func, value = test_case
#     if value:
#         func(func, *value)
#     else:
#         func(func)


# used to map all the test cases
def format_time(time_delta: float):
    ms = "{0:0.3f}".format(time_delta % 1000).split('.')[-1]
    seconds = "{0:0>2d}".format(int(time_delta % 60))
    minutes = "{0:0>2d}".format(int(time_delta / 60))
    hours = "{0:0>2d}".format(int(time_delta / (60 * 60)))
    return hours + "h: " + minutes + "m: " + seconds + "s: " + ms + "ms"


def func_run(test_case):
    try:
        f_c = dict()
        # 测试开始时间
        s = time.time()
        test_tag,  cls, func_name, func, value = test_case
        log.debug('类 -{cls}的方法{func}- 开始运行'.format(cls=cls.__name__, func=func_name))

        if value:
            func(func, *value)
        else:
            func(func)

        setattr(func, 'run_status', 'pass')

        # 测试结束时间
        e = time.time()
        log.debug('类 -{cls}的方法{func}- 结束运行'.format(cls=cls.__name__, func=func_name))


        # 超时运行时间，通过get_config获取
        if e - s > get_config('config')["run_time_out"]:
            raise RunTimeTooLong(func_name, e - s)
        f_c["execution_time"] = format_time(e - s)
    except RunTimeTooLong as runtime_err:
        log.error("运行时间过长错误{}".format(repr(runtime_err)))
        setattr(func, 'run_status', 'error')
        setattr(func, 'exception_type', 'RunTimeTooLong')
        setattr(func, 'error_message', repr(traceback.format_exc()))

    except AssertionError as assert_err:
        log.error("断言错误{}".format(repr(assert_err)))

        setattr(func, 'run_status', 'fail')
        setattr(func, 'exception_type', 'AssertionError')
        setattr(func, 'error_message', repr(traceback.format_exc()))
    except Exception as e:
        log.error("Exception错误{}".format(repr(e)))
        setattr(func, 'run_status', 'error')
        setattr(func, 'exception_type', 'Exception')
        setattr(func, 'error_message', repr(traceback.format_exc()))
    finally:
        if not f_c.setdefault("execution_time", None):
            # 当try语句运行出错后，重新获取测试用例结束时间
            e = time.time()
            f_c["execution_time"] = format_time(e - s)
        f_c["testcase"] = cls.__name__ + '.' + func_name
        f_c["testcase_id"] = getattr(cls, 'test_case_id', None)

        f_c["running_testcase_name"] = func_name
        f_c["class_name"] = cls.__name__
        f_c['module_name'] = func.__name__

        f_c["exception_type"] = getattr(func, 'exception_type', None)
        f_c["exception_info"] = getattr(func, 'error_message', None)
        f_c["error_message"] = getattr(func, 'error_message', None)
        f_c["re_run"] = None
        f_c["screenshot_list"] = []

        # 收集测试成功用例
        if getattr(func, 'run_status') == 'pass':
            cases_run_success.append(f_c)
        else:
            # 如果测试运行不成功，则记录日志消息
            func_log_path = os.path.join(get_config('out_put_folder'), func_name)
            if not os.path.exists(func_log_path):
                os.mkdir(func_log_path)

            func_log_file = os.path.join(func_log_path, 'first_run_log.log')
            with open(func_log_file, 'w+', encoding="utf-8") as f:
                f.writelines(repr(getattr(func, 'error_message', None)))
            f_c.setdefault('log_list', []).append('.%s%s%sfirst_run_log.log' % (os.sep, func_name, os.sep))

            # 收集断言错误的测试用例
            if getattr(func, 'run_status') == 'fail':
                cases_run_fail.append(f_c)
            elif getattr(func, "exception_type") == 'RunTimeTooLong':
                # 收集运行时发生错误的测试用例
                cases_encounter_error.append(f_c)


if __name__ == "__main__":
    main()

