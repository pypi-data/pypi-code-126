def Post(path=""):
    def post(function):
        def controller_post_function(self):
            def post_wrapper():
                return function(self)
            return {
                'path': path,
                'function': post_wrapper,
                'httpMethod': 'POST',
                'nameFunction': function.__name__
            }
        controller_post_function.decorators = []
        controller_post_function.decorators.append('ACTION')

        return controller_post_function
    return post