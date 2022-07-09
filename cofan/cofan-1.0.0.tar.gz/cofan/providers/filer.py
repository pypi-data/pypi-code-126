import logging
from pathlib import Path
import io
import os
import mimetypes
import http
import json
import traceback
import datetime
import zipfile
from base64 import b16encode
import threading

from .base_provider import BaseProvider

logger = logging.getLogger(__name__)

class Filer(BaseProvider):
    '''
    Lists directory contents and serves files from local file system based on
    the recieved url.
    
    Allows uploading files to this directory.
    
    For file uploads, consider using a TPChecker to prevent unauthorized
    uploads.
    '''
    
    HTTP_DATE_TEMPLATE = '%a, %d %b %Y %H:%M:%S GMT'
    MAX_AGE = 'max-age={}'.format(60)
    CHUNK_SIZE = 4 * 2**10
    PAGE = Path(__file__).parent / 'asset' / 'filer_main.html'
    
    def __init__(self, root, iconer=None, icons_prefix='__icons__/',
        default_format='html', tfman=None):
      '''
      args:
      
        * root (path-like object): Root directory or file to serve. Any
          requested url will be served starting from this directory.
        * iconer (Iconer): An instance of `Iconer` which will be used for the
          directories and files icons. Defaults to None which will display
          no icons.
        * icons_prefix (str): The prefix to be used for icons root url. Defaults
          to `__icons__/`.
        * default_format (str): can be the string `html` or `json`. This tells
          whether to serve the filer as an html page or as a json file.
        * tfman (TFMan): An instance of `cofan.utils.TFMan`. The temporary file
          manager to manage uploaded files until they are fully uploaded. If
          `None`, disables file uploads. Defaults to `None`.
      '''
      
      self.root = str(Path(root).resolve())
      self.iconer = iconer
      self.icons_prefix = icons_prefix
      self.page = type(self).PAGE
      self.default_format = default_format
      self.tfman = tfman
    
    def handle_get(self, handler, url, query=None, body_data=None,
        full_url=''):
      '''
        Serves files and directories. If `url` points to a file, the file is
        sent in the response. If `url` points to a directory, its content is
        sent as an html page if `query['format']` is the string `html` or as
        a JSON file if `query['format']` is the string `json`.
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
      elif self.is_dir(url):
        return self.serve_dir(handler, url, query, full_url)
      elif self.is_file(url):
        return self.serve_file(handler, url, query, full_url)
      else:
        return self.short_response(http.HTTPStatus.NOT_FOUND)
    
    def serve_dir(self, handler, url, query, full_url):
      '''
      Overrides `JFiler.serve_dir()`. Sends an html file containing
      subdirectories and files present in the requested directory in a similar
      way to file browsers. Icons are taken from `self.iconer`.
      '''
      
      path = Path(url)
      
      if self.is_file(path / 'index.html'):
        url = (path / 'index.html').as_posix()
        response = http.HTTPStatus.TEMPORARY_REDIRECT
        headers = {
                'Location': url,
                'Content-Length': 0
            }
        f = io.BytesIO()
        return response, headers, f, lambda: None
      
      if 'download' in query:
        return self.serve_dir_zip(handler, url, query, full_url)
      elif query['format'][0] == 'html':
        return self.serve_dir_html(handler, url, query, full_url)
      elif query['format'][0] == 'json':
        return self.serve_dir_json(handler, url, query, full_url)
      else:
        return short_response(http.HTTPStatus.BAD_REQUEST)
    
    def serve_dir_zip(self, handler, url, query, full_url):
      path = Path(self.root) / url
      rfd, wfd = os.pipe()
      rpipe, wpipe = open(rfd, 'rb'), open(wfd, 'wb')
      
      response = http.HTTPStatus.OK
      headers = {
        'Content-Type':'application/zip',
      }
      
      threading.Thread(target=self.zip_dir, args=(path, wpipe)).start()
      
      return response, headers, rpipe, lambda: None
    
    def serve_dir_html(self, handler, url, query, full_url):
      f = self.page.open('rb')
      
      response = http.HTTPStatus.OK
      length = f.seek(0, 2)
      f.seek(0)
      headers = {
        'Content-Type':'text/html',
        'Content-Length': length,
      }
      return response, headers, f, lambda: None
    
    def serve_dir_json(self, handler, url, query, full_url):
      dir_ls = self.get_file_list(url)
      dir_ls['base_url'] = full_url[:len(full_url)-len(url)]
      dir_ls['icons_prefix'] = self.icons_prefix
      
      if self.tfman is not None:
        dir_ls['upload-allowed'] = ''
      
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
    
    def serve_file(self, handler, url, query, full_url):
      path = Path(self.root) / url
      mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime)
      ifmod = handler.headers['If-Modified-Since']
      if ifmod is not None:
        ifmod = datetime.datetime.strptime(ifmod, self.HTTP_DATE_TEMPLATE)
        if mtime <= ifmod:
          response = http.HTTPStatus.NOT_MODIFIED
          headers = {'Content-Length': 0}
          f = io.BytesIO(b'')
          return response, headers, f, lambda: None
      
      mime = mimetypes.guess_type(url)[0]
      f = path.open('br')
      
      response = http.HTTPStatus.OK
      length = f.seek(0, 2)
      f.seek(0)
      headers = {
        'Content-Length': length,
        'Last-Modified': mtime.strftime(self.HTTP_DATE_TEMPLATE),
        'Cache-Control': self.MAX_AGE,
      }
      if mime is not None:
        headers['Content-Type'] = mime
      
      return response, headers, f, lambda: None
    
    def handle_put(self, handler, url,
        query=None, body_data=None, full_url=''):
      
      if self.tfman is None:
        return self.short_response(http.HTTPStatus.BAD_REQUEST)
      
      tmp_name = b16encode(full_url.encode('utf8')).decode('ascii')
      
      if (
            handler.headers['Content-Length'] is None or
            int(handler.headers['Content-Length']) <= 0
          ):
        self.tfman.delete(tmp_name, True)
        
        response = http.HTTPStatus.OK
        f = io.BytesIO(b'')
        headers = {
          'Content-Length': 0,
        }
        
        return response, headers, f, lambda: None
      
      total_length = int(handler.headers['Content-Total-Length'])
      offset = int(handler.headers['Content-Offset'])
      length = int(handler.headers['Content-Length'])
      
      if offset == 0:
        self.tfman.create(tmp_name)
      
      with self.tfman.open(tmp_name, 'ab') as f:
        read_size = 0
        data = handler.rfile.read1(self.CHUNK_SIZE)
        read_size += len(data)
        f.write(data)
        while read_size < length:
          data = handler.rfile.read1(self.CHUNK_SIZE)
          read_size += len(data)
          f.write(data)
      
      if offset + length == total_length:
        self.save_file(tmp_name, url)
      
      response = http.HTTPStatus.OK
      f = io.BytesIO(b'')
      headers = {
        'Content-Length': 0,
      }
      
      return response, headers, f, lambda: None
    
    def save_file(self, fname, path):
      root_path = Path(self.root)
      new_file_path = root_path / path
      parent = new_file_path.parent.resolve()
      
      if parent.is_relative_to(root_path):
        self.tfman.move(fname, new_file_path)
      else:
        raise RuntimeError('tried to upload file outside my root dir')
    
    def exists(self, url):
        '''
        Returns `True` if the url points to an existing file or directory under
        `self.root`. Otherwise returns `False`.
        
        args:
        
            * url (path-like object): The recieved url to check.
        
        returns: True if `url` is an existing file or subdirectory in
            `self.root`. False otherwise.
        '''
        try:
            root = Path(self.root)
            path = root / url
            path = path.resolve()
            if path.samefile(self.root) or root in path.parents:
                return path.exists()
        except FileNotFoundError:
            pass
        
        return False
    
    def is_dir(self, url):
        '''
        Returns `True` if the url points to an existing directory under
        `self.root`. Otherwise returns `False`.
        
        args:
        
            * url (path-like object): The recieved url to check.
        
        return: True if `url` is an existing subdirectory of `self.root`. False
            otherwise.
        '''
        return self.exists(url) and (Path(self.root) / url).is_dir()
    
    def is_file(self, url):
        '''
        Returns `True` if the url points to an existing file under `self.root`.
        Otherwise returns `False`.
        
        args:
        
            * url (path-like object): The recieved url to check.
        
        returns: True if `url` is an existing file in `self.root` or one of its
            subdirectories. False otherwise.
        '''
        return self.exists(url) and (Path(self.root) / url).is_file()
    
    def get_file_list(self, url):
        '''
        Called by `self.handle_get`. Returns a dictionary containing 2
        members:
        
            * dirs: A list of directories under the directory pointed by url.
            * files: A list of files under the directory pointed by url.
        
        args:
        
            * url (path-like object): The directory url to list its content.
        '''
        if self.is_dir(url):
            path = Path(self.root) / url
            dir_ls = [x for x in path.glob('*') if not x.name.startswith('.')]
            
            dirs = sorted([x.name for x in dir_ls if x.is_dir()])
            files = sorted([x.name for x in dir_ls if x.is_file()])
            return {'dirs': dirs, 'files': files}
        else:
            raise ValueError('url is not pointing to a directory')
    
    def zip_dir(self, path, dest):
      try:
        with zipfile.ZipFile(dest, 'w') as f:
          for item in path.glob('**/*'):
            if item.is_file():
              f.write(item, str(item.relative_to(path)))
      finally:
        dest.close()

