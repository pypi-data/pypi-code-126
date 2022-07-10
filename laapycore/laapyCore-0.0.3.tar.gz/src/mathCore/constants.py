from .libs import *

i = 1j
oo = sym.oo
pi = np.pi
e = np.e


a, b, x, y, z, k, s, t = sym.symbols('a,b,x,y,z,k,s,t')

feet = 0.3048
inch = 2.54e-2

consts = {
    'c': 3.00e8,  # Speed of light
    'e': 1.6e-19,  # Elementary charge
    'me': 9.11e-31,  # Electron mass
    'mp': 1.67e-27,  # Proton mass
    'g': 6.67e-11,  # Gravitational constant
    'u0': 1.26e-6,  # Permeability constant
    'e0': 8.85e-12,  # Permittivity constant
    'k': 1.38e-23,  # Boltzmann’s constant
    'R': 8.31,  # Universal gas constant
    'o': 5.67e-8,  # Stefan–Boltzmann constant
    'h': 6.63e-34,  # Planck’s constant
    'na': 6.02e23,  # Avogadro’s number
    'a0': 5.29e-11,  # Bohr radius
    'K': 8.987e9,
}


molar_mass = 'g/mol'
molarity = 'mol/litre'
