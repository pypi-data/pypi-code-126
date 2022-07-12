'''
luckylog
author: 测码课堂-范晔
Email: 1538379200@qq.com
有任何问题或者建议请联系邮箱

v 2.0.0版本：
改动：
1、部分文字错误进行了修改
2、增加了日志文件跳转，在pycharm等编辑器上可以直接点击跳转页面
3、使用log_conf代替原来分散的日志配置，使用log_conf来进行统一管理，日志类型以列表形式传入
4、logger装饰器修改形参名为passed、failed
5、logger开放参数deep，默认为1，为当前调用深度，本身为0，调用一次为1，可自行设置
6、日志书写模式不再支持键值对方式，即Logger(test='测试')的形式
7、更改debug_file配置名称为error_file更贴近文件意义
8、修改Debug变量名称为detail，区别于debugger，为显示错误日志详细信息
9、增加debug功能，对函数详细步骤进行解析

使用:
from luckylog.luckylog import *         # from luckylog.luckylog import Logger, logger, log_conf, debugger

log_conf.path = './test.log'                                    # 设置保存的日志路径
log_conf.module = ['success', 'error', 'tip', 'warning']        # 设置需要保存那些类型的日志
log_conf.error_file = './error.log'                             # 设置装饰器错误信息保存路径
log_conf.detail = False                                          # 可以设置是否开启装饰器debug模式，显示更多信息

Logger.success("123")

@logger('成功', '失败')
def test():
    print(123)

@debugger()
def test_debug(a):
    if a > 10:
        return a
    else:
        return test_debug(a + 1)
'''

import time
import sys
from functools import wraps
import threading
import platform
import os
import inspect


_func_name = ''                     # debugger用于记录主要函数名
_file_debug = ''                    # 写入debug信息的文件，装饰器启动时赋值
_debug_lock = threading.RLock()     # debugger信息写入线程锁


class _LogConf:
    def __init__(self):
        self.__conf_path = None             # 日志文件路径
        self.__conf_module = None           # 保存的日志类型
        self.__conf_error_file = None       # 错误日志保存地址
        self.__detail = False               # 是否显示详细日志信息，原Debug参数
        self.__device = platform.system()
        self.__log_deep = 2                 # 设置Logger深度
        if self.__device == 'Windows':
            os.system("")

    @property
    def path(self):
        return self.__conf_path

    @path.setter
    def path(self, set_path):
        """
        设置日志保存的路径，需要写上路径、文件名，例如：./test.log
        :param set_path: 设置的路径值
        :return:
        """
        self.__conf_path = set_path

    @property
    def module(self):
        return self.__conf_module

    @module.setter
    def module(self, set_module):
        """
        设置需要写入的日志类型，必须再设置的列表中才能启用
        :param set_module: success、warning、error、tip中选取
        :return:
        """
        origin = ['success', 'warning', 'error', 'tip']
        if all(list(map(lambda x: x in origin, set_module))):
            self.__conf_module = set_module
        else:
            raise ValueError('输入的module必须在 success, warning, error, tip 中')

    @property
    def error_file(self):
        return self.__conf_error_file

    @error_file.setter
    def error_file(self, set_val):
        """
        保存错误信息的路径和文件名，仅支持logger装饰器使用
        :param set_val: 设置的路径和文件名，例如：./myerror.log
        :return:
        """
        self.__conf_error_file = set_val

    @property
    def detail(self):
        return self.__detail

    @detail.setter
    def detail(self, set_val):
        """
        设置是否开启debug模式，debug模式会显示更多的参数信息，默认False
        :param set_val: 布尔值，默认False
        :return:
        """
        if type(set_val) is not bool:
            raise ValueError("输入的参数必须是一个布尔值")
        else:
            self.__detail = set_val

    @property
    def device(self):
        return self.__device

    @property
    def deep(self):
        return self.__log_deep

    @deep.setter
    def deep(self, set_val):
        if type(set_val) is not int:
            raise ValueError("输入的深度值必须是一个整数")
        else:
            self.__log_deep = set_val

