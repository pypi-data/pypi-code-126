import re
import pathlib
import io
import http
from .base_provider import BaseProvider
from .filer import Filer

class PatternLister(Filer):
    '''
    Similar to `Filer` but instead of showing content of a directory, shows the
    prefixes added to a `Patterner`. It also provides icon urls for the
    prefixes. See `Patterner` for more details of the `Patterner` provider.
    '''
    def __init__(self, patterner, iconer=None, icons_prefix='__icons__/',
        default_format='html', exclude='__.*__', include='..*'):
      '''
      args:
      
          patterner: The `Patterner` to list its prefixes.
          iconer: Iconer which provides icons for the branches. Defaults to
          `None`.
          exclude: A regex `str` which will be matched to each prefix in
          `self.patterner`. If the prefix matches, it will not be listed.
          Defaults to `|__.*__/?` (empty prefix or any prefix that starts and
          ends with 2 underscores).
          include: A regex `str` which will be matched to each prefix in
          `self.patterner`. If the prefix does not matches, it will not be
          listed. Defaults to `.*` (any prefix).
          
      In order for a prefix to be listed and sent to the client, it must not
      match `exclude` and must match `include`. If any of them fails, the
      prefix is ignored.
      '''
      self.patterner = patterner
      self.iconer = iconer
      self.icons_prefix = icons_prefix
      self.page = type(self).PAGE
      self.default_format = default_format
      self.tfman = None
      
      self.exclude = re.compile(exclude)
      self.include = re.compile(include)
    
    def exists(self, url):
        '''
        overrides `Filer.exists()`.
        
        args:
        
            * url (path-like object): The recieved url to check.
        
        returns: True if `url` is an empty string
        '''
        return not url
    
    def is_dir(self, url):
        '''
        overrides `Filer.is_dir()`. same as `self.exists()`.
        
        args:
        
            * url (path-like object): The recieved url to check.
        
        returns: True if `url` is an empty string
        '''
        return self.exists(url)
    
    def is_file(self, url=''):
        '''
        overrides `Filer.is_file()`. always returns False
        
        args:
        
            * url (path-like object): The recieved url to check.
        
        returns: False
        '''
        return False
    
    def serve_dir_zip(self, handler, url, query, full_url):
      raise NotImplemented('Download as zip is not supported in PatternLister')
    
    def get_file_list(self, url):
        '''
        Overrides `Filer.get_file_list()` where the returned dict contains:
        
            * dirs: An empty list.
            * files: A list of patterns under `self`.
        
        args:
        
            * url (path-like object): The directory url to list its content.
        '''
        
        patterns = [
          {'name': c, 'title': self.patterner.get_title(c)}
          for c in self.patterner.get_patterns()
            if self.include.match(c) and not self.exclude.match(c)
        ]
        return {'dirs': [], 'files': patterns}
    
