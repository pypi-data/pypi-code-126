# Copyright (c) 2021-2022
# This file (test_tea.py) is open-source software under the
# GNU GENERAL PUBLIC LICENSE  Version 2

import os
import pytest

import numpy as np

import tea
import tea.utils as u


nlayers = 11
net_temperature = np.tile(1200.0, nlayers)
net_pressure = np.logspace(-8, 3, nlayers)
net_molecules = 'H2O CH4 CO CO2 NH3 N2 H2 HCN OH H He C N O'.split()

expected_elements_asplund = (
    'D   H   He  Li  Be  B   C   N   O   F   Ne  Na '
    'Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V '
    'Cr  Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se '
    'Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Ru  Rh  Pd '
    'Ag  Cd  In  Sn  Sb  Te  I   Xe  Cs  Ba  La '
    'Ce  Pr  Nd  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm '
    'Yb  Lu  Hf  Ta  W   Re  Os  Ir  Pt  Au  Hg '
    'Tl  Pb  Bi  Th  U').split()

expected_nonzero_dex_2009 = np.array([
    7.3 , 12.  , 10.93,  1.05,  1.38,  2.7 ,  8.43,  7.83,  8.69,
    4.56,  7.93,  6.24,  7.6 ,  6.45,  7.51,  5.41,  7.12,  5.5 ,
    6.4 ,  5.03,  6.34,  3.15,  4.95,  3.93,  5.64,  5.43,  7.5 ,
    4.99,  6.22,  4.19,  4.56,  3.04,  3.65,  3.25,  2.52,  2.87,
    2.21,  2.58,  1.46,  1.88,  1.75,  0.91,  1.57,  0.94,  0.8 ,
    2.04,  2.24,  2.18,  1.1 ,  1.58,  0.72,  1.42,  0.96,  0.52,
    1.07,  0.3 ,  1.1 ,  0.48,  0.92,  0.1 ,  0.84,  0.1 ,  0.85,
    0.85,  1.4 ,  1.38,  0.92,  0.9 ,  1.75,  0.02])

expected_nonzero_dex_2021 = np.array([
    7.3  , 12.   , 10.914,  0.96 ,  1.38 ,  2.7  ,  8.46 ,  7.83 ,
    8.69 ,  4.4  ,  8.06 ,  6.22 ,  7.55 ,  6.43 ,  7.51 ,  5.41 ,
    7.12 ,  5.31 ,  6.38 ,  5.07 ,  6.3  ,  3.14 ,  4.97 ,  3.9  ,
    5.62 ,  5.42 ,  7.46 ,  4.94 ,  6.2  ,  4.18 ,  4.56 ,  3.02 ,
    3.62 ,  3.12 ,  2.32 ,  2.83 ,  2.21 ,  2.59 ,  1.47 ,  1.88 ,
    1.75 ,  0.78 ,  1.57 ,  0.96 ,  0.8  ,  2.02 ,  2.22 ,  2.27 ,
    1.11 ,  1.58 ,  0.75 ,  1.42 ,  0.95 ,  0.52 ,  1.08 ,  0.31 ,
    1.1  ,  0.48 ,  0.93 ,  0.11 ,  0.85 ,  0.1  ,  0.85 ,  0.79 ,
    1.35 ,  0.91 ,  0.92 ,  1.95 ,  0.03 ])


