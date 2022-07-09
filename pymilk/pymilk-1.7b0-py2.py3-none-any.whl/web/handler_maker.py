from re import sub as ReSub
from os.path import abspath
from pathlib import Path as libpath
from .handler_base import handler_base


def fileContent_handler(file):
    class handler(handler_base):
        async def get(self):
            self.allowAnyOrigin()
            self.write(libpath(file).read_text('utf8'))
    return handler

def text_handler(text):
    class handler(handler_base):
        async def get(self):
            self.allowAnyOrigin()
            self.write(text)
    return handler


class folder_handler:
    prefix = ''

    def __init__(self, folder):
        self.folder = folder
        self.AbsFolder = abspath(folder)
        print(f"folder_handler: {self.AbsFolder}")
    
    def _make_handler(self, prefix):
        self.prefix = prefix
        class handler(handler_base):
            async def get(self_2):
                self_2.allowAnyOrigin()
                self_2.write(self._getFileContent(self_2.request))
        return handler

    def _getFileContent(self, request):
        host = request.host  # localhost:81
        full_url = request.full_url()  # http://localhost:81/static/55555/
        file = ReSub(f'^https?://{host}{self.prefix}', '', full_url)  # self.prefix: /static/
        if file:
            file = abspath(f"{self.folder}/{file}")
            if file[:len(self.AbsFolder)] == self.AbsFolder:
                file = libpath(file)
                if file.is_file():
                    return file.read_text('utf8')
        return ''
