from tornado.web import RequestHandler


class handler_base(RequestHandler):

    # 允许跨域, 必须开启才能进行Ajax异步请求
    def allowAnyOrigin(self):
        self.set_header("Access-Control-Allow-Origin", "*")
