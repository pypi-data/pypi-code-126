import pathlib
from .. import providers
from ..providers.patterner import Patterner
from importlib.util import spec_from_file_location, module_from_spec
import sys

def tree_patterner(path, env=None):
  '''
  creates url prefixes for the directory tree under path. each prefix is handled
  by the provider returned from the provider.py file in the directory.
  '''
  if env is None:
    env = {}
  
  path = pathlib.Path(path)
  patterner = Patterner()
  env.update({'self': patterner, 'providers': providers})
  
  for c in reversed(list(path.glob('**/provider.py'))):
    prefix = str(c.parent.relative_to(path)).strip('.') + '/'
    if prefix == '/':
      prefix = ''
    
    spec = spec_from_file_location('', c)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    provider = module.provider(env)
    if provider is not None:
      print('adding', prefix, provider)
      patterner.add(prefix, provider)
  
  return patterner

