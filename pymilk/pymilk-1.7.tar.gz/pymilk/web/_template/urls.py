# 第三方模块
from pymilk.web.info import BuiltStaticPath
from pymilk.web.handler_maker import folder_handler, fileContent_handler
# 本项目模块
import handlers


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

    '': fileContent_handler('static_files/index.html'), # http://localhost:81/

    'example': handlers.Example,  # http://localhost:81/example
    'token_example': handlers.TokenExample,  # http://localhost:81/token_example

    'bcd/': {
        'b': handlers.Example,  # http://localhost:81/bcd/b
        'c': handlers.Example,  # http://localhost:81/bcd/c
    },

    'bcd/d':  handlers.Example,  # http://localhost:81/bcd/d
}
