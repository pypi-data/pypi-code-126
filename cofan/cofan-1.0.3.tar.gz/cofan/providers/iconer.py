import pathlib
import io
import mimetypes
import http
from .ziper import Ziper

class Iconer(Ziper):
    '''
    Same as `Ziper` but used to serve file icons used in `Filer` and `Ziper`.
    Defines methods to help other objects find icon urls for files of different
    types. The root of `Iconer` is a zip file which contains image files in its
    toplevel. The name of each image file should be in the form `<name>.<ext>`
    where `<ext>` can be any extension and <name> can be any of the following:
    
        * The string `directory`. It makes the image used as the icon for
          directories.
        * A file extension. It makes the image used for file of this extension.
        * General mimetype (such as audio, video, text, ...). It makes the image
          used for this mimetype if the file extension image does not exist.
        * The string `generic`. It makes the image used as a fallback icon if
          none of the above was found.
    
    Any file without extension in `self.root` is ignored.
    '''
    
    def __init__(self, root=None, theme='humanity'):
        '''
        Overrides `Ziper.__init__()`. Does not take `iconer` argument
        and always uses `self` as its `self.iconer`.
        
        args:
        
            * root (path-like object): Similar to `Ziper` constructor. If
              `None` is given the `Iconer` finds its root based on `theme`
              argument. Defaults to `None`.
            * theme (str): Ignored if `root` is not `None`. If `root` is `None`,
              looks for the root in
              `<module path>/asset/themes/<theme name>.zip` where
              `<module path>` is the path of cofan library and <theme name>
              is the value given in this argument.
            * prefix: The root url of the `Iconer` added to the `Paterner`
              class. For example, if the iconer root url is `foo_bar/`, the
              string `foo_bar` must be given in this argument and also added
              to the `Patterner` object that will relay requests to this
              `Iconer`. Defaults to `__icons__/`.
        '''
        if root is None:
            root = str(pathlib.Path(__file__).parent / 'asset' / 'themes' / '{}.zip'.format(theme))
        
        super().__init__(root, iconer=self)
        self.icon_index = self.get_icons()
    
    def handle_get(self, handler, url, query=None, full_url=''):
      ext = url.casefold()
      mime = mimetypes.guess_type('a.{}'.format(url))[0]
      if mime is not None:
        mime = mime.split('/')[0]
      
      if ext in self.icon_index:
        url = self.icon_index[ext]
      elif mime is not None and mime in self.icon_index:
        url = self.icon_index[mime]
      elif 'generic' in self.icon_index:
        url = self.icon_index['generic']
      else:
        return self.short_response(http.HTTPStatus.NOT_FOUND)
      
      return super().handle_get(handler, url, query, full_url)
    
    def get_icons(self):
        '''
        Used in `self.__init__()`. Looks at the toplevel content of `self.root`
        for any files and makes a dictionary for each file. The keys of the
        dictionary are file names without extensions and the values are the file
        names with extensions. Any files without extension are ignored. The
        dictionary is used to look for icons without opening the zip file.
        '''
        icon_index = {}
        dir_ls = self.get_file_list('')
        for c in dir_ls['files']:
            name_ext = c.rsplit('.', 1)
            if len(name_ext) > 1:
                icon_index[name_ext[0]] = c
        
        return icon_index
    
    def get_icon(self, name):
        '''
        This method is to be used in other content providers to get icons.
        Returns the url of an icon for `name`. The icon is constructed in the
        following way:
        
            * The extension is extracted from `name`. If `name` has no
              extension, the full value of `name` is taken.
            * If there is a file in `self.root` named as the extension of `name`
              extracted in the previous step, the url of this file is
              returned. For example, if `name` is `foo.mp4`, this method will
              look for a file named `mp4.<extension>` where `<extension>` may
              be any string. The extension is case insensitive so `foo.mp4`
              will be the same as `foo.MP4`.
            * If there is no file found in the previous step, the mimetype is
              guessed and the general type is taken (such as audio,
              video, etc...).
            * If there is a file in `self.root` with the same name as the
              generel mimetype extracted in the previous step, the url of this
              file is returned. For example, if `name` is `foo.mp4`, this
              method will look for a file named `mp4.<anything>` first. If it
              there is no such file in `self.root`, the method will look for
              `video.<anything>`. `<anything>` may be any string.
            * If there is no file found in the previous step, this method looks
              for a file named `generic.<anything>` and the url of this file
              is returned.
            * If there is no file found in the previous step, an empty string
              is returned.
        '''
        ext = name.rsplit('.', 1)[-1].casefold()
        mime = mimetypes.guess_type(name)[0]
        if mime is not None:
            mime = mime.split('/')[0]
        if ext in self.icon_index:
            return (pathlib.Path(
                '/' + self.prefix) / self.icon_index[ext]).as_posix()
        elif mime is not None and mime in self.icon_index:
            return (pathlib.Path(
                '/' + self.prefix) / self.icon_index[mime]).as_posix()
        elif 'generic' in self.icon_index:
            return (pathlib.Path(
                '/' + self.prefix) / self.icon_index['generic']).as_posix()
        else:
            return ''

