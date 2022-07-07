'''_154.py

ElmerSimulationType
'''


from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELMER_SIMULATION_TYPE = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer', 'ElmerSimulationType')


__docformat__ = 'restructuredtext en'
__all__ = ('ElmerSimulationType',)


class ElmerSimulationType(Enum):
    '''ElmerSimulationType

    This is a mastapy class.

    Note:
        This class is an Enum.
    '''

    @classmethod
    def type_(cls):
        return _ELMER_SIMULATION_TYPE

    __hash__ = None

    STEADY_STATE = 0
    TRANSIENT = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ElmerSimulationType.__setattr__ = __enum_setattr
ElmerSimulationType.__delattr__ = __enum_delattr
