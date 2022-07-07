#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : aizoo.
# @File         : paddlenlp_utils
# @Time         : 2022/7/7 下午3:20
# @Author       : yuanjie
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :


from paddlenlp.taskflow.taskflow import Taskflow as _Taskflow, TASKS

# ME
from meutils.pipe import *

Taskflow = singleton(_Taskflow)


def taskflow4batch(data, batch_size=64, taskflow=Taskflow('ner'), cache=None):
    """

    @param data:
    @param batch_size:
    @param taskflow:
    @param cache: 默认硬盘缓存
    @return:
    """
    if isinstance(cache, str):
        taskflow = disk_cache(location=cache)(taskflow.__call__)

    return data | xgroup(batch_size) | xtqdm | xmap(taskflow)
