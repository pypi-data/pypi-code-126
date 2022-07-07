'''_3992.py

SpringDamperPowerFlow
'''


from mastapy.system_model.part_model.couplings import _2460
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6791
from mastapy.system_model.analyses_and_results.power_flows import _3924
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'SpringDamperPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperPowerFlow',)


class SpringDamperPowerFlow(_3924.CouplingPowerFlow):
    '''SpringDamperPowerFlow

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2460.SpringDamper':
        '''SpringDamper: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2460.SpringDamper)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6791.SpringDamperLoadCase':
        '''SpringDamperLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6791.SpringDamperLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None
