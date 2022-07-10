'''
:Date: 2022-07-10
:Version: 1.0.3
:Authors:
    * Mohammad Alghafli <thebsom@gmail.com>

cofan is an http server library for serving files and any other things. You use
it to share content in the form of a website. The current classes give you the
following:
    
  * Serve the content of a local directory in a form similar to file browser
    with icons for directories and files based on their extension.
  * Serve the content of a local zip file the same way as the local
    directories.
  * Serve local html files as a web site.
  * Upload to existing directory.
  * Organize your urls in prefix trees.
  * Response differently for different ip addresses

It also supports requests of partial files to resume previously interrupted
download.

Here is an example of how to use it::
    
  from cofan import *
  
  #allows uploads
  from cofan.utils.tfman import TFMan
  import pathlib
  
  #our site will be like this:
  # /           (this is our root. will list all the branches below)
  # |
  # |- vid/
  # |  this branch is a file browser for videos
  # |
  # -- site/
  #    this will be a web site. just a collection of html files
  
  #lets make an http file browser and share our videos
  #first, we specify the icons used in the file browser
  #you can omit the theme. it defaults to `humanity`
  icons = Iconer(theme='humanity')
  
  #now we create a Filer and specify the path we want to serve
  vid = Filer(pathlib.Path.home() / 'Videos', iconer=icons, tfman=TFMan())
  
  #we also want to serve a web site. lets create another filer. since the root
  #directory of the site contains `index.html` file, the filer
  #will automatically redirect to it instead of showing a file browser
  #no file browser also means we do not need to specify `iconer`
  #parameter. you can still use it if you want but that would not be very
  #useful
  site = Filer(pathlib.Path.home() / 'mysite')
  
  #now we need to give prefixes to our branches
  #we create a patterner
  patterns = Patterner()
  
  #then we add the filers with their prefixes
  #make sure to add a trailing slash
  patterns.add('vid/', vid)
  patterns.add('site/', site)
  
  #now we have all branches. but what if the user types our root url?
  #the path we will get will be an empty string which is not a prefix of any
  #branch. that will be a 404
  #lets make the root list and other branches added to `patterns`
  #the branches will be shown like the file browser but now the icons will be
  #for the patterns instead of file extensions
  #we need to specify where the icons are taken from
  #the icons file should contain an icon named `vid.<ext>` and an icon named
  #`site.<ext>` where <ext> can be any extension.
  root = PatternLister(patterns, root=pathlib.Path.home() / 'icons.zip')
  
  #and we add our root to the patterns with empty prefix
  patterns.add('', root)
  
  #now we create our handler like in http.server. we give it our patterner
  handler = BaseHandler(patterns)
  
  #and create our server like in http.server
  srv = Server(('localhost', 8000), handler)
  
  #and serve forever
  srv.serve_forever()
  
  #now try to open your browser on http://localhost:8000/

This module can also be run as a main python script to serve files from a
directory.

commandline syntax::

    python -m cofan.py [-a <addr>] [-u] [-nu] [<root>]

options:

    * -a <addr>, --addr <addr>: specify the address and port to bind to. <addr>
      should be in the form `<ip>:<port>` where `<ip>` is the ip address and
      `<port>` is the tcp port. defaults to `localhost:8000`.
    * -u, --upload: allow uploads. defaults to False.
    * -nu, --no-upload: opposite -u option. disallow uploads. this is selected
      by default.

args:

    * root: The root directory to serve. Defaults to the current directory.
'''

import logging
import traceback
import re
import urllib.parse
import http
import http.server
import socketserver
from cgi import parse_header
import multipart
from .providers import *

try:
    from fileslice import Slicer
except ImportError:
    Slicer = None

__version__ = '1.0.0'

logger = logging.getLogger(__name__)