def test_stoich_matrix_neutrals():
    stoich_data = [
        {'H': 2.0, 'O': 1.0},
        {'C': 1.0, 'H': 4.0},
        {'C': 1.0, 'O': 2.0},
        {'H': 2.0},
        {'H': 1.0},
        {'He': 1.0},
    ]
    expected_stoich = np.array([
        [0, 2, 0, 1],
        [1, 4, 0, 0],
        [1, 0, 0, 2],
        [0, 2, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
    ])

    elements, stoich_matrix = u.stoich_matrix(stoich_data)
    np.testing.assert_equal(elements, np.array(['C', 'H', 'He', 'O']))
    np.testing.assert_equal(stoich_matrix, expected_stoich)


def test_stoich_matrix_ions():
    stoich_data = [
        {'H': 2.0, 'O': 1.0},
        {'C': 1.0, 'H': 4.0},
        {'C': 1.0, 'O': 2.0},
        {'H': 2.0},
        {'H': 1.0, 'e': -1.0},
        {'He': 1.0},
        {'e': 1.0},
    ]
    expected_stoich = np.array([
        [ 0,  2,  0,  1,  0],
        [ 1,  4,  0,  0,  0],
        [ 1,  0,  0,  2,  0],
        [ 0,  2,  0,  0,  0],
        [ 0,  1,  0,  0, -1],
        [ 0,  0,  1,  0,  0],
        [ 0,  0,  0,  0,  1],
    ])

    elements, stoich_matrix = u.stoich_matrix(stoich_data)
    np.testing.assert_equal(elements, np.array(['C', 'H', 'He', 'O', 'e']))
    np.testing.assert_equal(stoich_matrix, expected_stoich)


@pytest.mark.parametrize('sources', ('janaf', ['janaf']))
def test_de_aliasing_janaf_only(sources):
    input_species = ['H2O', 'C2H2', 'HO2', 'CO']
    output_species = u.de_aliasing(input_species, sources)
    assert output_species == ['H2O', 'C2H2', 'HOO', 'CO']


@pytest.mark.parametrize('sources', ('cea', ['cea']))
def test_de_aliasing_cea_only(sources):
    input_species = ['H2O', 'C2H2', 'HO2', 'CO']
    output_species = u.de_aliasing(input_species, sources)
    assert output_species == ['H2O', 'C2H2,acetylene', 'HO2', 'CO']


def test_de_aliasing_janaf_cea():
    input_species = ['H2O', 'C2H2', 'HO2', 'CO']
    sources = ('janaf', 'cea')
    output_species = u.de_aliasing(input_species, sources)
    assert output_species == ['H2O', 'C2H2', 'HOO', 'CO']


def test_de_aliasing_not_found():
    input_species = ['H2O', 'C4H2', 'HO2', 'CO']
    sources = 'janaf'
    output_species = u.de_aliasing(input_species, sources)
    assert output_species == ['H2O', 'C4H2', 'HOO', 'CO']


def test_de_aliasing_default_cea():
    input_species = ['H2O', 'C4H2', 'HO2', 'CO']
    sources = ('janaf', 'cea')
    output_species = u.de_aliasing(input_species, sources)
    assert output_species == ['H2O', 'C4H2,butadiyne', 'HOO', 'CO']


def test_resolve_sources_with_missing_species():
    species = 'H2O CO (KOH)2 HO2'.split()
    sources = u.resolve_sources(species, sources=['cea'])
    assert list(sources) == ['cea', 'cea', None, 'cea']


def test_resolve_sources_cea_priority():
    species = 'H2O CO (KOH)2 HO2'.split()
    sources = u.resolve_sources(species, sources=['cea', 'janaf'])
    assert list(sources) == ['cea', 'cea', 'janaf', 'cea']


def test_resolve_sources_janaf_priority():
    species = 'H2O CO (KOH)2 HO2'.split()
    sources = u.resolve_sources(species, sources=['janaf', 'cea'])
    assert list(sources) == ['janaf', 'janaf', 'janaf', 'cea']


@pytest.mark.parametrize('sources', ('cea', ['cea']))
def test_resolve_sources_list_or_string(sources):
    species = 'H2O CO (KOH)2 HO2'.split()
    source_names = u.resolve_sources(species, sources=['cea'])
    assert list(source_names) == ['cea', 'cea', None, 'cea']


def test_read_elemental_asplund_2009():
    element_file = f'{u.ROOT}tea/data/asplund_2009_solar_abundance.dat'
    elements, dex = u.read_elemental(element_file)

    assert len(elements) == 84
    for e, ee in zip(elements, expected_elements_asplund):
        assert e == ee
    np.testing.assert_allclose(dex[dex>0], expected_nonzero_dex_2009)


def test_read_elemental_asplund_2021():
    element_file = f'{u.ROOT}tea/data/asplund_2021_solar_abundance.dat'
    elements, dex = u.read_elemental(element_file)

    assert len(elements) == 84
    for e, ee in zip(elements, expected_elements_asplund):
        assert e == ee
    np.testing.assert_allclose(dex[dex>0], expected_nonzero_dex_2021)


def test_set_element_abundance_solar():
    element_file = f'{u.ROOT}/lib/abundances.txt'
    sun_elements, sun_dex = u.read_elemental(element_file)
    elements = 'H He C N O'.split()
    e_abundances = u.set_element_abundance(
        elements, sun_elements, sun_dex)
    expected_abundance = np.array([
        1.0, 8.51138038e-02, 2.69153480e-04, 6.76082975e-05, 4.89778819e-04])
    np.testing.assert_allclose(e_abundances, expected_abundance)


def test_set_element_abundance_metallicity():
    element_file = f'{u.ROOT}/lib/abundances.txt'
    sun_elements, sun_dex = u.read_elemental(element_file)
    elements = 'H He C N O'.split()
    e_abundances = u.set_element_abundance(
        elements, sun_elements, sun_dex, metallicity=0.5)
    expected_abundance = np.array([
        1.0, 8.51138038e-02, 8.51138038e-04, 2.13796209e-04, 1.54881662e-03])
    np.testing.assert_allclose(e_abundances, expected_abundance)


def test_set_element_abundance_custom_element():
    element_file = f'{u.ROOT}/lib/abundances.txt'
    sun_elements, sun_dex = u.read_elemental(element_file)
    elements = 'H He C N O'.split()
    e_abundances = u.set_element_abundance(
        elements, sun_elements, sun_dex, e_abundances={'C': 8.8})
    expected_abundance = np.array([
        1.0, 8.51138038e-02, 6.30957344e-04, 6.76082975e-05, 4.89778819e-04])
    np.testing.assert_allclose(e_abundances, expected_abundance)


def test_set_element_abundance_custom_e_scale():
    element_file = f'{u.ROOT}/lib/abundances.txt'
    sun_elements, sun_dex = u.read_elemental(element_file)
    elements = 'H He C N O'.split()
    e_abundances = u.set_element_abundance(
        elements, sun_elements, sun_dex, e_scale={'C': np.log10(3.0)})
    expected_abundance = np.array([
        1.0, 8.51138038e-02, 8.07460441e-04, 6.76082975e-05, 4.89778819e-04])
    np.testing.assert_allclose(e_abundances, expected_abundance)


def test_set_element_abundance_custom_e_ratio():
    element_file = f'{u.ROOT}/lib/abundances.txt'
    sun_elements, sun_dex = u.read_elemental(element_file)
    elements = 'H He C N O'.split()
    e_abundances = u.set_element_abundance(
        elements, sun_elements, sun_dex, e_ratio={'C_O': 0.6})
    expected_abundance = np.array([
        1.0, 8.51138038e-02, 2.938672914e-04, 6.76082975e-05, 4.89778819e-04])
    np.testing.assert_allclose(e_abundances, expected_abundance)


def test_write_read_tea(tmpdir):
    atm_file = "atm_file.tea"
    atm = "{}/{}".format(tmpdir, atm_file)

    tea_net = tea.Tea_Network(net_pressure, net_temperature, net_molecules)
    vmr = tea_net.thermochemical_equilibrium()
    u.write_tea(atm, net_pressure, net_temperature, tea_net.species, vmr)
    assert atm_file in os.listdir(str(tmpdir))
    # Now, open file and check values:
    pressure, temperature, species, read_vmr = u.read_tea(atm)
    np.testing.assert_allclose(pressure, net_pressure, rtol=1e-6)
    np.testing.assert_allclose(temperature, net_temperature)
    np.testing.assert_equal(species, tea_net.species)
    np.testing.assert_allclose(read_vmr, vmr, rtol=1e-6)


def test_write_read_tea_tiny_abundances(tmpdir):
    atm_file = "atm_file.tea"
    atm = "{}/{}".format(tmpdir, atm_file)

    tea_net = tea.Tea_Network(net_pressure, net_temperature, net_molecules)
    vmr = tea_net.thermochemical_equilibrium()
    # Very small values change the print format:
    vmr[:,3] = 1.0e-200
    u.write_tea(atm, net_pressure, net_temperature, tea_net.species, vmr)
    assert atm_file in os.listdir(str(tmpdir))
    # Now, open file and check values:
    pressure, temperature, species, read_vmr = u.read_tea(atm)
    np.testing.assert_allclose(pressure, net_pressure, rtol=1e-6)
    np.testing.assert_allclose(temperature, net_temperature)
    np.testing.assert_equal(species, tea_net.species)
    np.testing.assert_allclose(read_vmr, vmr, rtol=1e-6)


