'''_1572.py

MagneticFlux
'''


from mastapy.utility.units_and_measurements import _1500
from mastapy._internal.python_net import python_net_import

_MAGNETIC_FLUX = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MagneticFlux')


__docformat__ = 'restructuredtext en'
__all__ = ('MagneticFlux',)


class MagneticFlux(_1500.MeasurementBase):
    '''MagneticFlux

    This is a mastapy class.
    '''

    TYPE = _MAGNETIC_FLUX

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MagneticFlux.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
