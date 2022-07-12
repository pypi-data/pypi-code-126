
from gevent import monkey
monkey.patch_all()

from gevent import spawn
import gevent

from pprint import pprint
from time import sleep

from hyload.stats import Stats
from hyload.httpclient import HttpsClient,HttpClient

clientName2Func = {}

# 如果 args 有值，一定是列表，元素依次赋值给每次clientfunc调用
def createClient(clientName, clientNum, interval, args=None):
    clientFunc = clientName2Func[clientName]
    for i in range(clientNum):
        if args:
            spawn(clientFunc, args[i])
        else:
            spawn(clientFunc)

        if i < clientNum - 1:
            sleep(interval)

Stats.start()

################## write your code  * begin * ###################



def client_1(arg=None):
    
    # 创建客户端     
    client = HttpClient('127.0.0.1',    # 目标地址:端口
                            timeout=10    # 超时时间，单位秒
                           ) 
    
    
    while True:
        response = client.sendAndRecv(
            'GET',
            "/api/path1"
        )
    
    

clientName2Func['client-1'] = client_1

# 定义性能场景，点击右边条目，可自动插入代码

createClient(
    'client-1', # 客户端名称
    3,       # 客户端数量
    0.1,     # 启动间隔时间，秒
    )








################## write your code * end * ###################

gevent.wait()
