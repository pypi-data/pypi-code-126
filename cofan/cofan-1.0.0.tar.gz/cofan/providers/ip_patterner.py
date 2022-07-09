import http
import traceback
from .patterner import Patterner, NoMatchFoundError

class IPPatterner(Patterner):
    '''
    The same as `Patterner` but relays requests based on IP address patterns
    instead of url.
    '''
    
    def find_provider(self, addr):
        for pattern, provider in self.patterns:
            if pattern.match(addr):
                return provider, pattern
        else:
            raise NoMatchFoundError
    
    def handle_default(self, handler, *args, **kwargs):
      try:
        addr = handler.client_address[0]
        provider, pattern = self.find_provider(addr)
        
        provider_method = provider.handle_method(handler)
        return provider_method(handler, *args, **kwargs)
      except NoMatchFoundError:
        return self.short_response(http.HTTPStatus.UNAUTHORIZED)

