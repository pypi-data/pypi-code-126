import pytest
from pycalibration.mdf import MDF

__author__ = "Jerome Douay"
__copyright__ = "Jerome Douay"
__license__ = "MIT"

mdf = MDF('./tests/test.mf4')

def test_is_channel():
    assert(mdf.is_channel('EngSpeed')==True)
    assert(mdf.is_channel('aa')==False)

def test_get_channel():
    data=mdf.get_channel('EngSpeed')
    assert(data.iloc[0][0]==1093)

def test_add_channel():
    mdf.add_channel('EngSpeed')
    assert(len(mdf.channels.loc[mdf.channels['channel']=='EngSpeed'])==1)
    assert(len(mdf.channels.loc[mdf.channels['rename']=='EngSpeed'])==1)
    assert(len(mdf.channels.index)==1)
    mdf.add_channel('EngSpeed') # double insertion
    assert(len(mdf.channels.index)==1)

def test_get_data():
    data=mdf.get_data()
    assert(len(data.columns)==3)
    assert('EngSpeed' in data.columns)

# def test_get_all():
#     data=mdf.get_all()
#     assert(data.columns=={'EngSpeed'})

def test_add_channels():
    mdf.add_channels(['EngFuelRate','EngOilPress'])
    assert(len(mdf.channels.loc[mdf.channels['channel']=='EngSpeed'])==1)
    assert(len(mdf.channels.loc[mdf.channels['rename']=='EngSpeed'])==1)
    assert(len(mdf.channels.loc[mdf.channels['channel']=='EngFuelRate'])==1)
    assert(len(mdf.channels.loc[mdf.channels['rename']=='EngFuelRate'])==1)
    assert(len(mdf.channels.loc[mdf.channels['channel']=='EngOilPress'])==1)
    assert(len(mdf.channels.loc[mdf.channels['rename']=='EngOilPress'])==1)
    assert(len(mdf.channels.index)==3)
