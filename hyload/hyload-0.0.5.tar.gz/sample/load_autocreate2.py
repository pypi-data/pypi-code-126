
from gevent import monkey
monkey.patch_all()

from gevent import spawn
import gevent

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
    client = HttpClient('localhost:80', # 目标地址:端口
                            timeout=10    # 超时时间，单位秒
                           ) 
    
    
    while True:
        response = client.sendAndRecv(
            'GET',
            f"/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20&wait={arg}",
            duration=1 # 接收到响应后等待，确保本操作耗时1秒
        )

    
    

clientName2Func['act-1'] = client_1


createClient(
    'act-1', # 客户端名称
    3,       # 客户端数量
    1,     # 启动间隔时间，秒
    [50,0,50])








################## write your code * end * ###################

gevent.wait()
