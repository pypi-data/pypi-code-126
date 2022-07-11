'''
--------------------------------------------------------------------------
Copyright (C) 2017-2022 Lukasz Laba <lukaszlab@o2.pl>

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

altnames = {}

#Section type CAI
#Unequal angles (x-y axis, parallel to legs)
altnames['LN '] = 'CAI '

#Section type CAE
#Equal angles (x-y axis, parallel to legs)
altnames['LR '] = 'CAE '

#Section type CARR
#Square bars

#Section type ROND
#Round bars
altnames['FI '] = 'ROND '

#Section type PLAT
altnames['BL '] = 'PLAT '
#Flat beams

#Section type TRON
#Round hollow tubes
#RO
altnames['RO '] = 'TRON '

#Section type THEX
#Hexagonal hollow tubes

#Section type TREC
#Rectangular hollow tubes
altnames['RP '] = 'TREC '

#Section type TCAR
#Square hollow tubes
altnames['RK '] = 'TCAR '

#Section type TEAI
#Structural tees

#Section type TEAE
#Structural tees

#Section type MHEB
#Structural tees cut from HEB

#Section type MHEM
#Structural tees cut from HEM

#Section type MHEA
#Structural tees cut from HEA

#Section type MIPE
#Structural tees cut from IPE


def translate (sectname):
    for name in altnames.keys():
        sectname = sectname.replace(name, altnames[name])
    return sectname

def inject_to_base_report(report):
    report = report.replace('Section type CAI', 'Section type CAI' + ' (alternate use name LN)')
    report = report.replace('Section type CAE', 'Section type CAE' + ' (alternate use name LR)')
    report = report.replace('Section type ROND', 'Section type ROND' + ' (alternate use name FI)')
    report = report.replace('Section type PLAT', 'Section type PLAT' + ' (alternate use name BL)')
    report = report.replace('Section type TRON', 'Section type TRON' + ' (alternate use name RO)')
    report = report.replace('Section type TREC', 'Section type TREC' + ' (alternate use name RP)')
    report = report.replace('Section type TCAR', 'Section type TCAR' + ' (alternate use name RK)')
    return report

# Test if main
if __name__ == "__main__":
    print(  'CAI 35x20x3,5',    translate('LN 35x20x3,5'))
    print(  'CAE 30x3',         translate('LR 30x3'))
    print(  'ROND 10',          translate('FI 10'))
    print(  'PLAT 40x4',        translate('BL 40x4'))
    print(  'TRON 26x3,2',      translate('RO 26x3,2'))
    print(  'TREC 50x25x2,5',   translate('RP 50x25x2,5'))
    print(  'TCAR 30x2,5',      translate('RK 30x2,5'))



