'''_5005.py

HypoidGearModalAnalysis
'''


from mastapy.system_model.part_model.gears import _2394
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6738
from mastapy.system_model.analyses_and_results.system_deflections import _2620
from mastapy.system_model.analyses_and_results.modal_analyses import _4945
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'HypoidGearModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearModalAnalysis',)


class HypoidGearModalAnalysis(_4945.AGMAGleasonConicalGearModalAnalysis):
    '''HypoidGearModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2394.HypoidGear':
        '''HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2394.HypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6738.HypoidGearLoadCase':
        '''HypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6738.HypoidGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2620.HypoidGearSystemDeflection':
        '''HypoidGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2620.HypoidGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
