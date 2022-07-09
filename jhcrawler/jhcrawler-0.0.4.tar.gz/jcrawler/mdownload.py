import re
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Callable,List,Any,Iterable
import websockets

class RpcServer:

    def __init__(self, send_ls):
        self.send_ls = send_ls

    async def check_permit(self, websocket):
        for send_text in self.send_ls:
            await websocket.send(send_text)
        return True

    async def recv_msg(self,websocket):
        while 1:
            recv_text = await websocket.recv()
            print(recv_text)

    async def main_logic(self,websocket, path):
        await self.check_permit(websocket)
        await self.recv_msg(websocket)

    def run(self, host="127.0.0.1", port=9999):
        print('listen %s:%s' % (host, port))
        start_server = websockets.serve(self.main_logic, host, port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

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