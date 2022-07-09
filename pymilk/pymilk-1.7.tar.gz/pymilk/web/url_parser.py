from re import sub as ReSub
from .handler_maker import folder_handler


class url_parser:

    @classmethod
    def _parserBase(cls, dic):
        for k, v in dic.items():
            if type(v) is dict:
                for k2, v2 in cls._parserBase(v):
                    yield k + k2, v2
            else:
                yield k, v
    
    @classmethod
    def parser(cls, dic):
        routes = {}
        for k, v in cls._parserBase(dic):
            if type(v) is folder_handler:
                k = ReSub('^/*', '/', k)
                k = ReSub('[/?]*$', '/', k)
                routes[k + '.+'] = v._make_handler(prefix=k)
            else:
                k = ReSub('^/*', '/', k)
                k = ReSub('[/?]*$', '/?', k)
                routes[k] = v
        for x in list(routes):
            if x[:8] == '/static/':  # tornado的静态文件前缀
                routes.pop(x, None)
        return list(routes.items())
