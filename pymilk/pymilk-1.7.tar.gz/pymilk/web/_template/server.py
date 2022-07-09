# 第三方模块
from tornado.web import Application
from tornado.ioloop import IOLoop
from pymilk.web.url_parser import url_parser
# 本项目模块
import settings
from urls import routes, static_path


if static_path:
    app = Application(url_parser.parser(routes), settings.debug, static_path=static_path)
else:
    app = Application(url_parser.parser(routes), settings.debug)

app.listen(settings.port)

print(
    '',
    f'static_path: {static_path}',
    f'Debug: {settings.debug}',
    f'port: {settings.port}',
    '',
    'Start service ...',
    sep='\n'
)

IOLoop.instance().start()