log_conf = _LogConf()

'''定义关于日志输出的格式'''

class _LogConfig:
    def __init__(self):
        self.num = log_conf.deep

    def conf_success(self, *args) -> str:
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        def_name = sys._getframe(self.num).f_code.co_name
        line = sys._getframe(self.num).f_lineno
        file_path = sys._getframe(self.num).f_code.co_filename

        return f'(p≧w≦q) === {now_time} FILE_PATH="{file_path}:{line}" FUNC-({def_name}) <SUCCESS> LINE-{line} *MSG==√{[*args]} ==='

    def conf_erro(self, *args) -> str:
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        def_name = sys._getframe(self.num).f_code.co_name
        line = sys._getframe(self.num).f_lineno
        file_path = sys._getframe(self.num).f_code.co_filename
        return f'φ(゜▽゜*)♪ === {now_time} FILE_PATH="{file_path}:{line}" FUNC-({def_name}) <ERROR> LINE-{line} *MSG==×{[*args]} ==='

    def conf_warning(self, *args) -> str:
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        def_name = sys._getframe(self.num).f_code.co_name
        line = sys._getframe(self.num).f_lineno
        file_path = sys._getframe(self.num).f_code.co_filename
        return f'o(*￣▽￣*)ブ === {now_time} FILE_PATH="{file_path}:{line}" FUNC-({def_name}) <WARNING> LINE-{line} *MSG==!{[*args]} ==='

    def conf_normal(self, *args) -> str:
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        def_name = sys._getframe(self.num).f_code.co_name
        line = sys._getframe(self.num).f_lineno
        file_path = sys._getframe(self.num).f_code.co_filename
        return f'm（￣︶￣）↗ === {now_time} FILE_PATH="{file_path}:{line}" FUNC-({def_name}) <TIP> LINE-{line} *MSG=={[*args]} ==='


'''进行是否存入文件的方法，给文字添加颜色'''


class Logger:
    __lock = threading.RLock()

    @staticmethod
    def success(*args):
        Logger.__lock.acquire()
        print('\033[1;50;32m{}\033[0m'.format(_LogConfig().conf_success(*args)))
        if log_conf.path and ('success' in log_conf.module):
            with open(log_conf.path, 'a', encoding='utf-8') as f:
                f.writelines(_LogConfig().conf_success(*args) + '\n')
        Logger.__lock.release()

    @staticmethod
    def error(*args):
        Logger.__lock.acquire()
        print('\033[1;50;31m{}\033[0m'.format(_LogConfig().conf_erro(*args)))
        if log_conf.path and ('error' or 'erro' in log_conf.module):
            with open(log_conf.path, 'a', encoding='utf-8') as f:
                f.writelines(_LogConfig().conf_erro(*args) + '\n')
        Logger.__lock.release()

    @staticmethod
    def warning(*args):
        Logger.__lock.acquire()
        print('\033[1;50;33m{}\033[0m'.format(_LogConfig().conf_warning(*args)))
        if log_conf.path and ('warning' or 'worning' in log_conf.module):
            with open(log_conf.path, 'a', encoding='utf-8') as f:
                f.writelines(_LogConfig().conf_warning(*args) + '\n')
        Logger.__lock.release()

    @staticmethod
    def tip(*args):
        Logger.__lock.acquire()
        print('\033[1;50;34m{}\033[0m'.format(_LogConfig().conf_normal(*args)))
        if log_conf.path and ('tip' in log_conf.module):
            with open(log_conf.path, 'a', encoding='utf-8') as f:
                f.writelines(_LogConfig().conf_normal(*args) + '\n')
        Logger.__lock.release()


'''
下面是作为装饰器的方法配置
因为调用不能准确获取运行的行数，所以重新创建新的class，不继承直接另写
'''


