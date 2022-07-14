import pytest
from pycalibration import Extract

__author__ = "Jerome Douay"
__copyright__ = "Jerome Douay"
__license__ = "MIT"

extract =Extract()

def test_add_file():
    extract.add_file('./tests/test.mf4')
    assert(extract.files==['./tests/test.mf4'])

def test_add_directory():
    extract.files=[]
    extract.add_directory('./tests')
    assert(len(extract.files)==1)

def test_add_channel():
    extract.add_channel('EngSpeed')
    assert(len(extract.channels.loc[extract.channels['channel']=='EngSpeed'])==1)
    assert(len(extract.channels.loc[extract.channels['rename']=='EngSpeed'])==1)
    assert(len(extract.channels.index)==1)
    extract.add_channel('EngSpeed') # double insertion
    assert(len(extract.channels.index)==1)

def test_add_channels():
    extract.add_channels(['EngFuelRate','EngOilPress'])
    assert(len(extract.channels.loc[extract.channels['channel']=='EngSpeed'])==1)
    assert(len(extract.channels.loc[extract.channels['rename']=='EngSpeed'])==1)
    assert(len(extract.channels.loc[extract.channels['channel']=='EngFuelRate'])==1)
    assert(len(extract.channels.loc[extract.channels['rename']=='EngFuelRate'])==1)
    assert(len(extract.channels.loc[extract.channels['channel']=='EngOilPress'])==1)
    assert(len(extract.channels.loc[extract.channels['rename']=='EngOilPress'])==1)
    assert(len(extract.channels.index)==3)

def test_get_data():
    data=extract.get_data()
    assert(len(data.columns)==5)
    assert('EngSpeed' in data.columns)

def test_set_rename():
    extract.set_rename('EngSpeed','n')
    assert(len(extract.channels.loc[extract.channels['channel']=='EngSpeed'])==1)
    assert(len(extract.channels.loc[extract.channels['rename']=='n'])==1)
    assert(len(extract.channels.index)==3)

def test_set_renames():
    extract.set_renames(['EngFuelRate','EngOilPress'],['FuelRate','OilPress'])
    assert(len(extract.channels.loc[extract.channels['channel']=='EngSpeed'])==1)
    assert(len(extract.channels.loc[extract.channels['rename']=='n'])==1)
    assert(len(extract.channels.loc[extract.channels['channel']=='EngFuelRate'])==1)
    assert(len(extract.channels.loc[extract.channels['rename']=='FuelRate'])==1)
    assert(len(extract.channels.loc[extract.channels['channel']=='EngOilPress'])==1)
    assert(len(extract.channels.loc[extract.channels['rename']=='OilPress'])==1)
    assert(len(extract.channels.index)==3)
