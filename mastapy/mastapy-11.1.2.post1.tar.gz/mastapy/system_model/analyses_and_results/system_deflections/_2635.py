'''_2635.py

MeasurementComponentSystemDeflection
'''


from mastapy.system_model.part_model import _2324
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6755
from mastapy.system_model.analyses_and_results.power_flows import _3962
from mastapy.system_model.analyses_and_results.system_deflections import _2690
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'MeasurementComponentSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentSystemDeflection',)


class MeasurementComponentSystemDeflection(_2690.VirtualComponentSystemDeflection):
    '''MeasurementComponentSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2324.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2324.MeasurementComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6755.MeasurementComponentLoadCase':
        '''MeasurementComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6755.MeasurementComponentLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3962.MeasurementComponentPowerFlow':
        '''MeasurementComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3962.MeasurementComponentPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
