import logging
import re
import http
import traceback
from .base_provider import BaseProvider

logger = logging.getLogger(__name__)

class NoMatchFoundError(Exception):
  pass

class Patterner(BaseProvider):
    '''
    `BaseProvider` subclass that relays requests to other providers based on
    requested url pattern. The other providers are added to the `Patterner`
    instance with the request url pattern they should get. When the `Patterner`
    gets a request, it searches for a pattern that matches the beginning of the
    url. When found, the `Patterner` calls `handle_get()` method of the target
    provider, giving it the same parameters but with the prefix stripped from
    the beginning of the url.
    '''
    def __init__(self):
        self.patterns = []
        self.titles = []
    
    def add(self, pattern, provider, title=''):
        '''
        Adds a pattern and a provider to the `Patterner`.
        
        args:
        
            * pattern (str): A string containing the url prefix of the provider.
            * provider (`BaseProvider`): The provider to relay the request to.
        '''
        self.patterns.append((re.compile(pattern), provider))
        self.titles.append((pattern, title))
    
    def remove(self, pattern):
        '''
        Removes a pattern and its provider from the pattern list. If a pattern
        exists multiple times (which you should not do anyway), only the first
        occurance is removed.
        
        args:
            pattern (str): Pattern to remove.
        '''
        for c in range(len(self.patterns)):
            if self.patterns[c][0].pattern == pattern:
                self.patterns.pop(c)
        else:
            raise ValueError('pattern not found')
        
        for c in range(len(self.titles)):
            if self.titles[c][0] == pattern:
                self.patterns.pop(c)
    
    def find_provider(self, url):
        '''
        Searches the pattern list for a pattern that matches the beginning of
        the url and returns the corresponding provider and the pattern.
        '''
        for pattern, provider in self.patterns:
            if pattern.match(url):
                return provider, pattern
        else:
            raise NoMatchFoundError
    
    def handle_default(self, handler, url, *args, **kwargs):
      try:
        provider, pattern = self.find_provider(url)
        new_url = pattern.sub('', url, count=1)
        
        provider_method = provider.handle_method(handler)
        return provider_method(handler, new_url, *args, **kwargs)
      except NoMatchFoundError:
        return self.short_response(http.HTTPStatus.NOT_FOUND)
    
    def get_patterns(self):
        '''
        Returns the pattern strings added to the `Patterner`.
        '''
        patterns = []
        for c in self.patterns:
            patterns.append(c[0].pattern)
        return patterns
    
    def get_title(self, pattern):
        '''
        Returns the pattern title.
        
        args:
        
            * pattern (str): the pattern to look for its title.
        
        returns:
        
            The pattern title.
        '''
        
        for c in range(len(self.titles)):
            if self.titles[c][0] == pattern:
                return self.titles[c][1]

