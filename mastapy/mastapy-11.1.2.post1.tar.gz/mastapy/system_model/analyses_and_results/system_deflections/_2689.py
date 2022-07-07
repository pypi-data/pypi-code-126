'''_2689.py

UnbalancedMassSystemDeflection
'''


from mastapy.system_model.part_model import _2338
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6813
from mastapy.system_model.analyses_and_results.power_flows import _4010
from mastapy.system_model.analyses_and_results.system_deflections import _2690
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'UnbalancedMassSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassSystemDeflection',)


class UnbalancedMassSystemDeflection(_2690.VirtualComponentSystemDeflection):
    '''UnbalancedMassSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _UNBALANCED_MASS_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2338.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2338.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6813.UnbalancedMassLoadCase':
        '''UnbalancedMassLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6813.UnbalancedMassLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_4010.UnbalancedMassPowerFlow':
        '''UnbalancedMassPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4010.UnbalancedMassPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
