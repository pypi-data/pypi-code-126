def Delete(path=""):
    def delete(function):
        def controller_delete_function(self):
            def delete_wrapper():
                return function(self)
            return {
                'path': path,
                'function': delete_wrapper,
                'httpMethod': 'DELETE',
                'nameFunction': function.__name__
            }
        controller_delete_function.decorators = []
        controller_delete_function.decorators.append('ACTION')
        return controller_delete_function
    return delete