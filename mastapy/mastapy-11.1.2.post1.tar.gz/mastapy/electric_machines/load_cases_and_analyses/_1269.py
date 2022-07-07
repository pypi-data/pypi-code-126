'''_1269.py

ElectricMachineFEAnalysis
'''


from mastapy.electric_machines.load_cases_and_analyses import _1278
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_FE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineFEAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineFEAnalysis',)


class ElectricMachineFEAnalysis(_1278.SingleOperatingPointAnalysis):
    '''ElectricMachineFEAnalysis

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_FE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineFEAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
