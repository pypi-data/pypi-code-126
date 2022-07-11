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

from tabulate import tabulate
from dxfstructure.pycore import section_base

language = 'PL'

def get_available_languages():
    return ['PL', 'EN']

def set_language(newlanguage='PL'):
    global language
    if newlanguage in get_available_languages():
        language = newlanguage

def title():
    if language == 'EN':
        title =      'PARTS SCHEDULE'
    if language == 'PL':
        title =      'ZESTAWIENIE PROFILI'
    return title

def header():
    if language == 'EN':
        header_1 =      ['Element',   'Part',     'Steel',      'Section',       'Cut',       'Mass',       'Number',   'Number of',    'Total',      'Total',    'Total']
        header_2 =      [      '',     'mark',    'grade',         '',         'length',       '',          'of',        'parts',      'number',     'length',    'mass']
        header_3 =      [   '   ',    '   ',       '   ',         '   ',        '[mm]',        '[kg]',    'elements',   'in element',     '   ',       '[m]',      '[kg]']


    if language == 'PL':
        header_1 =      ['Element',  'Poz.',   'Typ',      'Profil',      'Dl.',         'Masa',       'Ilosc',   'Profili',     'Laczna',     'Laczna',   'Laczna']
        header_2 =      [      '',    'nr',   'stali',        '',       'profilu',     'profilu',      'elem.',   'w elem.',      'ilosc',      'dl.',       'masa']
        header_3 =      [   '   ',    '   ',   '   ',      '   ',       '[mm]',        '[kg]',         '   ',     '   ',        '   ',       '[m]',      '[kg]']
    return [header_1, header_2, header_3]

def breake_mark():
    return [len(header()[0]) * ['---']]

def record(profile):
    #---
    Member = profile.element.name
    #---
    Profile_mark = profile.Mark
    #---
    Steel_type = profile.Grade
    #---
    Profile_sect = profile.Sect
    if not section_base.has_section(Profile_sect):
        Profile_sect += '(!-not reconized-!)'
    #---
    Profile_length = int(profile.Length)
    #---
    Profile_mass = profile.Mass
    #---
    Number_of_members = profile.element.quantity
    #---
    Number_of_profiles_in_element = profile.Number
    #---
    Total_number = profile.Number * profile.element.quantity
    #---
    Total_length = profile.Number * profile.element.quantity * profile.Length / 1000.0
    Total_length = round(Total_length, 2)
    #---
    Total_mass = profile.Total_Mass * profile.element.quantity
    Total_mass = round(Total_mass, 2)
    #---
    record =[ Member,   Profile_mark,   Steel_type,   Profile_sect,   Profile_length,  Profile_mass, Number_of_members,  Number_of_profiles_in_element,   Total_number,  Total_length, Total_mass]
    return [record]

def summary():
    if language == 'EN':
        sumary =      'TOTAL MASS FOR DRAWING :'
    if language == 'PL':
        sumary =      'CALKOWITA MASA DLA RYSUNKU :'
    return sumary

# Test if main
if __name__ == "__main__":
    from dxfstructure.pycore.environment import*
    DRAWING.open_file()
    SCANER.load_data_to_model()
    print(tabulate(header(), numalign="right"))
    profile = STEEL_MODEL.profilelist[0]
    print(tabulate(record(profile), numalign="right"))
    print(tabulate(header() + record(profile), numalign="right"))