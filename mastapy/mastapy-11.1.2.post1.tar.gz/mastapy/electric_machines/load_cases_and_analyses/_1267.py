'''_1267.py

EfficiencyMapLoadCase
'''


from mastapy.electric_machines.load_cases_and_analyses import _1275
from mastapy._internal.python_net import python_net_import

_EFFICIENCY_MAP_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'EfficiencyMapLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('EfficiencyMapLoadCase',)


class EfficiencyMapLoadCase(_1275.NonLinearDQModelMultipleOperatingPointsLoadCase):
    '''EfficiencyMapLoadCase

    This is a mastapy class.
    '''

    TYPE = _EFFICIENCY_MAP_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'EfficiencyMapLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
