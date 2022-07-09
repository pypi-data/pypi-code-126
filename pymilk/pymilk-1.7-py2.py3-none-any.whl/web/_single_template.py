# from re import findall as ReFindall
# from pathlib import Path as libpath
# from json import loads as json_loads
# from json import dumps as json_dumps
from tornado.web import Application
from tornado.ioloop import IOLoop
from pymilk.web.url_parser import url_parser
from pymilk.web.info import BuiltStaticPath
from pymilk.web.handler_maker import folder_handler, fileContent_handler
from pymilk.web.handler_base import handler_base
from pymilk.web.token_tools import token_tools
# from pymilk.localtool import json_chinese, nowdate, nowtime
# from pymilk.dfa import dfa
# from pymilk.laydb import laydb, lc
# from pymilk.mongodb import mongo, mc, mo
# from pymilk.mysql import mysqldb
# from pymilk.mysql import mc as myc


debug = True
port = 81

# 根据需求自定义N个token处理器, 如无须token验证, 可全部去掉
tokenT1 = token_tools(token='123456', maxTimeDis=10, batchDis=10)
tokenT2 = token_tools(token='123456789', maxTimeDis=15, batchDis=30)


# 处理器示例
class Example(handler_base):
    async def get(self):
        self.allowAnyOrigin()  # 允许跨域
        self.write('this is example-get')
    async def post(self):
        self.allowAnyOrigin()
        body = self.request.body
        print(body)
        self.write('this is example-post')


# http://localhost:81/static/*.*
# tornado的静态文件夹功能
# 传入1个文件夹路径, 使这个文件夹里的文件全部可以通过http访问
static_path = 'static_files'


routes = {
    # http://localhost:81/built-static/*.*
    # folder_handler: 和static_path类似, 由于static_path只能指定1个文件夹, 因此开发出folder_handler来补充
    # BuiltStaticPath: 包预置的静态文件夹, 内含常用的JS函数和CSS样式
    'built-static': folder_handler(BuiltStaticPath),
    'static-files': folder_handler('static_files'),  # http://localhost:81/static-files/*.*
    'example': Example,  # http://localhost:81/example
    'bcd/': {
        'b': Example,  # http://localhost:81/bcd/b
        'c': Example,  # http://localhost:81/bcd/c
    },
    'bcd/d':  Example,  # http://localhost:81/bcd/d
}


# Start service
if static_path:
    app = Application(url_parser.parser(routes), debug, static_path=static_path)
else:
    app = Application(url_parser.parser(routes), debug)
app.listen(port)
print(
    '',
    f'Debug: {debug}',
    f'port: {port}',
    f'static_path: {static_path}',
    '',
    'Start service ...',
    sep='\n'
)
IOLoop.instance().start()
