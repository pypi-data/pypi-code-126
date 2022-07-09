import http
import time
import hmac
import urllib.parse

from .base_provider import BaseProvider

class PasswordChecker(BaseProvider):
    '''
    Prevents unauthorized requests by checking password. Made mainly to be used
    with Filer uploads. Provides basic protection and should not be considered
    safe in any means.
    '''
    def __init__(self, provider, password, max_delay=60,
        safe_methods=('GET', 'HEAD')):
      self.provider = provider
      self.password = password.encode('utf-8')
      self.max_delay = max_delay
      self.safe_methods = safe_methods
      
      self.timestamps = {}
    
    def compute_hash(self, path, t):
      msg = urllib.parse.unquote_to_bytes(path) + t.encode('utf-8')
      hasher = hmac.new(self.password, msg, 'md5')
      return hasher.hexdigest()
    
    def add_timestamp(self, addr):
      #clear too old timestamps
      now = time.time()
      for c in list(self.timestamps):
        if now - self.timestamps[c] > self.max_delay:
          self.timestamps.pop(c)
      
      if addr not in self.timestamps:
        self.timestamps[addr] = now - self.max_delay
    
    def is_allowed(self, handler):
      if handler.command in self.safe_methods:
        return True
      
      if 'Verify-Hash-T' in handler.headers:
        t = handler.headers['Verify-Hash-T']
        ft = float(t)
      else:
        ft = -1
      
      addr = handler.client_address[0]
      self.add_timestamp(addr)
      
      if self.timestamps[addr] < ft:
        self.timestamps[addr] = ft
        remote_hash = handler.headers['Verify-Hash']
        local_hash = self.compute_hash(handler.path, t)
        return hmac.compare_digest(local_hash, remote_hash)
      else:
        return False
    
    def handle_default(self, handler, *args, **kwargs):
      if self.is_allowed(handler):
        provider_method = self.provider.handle_method(handler)
        return provider_method(handler, *args, **kwargs)
      else:
        return self.short_response(http.HTTPStatus.UNAUTHORIZED)

