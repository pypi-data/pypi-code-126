'''_4087.py

KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.gears import _2398
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3956
from mastapy.system_model.analyses_and_results.power_flows.compound import _4084
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow',)


class KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow(_4084.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow):
    '''KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2398.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2398.KlingelnbergCycloPalloidHypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3956.KlingelnbergCycloPalloidHypoidGearPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3956.KlingelnbergCycloPalloidHypoidGearPowerFlow))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3956.KlingelnbergCycloPalloidHypoidGearPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3956.KlingelnbergCycloPalloidHypoidGearPowerFlow))
        return value
