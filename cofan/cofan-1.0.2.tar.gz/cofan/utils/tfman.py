from tempfile import TemporaryDirectory
from pathlib import Path
from threading import RLock
import shutil
import time
import logging
import traceback

logger = logging.getLogger(__name__)

def precheck_parent(f):
  def check(self, name, *args, **kwargs):
    if self.check_parent(name):
      return f(self, name, *args, **kwargs)
    else:
      raise ValueError(f'{name} not in root')
  
  return check

def precheck_max_files(f):
  def check(self, *args, **kwargs):
    if not self.check_max_files():
      return f(self, *args, **kwargs)
    else:
      raise ValueError('too many files')
  
  return check

def preclean(f):
  def clean(self, *args, **kwargs):
    print('cleaning')
    for c in self.path.iterdir():
      try:
        t = time.time()
        stat = c.stat()
        t = max(stat.st_atime, stat.st_mtime)
        print(c, time.time() - t, self.timeout)
        if time.time() - t >= self.timeout:
          c.unlink()
      except Exception as e:
        logging.warning('error while cleaning {c}')
        logging.warning(traceback.format_exc())
    
    return f(self, *args, **kwargs)
  
  return clean

class TFMan:
  '''
  Temporary file manager. Used in cofan by Filer to create a temporary file for
  each partially uploaded file until the upload completes. Then moves the
  temporary file to its upload path.
  '''
  def __init__(self, max_files=10, timeout=5*60):
    self.dir = TemporaryDirectory()
    self.path = Path(self.dir.name)
    self.max_files = max_files
    self.timeout = timeout
    self.lock = RLock()
  
  def check_parent(self, name):
    path = (self.path / name).resolve()
    return path.parent == self.path
  
  def check_max_files(self):
    return len(tuple(self.path.iterdir())) >= self.max_files
  
  @preclean
  @precheck_parent
  @precheck_max_files
  def create(self, name):
    path = (self.path / name).resolve()
    print('touching', path)
    path.touch(exist_ok=False)
      
  @precheck_parent
  def write(self, name, pos, data):
    path = (self.path / name).resolve()
    if path.is_file():
      if type(data) == bytes:
        mode = 'r+b'
      else:
        mode = 'r+'
      
      with path.open(mode) as f:
        written = 0
        f.seek(pos)
        while written < len(data):
          written += f.write(data[written:])
  
  @precheck_parent
  def append(self, name, data):
    path = (self.path / name).resolve()
    if type(data) == bytes:
      mode = 'ab'
    else:
      mode = 'a'
    
    with path.open(mode) as f:
      written = 0
      while written < len(data):
        written += f.write(data[written:])
  
  @precheck_parent
  def open(self, name, *args, **kwargs):
    path = (self.path / name).resolve()
    return path.open(*args, **kwargs)
  
  @precheck_parent
  def delete(self, name, missing_ok=False):
    path = self.path / name
    path.unlink(missing_ok=missing_ok)
  
  @precheck_parent
  def copy(self, name, dest):
    path = (self.path / name).resolve()
    shutil.copyfile(path, dest)
  
  def move(self, name, dest):
    path = (self.path / name).resolve()
    shutil.move(path, dest)
  
  @precheck_parent
  def size(self, name):
    return (self.path / name).stat().st_size

