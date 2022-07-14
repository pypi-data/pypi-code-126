import pytest
from pycalibration import Extract
from pycalibration import Shift

__author__ = "Jerome Douay"
__copyright__ = "Jerome Douay"
__license__ = "MIT"

extract =Extract()
extract.add_file('./tests/test.mf4')
extract.add_channels(['EngSpeed','TransShiftInProcess'])

def test_process():
    shift=Shift()
    shift.set_pre('TransShiftInProcess')
    shift.set_post('TransShiftInProcess')
    data=extract.get_data()
    shifts=shift.process(data)
    assert(len(shifts.index)!=0)