class BaseHandler(http.server.BaseHTTPRequestHandler):
    '''
    Base http handler class in cofan library. You give it a provider instance
    and gets the response of all requests from it. For example::
        
      myprovider = Filer('/path/to/my/directory')
      myhandler = BaseHandler(myprovider)
      srv = http.server.HTTPServer(('localhost', 80), myhandler)
        
    `BaseHandler` has 2 class attributes:
    
      * __header_modifiers__: A tuple of request headers which have modifier
        methods in this class. For each header present in a request,
        `self.mod_<header>()` is called where <header> is the header name. The
        modifier method must return the response, headers and content after
        any necessary modification. It must take the following arguments:
      
          * response: Last response status code after any previous
            modifications by other modifier mehtods.
          * headers: Last headers after any previous modifications by other
            modifier mehtods.
          * content: Last content file after any previous modifications by
            other modifier mehtods.
      
        This tuple currently has only one header: `Range`. See
        `self.mod_Range()` for the modification applied.
      * TIMEOUT: Connection timeout for each request connection.
    
    This class is probably good for most uses without creating a subclass. In
    case you want to subclass it, you may want to override `self.get_response()`
    or `self.default_response()`.
    '''
    
    
    TIMEOUT = 10
    __header_modifiers__ = ('Range',)
    
    def __init__(self, provider, max_size=2**30):
        '''
        args:
        
            provider: The provider to get content from.
            max_size: the maximum size for multipart/form-data body.
        '''
        
        self.provider = provider
        self.max_size = max_size
    
    def do_default(self):
      '''
      default request method handler. called when no do_* method is available
      for the method of the incoming request.
      '''
      
      handler = self.response_method
      
      self.request.settimeout(self.TIMEOUT)
      try:
        response, headers, content, postproc = handler()
      except NotImplementedError:
        response, headers, content, postproc = BaseProvider.short_response(
          http.HTTPStatus.NOT_IMPLEMENTED)
      except:
        traceback.print_exc()
        response, headers, content, postproc = BaseProvider.short_response(
          http.HTTPStatus.INTERNAL_SERVER_ERROR)
      
      try:
          self.send_response(response)
          for c in headers:
              self.send_header(c, headers[c])
          self.end_headers()
          data = content.read(1024)
          while data:
              self.wfile.write(data)
              data = content.read(1024)
          self.request.settimeout(None)
      finally:
          content.close()
          postproc()
    
    def do_GET(self):
        '''
        Calls `BaseProvider.handle_get()` from `self.provider` and sends the
        returned response, headers and content. After this process is done,
        the content file is closed and the returned post processing fucntion is
        called. This happens regardless of whether the process ended with
        success or not.
        '''
        
        self.request.settimeout(self.TIMEOUT)
        try:
          response, headers, content, postproc = self.get_response()
        except NotImplementedError:
          response, headers, content, postproc = BaseProvider.short_response(
            http.HTTPStatus.NOT_IMPLEMENTED)
        except:
          traceback.print_exc()
          response, headers, content, postproc = BaseProvider.short_response(
            http.HTTPStatus.INTERNAL_SERVER_ERROR)
        
        try:
            self.send_response(response)
            for c in headers:
                self.send_header(c, headers[c])
            self.end_headers()
            data = content.read(1024)
            while data:
                self.wfile.write(data)
                data = content.read(1024)
            self.request.settimeout(None)
        finally:
            content.close()
            postproc()
    
    def do_HEAD(self):
        '''
        Same as `self.do_GET()` but does not send any content.
        '''
        
        self.request.settimeout(self.TIMEOUT)
        try:
          response, headers, content, postproc = self.get_response()
        except NotImplementedError:
          response, headers, content, postproc = BaseProvider.short_response(
            http.HTTPStatus.NOT_IMPLEMENTED)
        except:
          traceback.print_exc()
          response, headers, content, postproc = BaseProvider.short_response(
            http.HTTPStatus.INTERNAL_SERVER_ERROR)
        
        try:
            self.send_response(response)
            for c in headers:
                self.send_header(c, headers[c])
            self.end_headers()
            self.request.settimeout(None)
        finally:
            content.close()
            postproc()
    
    def default_response(self):
        '''
        Same as `BaseProvider.get_response()` but calls
        `self.provider.handle_post()` instead of `self.provider.handle_get()`.
        It also does not modify headers (e.g. if there is Range request header,
        it does not respond with 204 but keep the response code and content
        without change.
        '''
        
        provider_method = self.provider.handle_method(self)
        
        body_data = None
        if self.headers['Content-Type'] is not None:
          content_type, pdict = parse_header(self.headers['Content-Type'])
          if content_type == 'multipart/form-data':
            body_data = self.parse_form()
        
        url = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(url.path)[1:]
        query = urllib.parse.parse_qs(url.query)
        return provider_method(self, path, query, body_data, path)
    
    def parse_form(self):
      length = int(self.headers['Content-Length'])
      if length > self.max_size:
        raise ValueError(
          'body size ({}) is greater than max size ({})'.format(
            length, self.max_size
          )
        )
          
      body_data = {}
      
      def on_field(f):
        body_data.setdefault(
          f.field_name.decode('utf8'), []).append(f.value.decode('utf8'))
      def on_file(f):
        new_file = {}
        new_file['data'] = f.file_object
        new_file['name'] = f.file_name.decode('utf8')
        ext = new_file['name'].rsplit('.', 1)[-1]
        new_file['ext'] = ext
        new_file['data'].seek(0)
        body_data.setdefault(f.field_name.decode('utf8'), []).append(new_file)
      
      multipart.parse_form(self.headers, self.rfile, on_field, on_file)
      return body_data
    
    def get_response(self):
        '''
        Called by `self.do_GET()` and `self.do_HEAD()`. Parses the url  path and
        query string and replaces all url escapes. After that, it gets the
        response `self.provider.handle_get()`. Before returning the response,
        headers, content file and post processing callables, it calls any
        modifier method that should be called. If the method fails while
        applying modifications, it closes the content file and calls the post
        processing callable before propagating the exception.
        '''
        
        url = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(url.path)[1:]
        query = urllib.parse.parse_qs(url.query)
        
        provider_method = self.provider.handle_method(self)
        
        response, headers, content, postproc = provider_method(
          self, path, query, full_url=path)
        
        try:
            response_group = int(str(response.value)[0])
            if response_group != 3 and response_group != 4 and response_group != 5:
                for c in self.__header_modifiers__:
                    if c in self.headers:
                        response, headers, content = getattr(self, 'mod_{}'.format(c))(response, headers, content)
        except:
            content.close()
            postproc()
            raise
        
        return response, headers, content, postproc
    
    def mod_Range(self, response, headers, content):
        '''
        Called when the `Range` header is present in the request. If the
        response status code is 200 (OK) and the content file is seekable, the
        status code is changed to 206 (Partial Content) and the content file is
        changed to a partial file pointing to the requested range.
        Response status code is changed to 416 (Requested Range Not Satisfiable)
        if the range start is not between 0 and total size or if the range end
        is not between start and total size.
        '''
        
        if (response == http.HTTPStatus.OK and content.seekable() and
                Slicer is not None):
            rng = self.headers['Range'].split('=')
            if rng[0] == 'bytes':
                rng = rng[1].split('-')
                if rng[0]:
                    start = int(rng[0])
                    if rng[1]:
                        end = int(rng[1])
                    else:
                        end = content.seek(0, 2) - 1
                else:
                    start = content.seek(0, 2) - int(rng[1])
                    end = content.seek(0, 2) - 1
            else:
                raise RuntimeError('invalid range')
            
            total_size = content.seek(0, 2)
            length = end - start + 1
            
            valid_start = 0 <= start < total_size
            valid_end = start <= end < total_size
            
            if valid_start and valid_end:
                rng = 'bytes {}-{}/{}'.format(start, end, total_size)
                
                headers['Content-Range'] = rng
                headers['Content-Length'] = length
                
                response = http.HTTPStatus.PARTIAL_CONTENT
            else:
                rng = 'bytes */{}'.format(total_size)
                
                headers['Content-Range'] = rng
                headers['Content-Length'] = length
                
                response = http.HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE
            
            content = Slicer(content)(start, length)
        
        return response, headers, content
    
    def __getattr__(self, name):
      if name.startswith('do_'):
        return self.do_default
      else:
        getattr(super(), name)
    
    def __call__(self, *args, **kwargs):
        '''
        Creates and returns another instance of the same type as `self` with
        the same provider. Any arguments and keyword arguments are passed to the
        constructor of the base class of `self`.
        '''
        
        handler = type(self)(self.provider)
        super(type(handler), handler).__init__(*args, **kwargs)
        return handler
    
    @property
    def response_method(self):
      method = f'{self.command.lower()}_response'
      if not hasattr(self, method):
        method = 'default_response'
      return getattr(self, method)

class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    '''
    same as `http.server.HTTPServer` but handles requests in daemon threads.
    '''
    
    daemon_threads = True

