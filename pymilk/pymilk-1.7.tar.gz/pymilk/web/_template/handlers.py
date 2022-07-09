# 第三方模块
# from re import findall as ReFindall
# from pathlib import Path as libpath
# from json import loads as json_loads
# from json import dumps as json_dumps
from pymilk.web.handler_base import handler_base
# from pymilk.localtool import json_chinese, nowdate, nowtime
# from pymilk.dfa import dfa
# from pymilk.laydb import laydb, lc
# from pymilk.mongodb import mongo, mc, mo
# from pymilk.mysql import mysqldb
# from pymilk.mysql import mc as myc

# 本项目模块
from settings import tokenT1


# 处理器示例
class Example(handler_base):
    async def get(self):
        self.allowAnyOrigin()  # 允许跨域
        self.write('this is example-get')

    async def post(self):
        self.allowAnyOrigin()
        print(self.request.body)
        self.write('this is example-post')


# 使用token验证请求的案例
class TokenExample(handler_base):
    async def get(self):
        self.allowAnyOrigin()
        self.write('this is token_example-get')
    
    async def post(self):
        self.allowAnyOrigin()
        checkState, reason, body = tokenT1.bodyParseToken(self.request.body)
        print(checkState)
        print(reason)
        print(body)
        if checkState:
            self.write(reason)
        else:
            self.write('this is token_example-post')
