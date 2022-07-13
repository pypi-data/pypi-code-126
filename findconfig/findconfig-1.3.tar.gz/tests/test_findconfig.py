#
# (c) 2022 Giorgio Gonnella, University of Goettingen, Germany
#

import pytest
from findconfig import findconfig
from pathlib import Path
from xdg import xdg_config_home, xdg_config_dirs
import warnings

def test_findconfig_xdg_config_home(a_file_in):
  filename = a_file_in(xdg_config_home())
  if filename is None:
    warnings.warn("No file is XDG config home directory found, test skipped")
    return
  assert findconfig(filename) == Path(xdg_config_home()) / filename

def test_findconfig_xdg_config_dirs(a_file_in):
  xcd = xdg_config_dirs()
  if not xcd:
    warnings.warn("No XDG config dirs found, test skipped")
    return
  filename = a_file_in(xcd[0], notin=[xdg_config_home()])
  if filename is None:
    warnings.warn("No file is XDG config dirs found, test skipped")
    return
  assert findconfig(filename) == Path(xcd[0]) / filename

def test_findconfig_home(a_file_in):
  filename = a_file_in(Path.home(), notin=[xdg_config_home()]+xdg_config_dirs())
  if filename is None:
    warnings.warn("No file is home directory found, test skipped")
    return
  assert findconfig(filename) == Path.home() / filename

def test_findconfig_src(a_file_in):
  import findconfig_caller.call
  assert findconfig_caller.call.find(0) == \
      Path(__file__).parent / "findconfig_testfile_0"
  assert findconfig_caller.call.find(1) == \
      Path(__file__).parent / "findconfig_caller" / "findconfig_testfile_1"
  assert findconfig_caller.call.find(2) == None
  import findconfig_caller.level2.call
  assert findconfig_caller.level2.call.find(0) == \
      Path(__file__).parent / "findconfig_testfile_0"
  assert findconfig_caller.level2.call.find(1) == \
      Path(__file__).parent / "findconfig_caller" / "findconfig_testfile_1"
  assert findconfig_caller.level2.call.find(2) == \
      Path(__file__).parent / "findconfig_caller" / "level2" / \
        "findconfig_testfile_2"

def test_findconfig_more_paths():
  custompath = Path(__file__).parent / "custom"
  findconfig("find", more_paths=[custompath]) == custompath / \
    "findconfig_testfile_C"

def test_findconfig_src_climb():
  import custompath.level2.call
  assert custompath.level2.call.find(0, 2) == \
      Path(__file__).parent / "findconfig_testfile_0"
  assert custompath.level2.call.find(0, 1) == None
  assert custompath.level2.call.find("C", 1) == \
      Path(__file__).parent / "custompath" / "findconfig_testfile_C"
  assert custompath.level2.call.find("C", 0) == None
  import custompath.level2.level3.call
  assert custompath.level2.level3.call.find("C", 1) == \
      Path(__file__).parent / "custompath" / "findconfig_testfile_C"
  assert custompath.level2.level3.call.find("C", 0) == None
  assert custompath.level2.level3.call.find(0, 2) == \
      Path(__file__).parent / "findconfig_testfile_0"
  assert custompath.level2.level3.call.find(0, 1) == None

def test_findconfig_allowdot():
  assert findconfig("findconfig_testfile_hidden") == \
      Path(__file__).parent / ".findconfig_testfile_hidden"
  assert findconfig("findconfig_testfile_hidden", allow_dot = False) == None

def test_exception():
  assert findconfig("findconfig_testfile_not_existing") == None
  with pytest.raises(FileNotFoundError):
    findconfig("findconfig_testfile_not_existing", exception = True)
