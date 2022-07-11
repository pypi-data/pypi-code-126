'''
--------------------------------------------------------------------------
Copyright (C) 2017-2018 Lukasz Laba <lukaszlab@o2.pl>

This file is part of DxfStructure (structural engineering dxf drawing system).

DxfStructure is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

DxfStructure is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
--------------------------------------------------------------------------
'''



from strupy.pill import SectionBase, u
from dxfstructure.pycore import altname


def mass_per_length(sectname):
    #translate alternative names
    sectname = altname.translate(sectname)
    #---
    mass_per_length = SectionBase.get_sectionparameters(sectname)['mass'].asUnit(u.kg / u.m).asNumber() # in [kg / m]
    return mass_per_length

def has_section(sectname):
    #translate alternative names
    sectname = altname.translate(sectname)
    sections_in_base = SectionBase.get_database_sectionlist()
    if sectname in sections_in_base:
        return True
    else:
        return False

    
 
# Test if main
if __name__ == "__main__":
    print(mass_per_length('CAI 35x20x3,5'))
    print(mass_per_length('LN 35x20x3,5'))
    print(has_section('CAI 35x20x3,5'))
    print(has_section('LN 35x20x3,5'))
    print(has_section('CA 35x20x3,5'))
    