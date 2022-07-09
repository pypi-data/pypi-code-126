def Get(path=""):
    def get(function):
        def controller_get_function(self):
            def get_wrapper():
                return function(self)
            return {
                'path': path,
                'function': get_wrapper,
                'httpMethod': 'GET',
                'nameFunction': function.__name__
            }

        controller_get_function.decorators = []
        controller_get_function.decorators.append('ACTION')
        return controller_get_function
    return get