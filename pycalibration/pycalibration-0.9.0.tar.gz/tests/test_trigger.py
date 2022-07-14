import pytest
from pycalibration import Extract
from pycalibration import Trigger

__author__ = "Jerome Douay"
__copyright__ = "Jerome Douay"
__license__ = "MIT"

extract =Extract()
extract.add_file('./tests/test.mf4')
extract.add_channels(['EngSpeed','TransShiftInProcess'])

def test_set_trigger():
    trigger=Trigger()
    trigger.set_trigger('TransShiftInProcess')
    assert(trigger.trigger=='TransShiftInProcess')

def test_process():
    trigger=Trigger()
    trigger.set_trigger('TransShiftInProcess')
    data=extract.get_data()
    assert(len(data.index)!=0)
