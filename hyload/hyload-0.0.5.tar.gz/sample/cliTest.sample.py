import time
from time import sleep
from pprint import pprint


from hyload.httpclient import HttpsClient,HttpClient

# httpbin.org  hq.sinajs.cn /list=sh601006
client = HttpsClient('api.github.com',
                       timeout=20)


response = client.sendAndRecv('GET',"/users/baiyueheiyu/repos")
print(f"响应时间为 {response.responseTime} ms")

# pprint(response.status) # 获取响应状态码
# pprint(response.getheaders()) # 获取响应所有 http 消息头 
# pprint(response.getheader('Content-Type')) # 获取指定 http消息头
# pprint(response.raw())  # 获取响应 消息体 原始字节串
# pprint(response.string())  # 获取响应 消息体 字节串解码后的字符串
pprint(response.json()) # 如果消息体是json格式 ，获取对应数据对象，如果不是json格式，返回 None
        