class __Getlog:
    def success(self, now_time, file_path, def_name, line, msg, info):
        if log_conf.detail:
            msg_value = f'(p≧w≦q) === {now_time} FILE_PATH="{file_path}:{line}" FUNC-({def_name}) <SUCCESS> LINE-{line} Arguments={info} *MSG==√[{msg}]==='
        else:
            msg_value = f'(p≧w≦q) === {now_time} FILE_PATH="{file_path}:{line}" FUNC-({def_name}) <SUCCESS> LINE-{line} *MSG==√[{msg}] ==='
        print('\033[1;50;32m{}\033[0m'.format(msg_value))
        if log_conf.path and ('success' in log_conf.module):
            with open(log_conf.path, 'a', encoding='utf-8') as f:
                f.writelines(msg_value + '\n')

    def error(self, now_time, file_path, def_name, line, msg, info, error):
        if log_conf.detail:
            msg_value = f'φ(゜▽゜*)♪ === {now_time} FILE_PATH="{file_path}:{line}" FUNC-({def_name}) <ERROR> LINE-{line} Arguments={info} *MSG==×[{msg}] \n Exception:{error}===='
        else:
            msg_value = f'φ(゜▽゜*)♪ === {now_time} FILE_PATH="{file_path}:{line}" FUNC-({def_name}) <ERROR> LINE-{line} *MSG==×[{msg}] ===='
        print('\033[1;50;31m{}\033[0m'.format(msg_value))
        if log_conf.path and ('erro' or 'error' in log_conf.module):
            with open(log_conf.path, 'a', encoding='utf-8') as f:
                f.writelines(msg_value + '\n')

'''
装饰器模块：
在def上使用 @logger()，括号中可填入自定义成功失败消息，不填写则显示默认
当Debug模式为True时，成功会增加显示输入的参数，失败会增加显示参数和异常报错
使用装饰器则无需在def中使用try方法
'''


def logger(passed='Success', fail='Fail', deep=1):
    def get_logger(func):
        @wraps(func)
        def get_func(*args, **kwargs):
            def get_args(*args, **kwargs):
                save_arg = locals()
                return save_arg

            __lcok = threading.RLock()
            __lcok.acquire()
            try:
                res = func(*args, **kwargs)
                argument = get_args(*args, **kwargs)
                now_time = time.strftime('%Y-%m-%d %H:%M:%S')
                def_name = func.__name__
                line = sys._getframe(deep).f_lineno
                file_path = sys._getframe(deep).f_code.co_filename
                __Getlog().success(now_time, file_path, def_name, line, passed, argument)
                return res
            except Exception as e:
                now_time = time.strftime('%Y-%m-%d %H:%M:%S')
                def_name = func.__name__
                argument = get_args(*args, *kwargs)
                line = sys._getframe(1).f_lineno
                # line = e.__traceback__.tb_lineno
                file_path = sys._getframe(1).f_code.co_filename
                __Getlog().error(now_time, file_path, def_name, line, fail, argument, e)
                if log_conf.error_file:
                    with open(log_conf.error_file, 'a', encoding='utf-8') as d_file:
                        d_file.writelines(
                            '========{0} *FUNC_NAME=({1}) *FILE_PATH=({2})========\n*Arguments={3}\n*ERROR_INFO=({4})'.format(
                                now_time, def_name, file_path, argument, e) + '\n' + '\n')
                else:
                    pass
            __lcok.release()

        return get_func

    return get_logger

"""
以下为debug实现
"""

def _write_debug(filename, txt, lock):
    """
    将debug信息写入文件中
    :param filename: 文件路径
    :param txt: 需要写入的字符串
    :return:
    """
    lock.acquire()
    if filename is None:
        return
    with open(filename, 'a', encoding='utf-8') as f:
        f.writelines(txt + '\n')
    lock.release()

