'''_3645.py

ConceptCouplingHalfStabilityAnalysis
'''


from mastapy.system_model.part_model.couplings import _2442
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6673
from mastapy.system_model.analyses_and_results.stability_analyses import _3656
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ConceptCouplingHalfStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfStabilityAnalysis',)


class ConceptCouplingHalfStabilityAnalysis(_3656.CouplingHalfStabilityAnalysis):
    '''ConceptCouplingHalfStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_HALF_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2442.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2442.ConceptCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6673.ConceptCouplingHalfLoadCase':
        '''ConceptCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6673.ConceptCouplingHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
