'''_2684.py

TorqueConverterPumpSystemDeflection
'''


from mastapy.system_model.part_model.couplings import _2468
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6807
from mastapy.system_model.analyses_and_results.power_flows import _4008
from mastapy.system_model.analyses_and_results.system_deflections import _2585
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'TorqueConverterPumpSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpSystemDeflection',)


class TorqueConverterPumpSystemDeflection(_2585.CouplingHalfSystemDeflection):
    '''TorqueConverterPumpSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_PUMP_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2468.TorqueConverterPump':
        '''TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2468.TorqueConverterPump)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6807.TorqueConverterPumpLoadCase':
        '''TorqueConverterPumpLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6807.TorqueConverterPumpLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_4008.TorqueConverterPumpPowerFlow':
        '''TorqueConverterPumpPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4008.TorqueConverterPumpPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