def debugger(file=None):
    """
    debug装饰器
    :param file: 需要写入的文件路径，为None则不写入
    :return:
    """
    def wrapper(func):
        global _func_name, _file_debug, _debug_lock
        _func_name = func.__name__
        if inspect.isclass(func):                           # 如果是class类型则使用不同方式获取当前代码所在模块
            file_path = inspect.getmodule(func).__file__
        else:
            file_path = func.__code__.co_filename
        _file_debug = file
        _device = platform.system()             # 获取当前设备系统
        if _device == 'Windows':
            os.system("")
        print('\n' + '=' * 50 + ' DEBUG START ' + '=' * 50)
        _write_debug(file, '\n' + '=' * 50 + ' DEBUG START ' + '=' * 50, _debug_lock)

        @wraps(func)
        def decorator(*args, **kwargs):
            print('\033[1;50;31m' + '- ' * 20 + f'开始运行: {_func_name}' + ' -' * 20 + '\033[0m')
            print('-' * 10 + f'文件 {file_path}' + '-' * 10)
            _write_debug(_file_debug, '= ' * 20 + f'开始运行: {_func_name}' + ' -' * 20 + '\n'
                         + '-' * 10 + f'文件 {file_path}' + '-' * 10, _debug_lock)
            res = None
            try:
                sys.settrace(_log_trace)
                res = func(*args, **kwargs)         # 运行函数，添加trace获取栈内数据
                sys.settrace(None)
            except Exception as e:
                print(f'\033[1;50;33m错误信息: {e}\033[0m')
                sys.settrace(None)
            sys.settrace(None)
            print('\033[1;50;31m' + '- ' * 15 + f'结束运行: {func.__name__} 返回值: \033[0m\033[1;50;34m{res}\033[0m' + '\033[1;50;31m -' * 15 + '\033[0m')
            _write_debug(_file_debug, '- ' * 15 + f'结束运行: {func.__name__} 返回值: {res}' + ' -' * 15, _debug_lock)
        return decorator
    return wrapper

def _log_trace(frame, event, arg=None):
    """
    trace回调，参数为调用时自动传入
    :param frame:
    :param event:
    :param arg:
    :return:
    """
    global _func_name, _file_debug, _debug_lock
    code = frame.f_code                         # 获取代码块
    line = frame.f_lineno                       # 获取当前所在行
    fun_name = frame.f_code.co_name             # 获取当前函数名称
    args_frame = inspect.getargvalues(frame)    # 获取里面所有的参数信息
    if fun_name != _func_name:                  # 如果获取的函数和装饰器执行前的函数名不一致则不进行后续操作
        return
    params = dict(list(args_frame)[-1])         # 获取最后的args参数值
    code_index = line - int(inspect.getsourcelines(code)[1])                # 获取代码行差异，定位相对代码行
    line_code = inspect.getsourcelines(code)[0][code_index].rstrip()        # 计算获取当前行代码
    [x if params.get(x) else params.pop(x) for x in list(params.keys())]    # 删除字典中为空值的键
    if event != 'return':                       # 如果返回的event不是return类型，则打印参数信息
        if list(params.values()) != []:
            msg = ' ' * 15 + '\033[1;50;31m' + '<' + '-'*5 + f' 运行参数: \033[0m\033[3;50;34m{params}\033[0m'
            write_msg = ' ' * 15 + '<' + '-'*5 + f' 运行参数: {params}'
        else:
            msg = ''
            write_msg = ''
    else:               # 为return时打印结束提示
        msg = ' ' * 15 + '\033[1;50;31m' + '<' + '-'*5 + ' 函数返回，结束运行\033[0m'
        write_msg = ' ' * 15 + '<' + '-'*5 + ' 函数返回，结束运行'
    print(f'\033[1;50;31mLINE {line}:\033[0m ', '\033[1;50;34m' + line_code + '\033[0m' + msg + '\n')
    _write_debug(_file_debug, f'LINE {line}: ' + line_code + write_msg + '\n', _debug_lock)
    return _log_trace
