from flask import Flask



class BaseController:
    instance = None
    klass = None
    path = None

    def __init__(self, app: Flask, arguments = []):
        self.app = app
        self.arguments = arguments

    def register_actions(self):
        methods_names = self.search_methods('ACTION')
        for name in methods_names:
            method = getattr(self.instance, name)
            info_method = method()
            path: str = self.path + info_method.get('path')
            id = self.klass.__name__ + '.' + info_method.get('nameFunction')
            self.app.add_url_rule(rule=path, endpoint=id,view_func=info_method.get('function'), methods=[info_method.get('httpMethod')])




    def add_controller(self):
        print(*self.arguments)
        self.instance = self.klass(*self.arguments)
        self.register_actions()




        ##self.app.add_url_rule(self)

        return self.instance

    def search_methods(self, type) -> list:
        response = []
        methods = dir(self.klass)
        for method_name in methods:
            method = getattr(self.klass, method_name)
            try:
                decorators = getattr(method, 'decorators')
                if type in decorators:
                    response.append(method_name)
            except:
                pass
        return response

def RestController(path_controller=''):

    def wrapper(klass_):
        class Controller(BaseController):
            path = path_controller
            klass = klass_
        return Controller

    return wrapper

