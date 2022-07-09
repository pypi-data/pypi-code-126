import io
import http

class BaseProvider:
    '''
    basic provider class. each time a request is intended to this provider,
    the provider should return a response code, headers and body. it defines one
    method:
        
      * short_response(): helper method to send a response code and its
        description.
    
    You should override methods that respond to http requests you want to
    handle. A handler for an http request with method <method> has to be
    handle_<method>(). E.g. handle_get() for GET requests, handle_put() for
    PUT requests, and so on. A default handler is handle_default() which
    handles any request that does not have a handler defined.
    
    All handler methods take the same arguments and should return the same
    values. refer to handle_default() documentation below for arguments.
    
    You probably want to use one of `BaseProvider` subclasses or inherit it in
    your own class.
    '''
    
    @classmethod
    def handle_default(handler, url,
        query=None, body_data=None, full_url=''):
      '''
      Handles all incoming requests that do not have a defined handler method.
      Default implementation raises NotImplementedError.
      
      args:
      
        * handler (http.server.BaseHTTPRequestHandler): The object that called
          this method.
        * url (str): The url that was requested after removing all prefixes by
          other providers. Look at Patterner for information of how prefixes are
          stripped.
        * query (dict): Request query arguments. Defaults to empty dictionary.
          full_url (str): The full url that was requested without removing
          prefixes.
        * body_data: the request body. `BaseHandler` implementation
          supplies this argument as a `dict` only if the request is
          multipart/form-data. Otherwise, `BaseHandler` passes an empty dict.

        returns:
        
            * response (http.HTTPStatus): Response code.
            * headers (dict): Response headers.
            * content (binary file-like object): The response content.
            * postproc (callable): A callable that will be called after serving
              the content. This callable will be called as long as this handler
              method succeded regardless whether sending the content to the
              client succeded or not. The intention of this callable is to close
              all files other than content in case there are open files. For
              example, if content is a file inside a zip file, closing content
              is not enough without closing the parent zip file.
      '''
      
      raise NotImplementedError
    
    @staticmethod
    def short_response(response=http.HTTPStatus.OK, body=None):
        '''
        Convinience method which can be used to send a status code and its
        description. It returns the same values as `handle_get` but the code is
        specified as a parameter and the body defaults to a description of the
        code.
              
        args:
        
          * response (http.HTTPStatus): Response code to send. Defaults to
            `http.HTTPStatus.OK`.
          * body: The value to send in the body. It defaults to `None` which
            sends a short description of the code. If the body is not a bytes
            object, it is converted to a string and then encoded to utf8.
        
        returns:
        
          * response (http.HTTPStatus): Response code given in the args.
          * headers (dict): Response headers dict with `text/html` in
            `Content-Type` header and the length of the body in
            `Content-Length` header.
          * content (binary file-like object): Description of `response` as a
            utf-8 encoded string if `body` arg is `None`. Otherwise, returns
            `body` represented as utf-8 encoded string.
          * postproc: Always a value of `None`.
        '''
        
        if body is None:
            body = '{} {}'.format(response.value, response.name.replace('_', ' ')).encode('utf8')
        elif type(body) is not bytes:
            body = str(body).encode('utf8')
        
        f = io.BytesIO(body)
        length = f.seek(0, 2)
        f.seek(0)
        headers = {
                'Content-Type':'text/html',
                'Content-Length': length,
            }
        return response, headers, f, lambda: None
    
    def handle_method(self, handler):
      '''
      returns the handler for the incoming request based on the request method.
      e.g. returns `self.handle_get()` for GET request, `self.handle_put()`
      method for PUT request, and so on. if no handler for the request method is
      defined, returns `self.handle_default()`.
      '''
      method = f'handle_{handler.command.lower()}'
      if not hasattr(self, method):
        method = 'handle_default'
      return getattr(self, method)
      

