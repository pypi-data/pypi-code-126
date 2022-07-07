'''_2606.py

DatumSystemDeflection
'''


from mastapy.system_model.part_model import _2310
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6703
from mastapy.system_model.analyses_and_results.power_flows import _3937
from mastapy.system_model.analyses_and_results.system_deflections import _2570
from mastapy._internal.python_net import python_net_import

_DATUM_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'DatumSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumSystemDeflection',)


class DatumSystemDeflection(_2570.ComponentSystemDeflection):
    '''DatumSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _DATUM_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2310.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2310.Datum)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6703.DatumLoadCase':
        '''DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6703.DatumLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3937.DatumPowerFlow':
        '''DatumPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3937.DatumPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
