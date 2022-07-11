import pint

ureg = pint.UnitRegistry()
ureg.default_system = 'SI'  # The SI unit system is used by default

g_zh = ureg('9.80665 meters/second**2')
