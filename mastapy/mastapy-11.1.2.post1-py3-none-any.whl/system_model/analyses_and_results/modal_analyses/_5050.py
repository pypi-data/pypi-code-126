'''_5050.py

SpringDamperHalfModalAnalysis
'''


from mastapy.system_model.part_model.couplings import _2461
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6790
from mastapy.system_model.analyses_and_results.system_deflections import _2666
from mastapy.system_model.analyses_and_results.modal_analyses import _4979
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'SpringDamperHalfModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfModalAnalysis',)


class SpringDamperHalfModalAnalysis(_4979.CouplingHalfModalAnalysis):
    '''SpringDamperHalfModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_HALF_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2461.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2461.SpringDamperHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6790.SpringDamperHalfLoadCase':
        '''SpringDamperHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6790.SpringDamperHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2666.SpringDamperHalfSystemDeflection':
        '''SpringDamperHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2666.SpringDamperHalfSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
