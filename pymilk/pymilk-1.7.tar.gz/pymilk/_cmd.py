import sys, os
from shutil import copytree
from shutil import copy as shutilCopy
from pathlib import Path as libpath
from .web.info import TemplatePath, SingleTemplatePath


class pymilk:
    @classmethod
    def parser(cls, words):
        if words:
            word = words[0].lower()
            if word == 'help': return cls.help()
            if word == 'web': return cls.web.parser(words[1:])
        else:
            print('''
指令集:

pymilk help | 帮助文档
pymilk web  | pymilk的web框架
''')

    @classmethod
    def help(cls):
        print('''
    一个开源的 Python 编程工具箱

    文档: https://www.yuque.com/jutooy/pymilk

    交流QQ群: 910429523
''')


    class web:
        @classmethod
        def parser(cls, words):
            if words:
                word = words[0].lower()
                if word == 'help': return cls.help()
                if word == 'mkweb': return cls.mkweb.parser(words[1:])
            else:
                print('''
指令集:

pymilk web help                | 帮助文档
pymilk web mkweb <项目名称>    | 创建新的WEB项目
    -single: 以单模块的形式创建项目
''')
        
        @classmethod
        def help(cls):
            print('''
    pymilk的web框架
            ''')


        class mkweb:
            @classmethod
            def parser(cls, words):
                if words:
                    name = words[0]
                    if '-single' in words:
                        name = f"{name}.py"
                        if libpath(name).exists():
                            raise Exception(f"文件'{name}'已存在!")
                        shutilCopy(SingleTemplatePath, name)
                    else:
                        copytree(TemplatePath, name)
                    print(f"OK! 创建项目:{name}")


def parser():
    return pymilk.parser(sys.argv[1:])
