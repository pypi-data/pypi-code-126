import re
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Callable,List,Any,Iterable

def asyncrun(ls:Iterable[Any], func:Callable):
    '''
    # 执行任务 
    ls: 需要处理的列表
    func: 用于处理ls中的元素的函数
    '''
    loop = asyncio.get_event_loop()
    tasks = []
    executor = ThreadPoolExecutor(25)
    for i in ls:
        futures = loop.run_in_executor(executor, func, i)
        tasks.append(futures)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

def get_m3u8_ls(m3u8file:str) -> List:
    '''
    # 获取m3u8文件url列表
    m3u8file: m3u8文件
    '''
    with open(m3u8file, 'r') as fp:
        t = fp.read()
    ls = re.findall(r"\n([^\n]+ts)\n", t)
    return ls
