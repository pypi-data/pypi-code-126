'''_3024.py

FEPartCompoundSteadyStateSynchronousResponseOnAShaft
'''


from typing import List

from mastapy.system_model.part_model import _2314
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2894
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _2970
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'FEPartCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartCompoundSteadyStateSynchronousResponseOnAShaft',)


class FEPartCompoundSteadyStateSynchronousResponseOnAShaft(_2970.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft):
    '''FEPartCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _FE_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEPartCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2314.FEPart':
        '''FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2314.FEPart)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2894.FEPartSteadyStateSynchronousResponseOnAShaft]':
        '''List[FEPartSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_2894.FEPartSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def planetaries(self) -> 'List[FEPartCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[FEPartCompoundSteadyStateSynchronousResponseOnAShaft]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(FEPartCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2894.FEPartSteadyStateSynchronousResponseOnAShaft]':
        '''List[FEPartSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_2894.FEPartSteadyStateSynchronousResponseOnAShaft))
        return value
