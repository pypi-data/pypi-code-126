#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : MeUtils.
# @File         : typings
# @Time         : 2022/4/29 上午9:44
# @Author       : yuanjie
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : https://www.jb51.net/article/213917.htm

# https://blog.csdn.net/qq_21127151/article/details/104666542


from typing import *

from meutils.pipe import *
from meutils.decorators.decorator import decorator


def task():
    logger.info(f"task进程：{os.getpid()}")

    for i in range(10) | xtqdm:
        time.sleep(1)


@decorator
def fork(task, n_jobs=4, *args, **kwargs):
    """
    def task():
        logger.info(f"task进程：{os.getpid()}")

        for i in range(10) | xtqdm:
            time.sleep(1)
    fork(task)()
    """
    logger.info(f"并行数：{n_jobs}")
    logger.info(f"父进程：{os.getppid()}")

    pid = -1
    for i in range(int(n_jobs ** 0.5)):
        pid = os.fork()

    if pid < 0:
        logger.error("子进程建立失败")
    elif pid == 0:  # 在子进程中的返回值
        task(*args, **kwargs)
    else:  # 在父进程中的返回值
        task(*args, **kwargs)


if __name__ == '__main__':
    fork(task)()
