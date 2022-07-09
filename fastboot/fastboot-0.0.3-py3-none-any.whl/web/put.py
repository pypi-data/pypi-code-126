def Put(path=""):
    def put(function):
        def controller_put_function(self):
            def put_wrapper():
                return function(self)
            return {
                'path': path,
                'function': put_wrapper,
                'httpMethod': 'PUT',
                'nameFunction': function.__name__
            }
        controller_put_function.decorators = []
        controller_put_function.decorators.append('ACTION')
        return controller_put_function
    return put