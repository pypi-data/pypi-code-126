#
# (c) 2022 Giorgio Gonnella, University of Goettingen, Germany
#
import pytest
from pathlib import Path

@pytest.fixture
def a_file_in():
  def _a_file_in(dirname, notin=[]):
    filenames = [f.name for f in Path(dirname).glob("*") if f.is_file()]
    for dirname in notin:
      for fn in filenames:
        if Path(dirname).joinpath(fn).exists():
          filenames.remove(fn)
    if filenames:
      return filenames[0]
    else:
      return None
  return _a_file_in
