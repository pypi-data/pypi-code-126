from gevent import monkey
monkey.patch_all()
from gevent import spawn
import gevent
from hyload.stats import Stats
from hyload.logger import TestLogger
from hyload.httpclient import HttpsClient,HttpClient
from time import sleep

Stats.start()

################## 你的代码写在这里  * 开始 * ###################

def client_1():    
    client = HttpClient('127.0.0.1:80', # 目标地址:端口
                            timeout=10    # 超时时间，单位秒
                           ) 
        
    while True:
        response = client.get(
            "/api/path1",
            duration=1 # 接收到响应后等待，确保本操作耗时1秒
        )

# 每隔 1秒 创建 20 个客户端     
for i in range(20):
    spawn(client_1)
    sleep(1)

################## 你的代码写在这里  * 结束 * ###################

gevent.wait()
