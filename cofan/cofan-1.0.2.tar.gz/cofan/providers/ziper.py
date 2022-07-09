import pathlib
import urllib.parse
from pathlib import Path
import io
import mimetypes
import http
import zipfile
import traceback
import datetime
import json
from .filer import Filer

class Ziper(Filer):
    '''
    Same as `Filer` but serves the content of a zip file instead of
    a directory. The root in the constructor must be a zip file. Files served
    from this class are not seekable so resuming download is not possible for
    the content of a Ziper.
    '''
    
    def __init__(self, root, iconer=None, icons_prefix='__icons__/',
        default_format='html', tfman=None):
      super().__init__(root, iconer, icons_prefix, default_format, None)
    
    def handle_get(self, handler, url, query=None, body_data=None, full_url=''):
      '''
      Overrides `Filer.handle_get()`. Gives the same result as
      `Filer.handle_get()` but looks at the content of a zip file instead of
      a directory.
      '''
      
      if query is None:
        query = {}
      query.setdefault('format', [self.default_format])
      
      if url.startswith(self.icons_prefix):
        if self.iconer is not None:
          icon_url = url[len(self.icons_prefix):]
          return self.iconer.handle_get(handler, icon_url, query, full_url)
        else:
          return self.short_response(http.HTTPStatus.NOT_FOUND)
      
      with zipfile.ZipFile(self.root) as root:
        if self.is_dir(url, root):
          return self.serve_dir(handler, url, query, full_url, root)
        elif self.is_file(url, root):
          return self.serve_file(handler, url, query, full_url, root)
        else:
          return self.short_response(http.HTTPStatus.NOT_FOUND)
    
    def serve_dir(self, handler, url, query, full_url, root):
      '''
      Overrides `JFiler.serve_dir()`. Sends an html file containing
      subdirectories and files present in the requested directory in a similar
      way to file browsers. Icons are taken from `self.iconer`.
      '''
      
      path = Path(url)
      
      if self.is_file(path / 'index.html', root):
        url = (path / 'index.html').as_posix()
        response = http.HTTPStatus.TEMPORARY_REDIRECT
        headers = {
                'Location': url,
                'Content-Length': 0
            }
        f = io.BytesIO()
        return response, headers, f, lambda: None
      
      if 'download' in query:
        return self.serve_dir_zip(handler, url, query, full_url, root)
      elif query['format'][0] == 'html':
        return self.serve_dir_html(handler, url, query, full_url)
      elif query['format'][0] == 'json':
        return self.serve_dir_json(handler, url, query, full_url, root)
      else:
        return short_response(http.HTTPStatus.BAD_REQUEST)
    
    
    
    def serve_dir_json(self, handler, url, query, full_url, root):
      dir_ls = self.get_file_list(url, parent=bool(full_url), root=root)
      
      dir_ls['base_url'] = full_url[:len(full_url)-len(url)]
      dir_ls['icons_prefix'] = self.icons_prefix

      page = json.dumps(dir_ls)
      f = io.BytesIO(page.encode('utf8'))

      response = http.HTTPStatus.OK
      length = f.seek(0, 2)
      f.seek(0)
      headers = {
        'Content-Type':'application/json',
        'Content-Length': length,
      }

      return response, headers, f, lambda: None
    
    def serve_file(self, handler, url, query, full_url, root):
        '''
        Overrides `JFiler.serve_dir()`. Looks at the content of the zip file
        instead of a directory.
        
        This method has an additional optional argument:
        
            root(`zipfile.ZipFile`) Opened `self.root`. It is used in
            `self.handle_get()` to avoid opening and closing `self.root`
            multiple times. Defaults to None which means `self.root` will be
            opened and a new `zipfile.ZipFile` instance will be created.
        '''
        
        zinfo = root.getinfo(url).date_time
        mtime = datetime.datetime(*zinfo)
        ifmod = handler.headers['If-Modified-Since']
        if ifmod is not None:
            ifmod = datetime.datetime.strptime(ifmod, self.HTTP_DATE_TEMPLATE)
            if mtime <= ifmod:
                response = http.HTTPStatus.NOT_MODIFIED
                headers = {}
                f = io.BytesIO(b'')
                return response, headers, f, lambda: None
        
        mime = mimetypes.guess_type(url)[0]
        f = root.open(url)
        
        response = http.HTTPStatus.OK
        length = root.getinfo(url).file_size
        headers = {
                'Content-Length':length,
                'Last-Modified': mtime.strftime(self.HTTP_DATE_TEMPLATE),
                'Cache-Control': self.MAX_AGE
            }
        
        if mime is not None:
            headers['Content-Type'] = mime
        
        return response, headers, f, lambda: root.close()
    
    def get_file_list(self, url, parent=False, root=None):
        '''
        Overrides `Filer.get_file_list()`. Looks at the content of the zip
        file instead of a directory.
        '''
        
        if root is None:
          with zipfile.ZipFile(self.root) as root:
            return self.get_file_list(url, parent, root)
        
        dir_ls = [
          x for x in root.namelist() if
            x != url and
            x.startswith(url) and
            not x.split('/')[-1].startswith('.') and
            '/' not in x[0:-1].replace(url, '', 1)
        ]
        dirs = sorted([x.split('/')[-2] for x in dir_ls if x.endswith('/')])
        files = sorted([x.split('/')[-1] for x in dir_ls if not x.endswith('/')])
        
        return {'dirs': dirs, 'files': files}
    
    def exists(self, url, root):
        '''
        Overrides `Filer.exists()`. Looks at the content of the zip file
        instead of a directory.
        '''
        if not url:
            return pathlib.Path(self.root).exists()
        else:
            try:
                path = root.getinfo(url)
                return True
            except KeyError:
                return False
    
    def is_dir(self, url, root):
        '''
        Overrides `Filer.is_dir()`. Looks at the content of the zip file
        instead of a directory.
        '''
        if not url:
            return pathlib.Path(self.root).exists()
        else:
            try:
                path = root.getinfo(url).filename
                return not path or path.endswith('/')
            except KeyError:
                return False
        
    def is_file(self, url, root):
        '''
        Overrides `Filer.is_file()`. Looks at the content of the zip file
        instead of a directory.
        '''
        try:
            path = root.getinfo(url).filename
            return not path.endswith('/')
        except KeyError:
            return False

