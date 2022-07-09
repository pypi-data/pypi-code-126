import http
from .base_provider import BaseProvider

class Statuser(BaseProvider):
    '''
    A subclass of `BaseProvider`. This provider is very similar to BaseProvider.
    The only difference is that it takes the response code in its constructor
    and sends this response code instead of OK.
    '''
    def __init__(self, response=http.HTTPStatus.NOT_FOUND):
      '''
      args:
      
        * response (http.HTTPStatus): The response code to send when
          `handle_default()` is called. It defaults to NOT_FOUND.
      '''
      self.response = response
    def handle_default(self, handler, url, query=None, body_data=None,
        full_url=''):
      return self.short_response(self.response)

