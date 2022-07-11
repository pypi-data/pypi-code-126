"""A Python wrapper for the c library from how-monochromatic.

    Currently supports Linux and Windows.
    View the module README at https://pypi.org/project/HowMonoPy/#description

"""

try:
    from HowMonoPy._wrapper import how_mono
except FileNotFoundError:  # If a library cannot be found the OS is unsupported
    raise ImportError("OS not supported")
