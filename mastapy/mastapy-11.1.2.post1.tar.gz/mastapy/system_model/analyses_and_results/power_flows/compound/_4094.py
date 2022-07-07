'''_4094.py

MeasurementComponentCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model import _2324
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3962
from mastapy.system_model.analyses_and_results.power_flows.compound import _4140
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'MeasurementComponentCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentCompoundPowerFlow',)


class MeasurementComponentCompoundPowerFlow(_4140.VirtualComponentCompoundPowerFlow):
    '''MeasurementComponentCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentCompoundPowerFlow.TYPE'):
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
    def component_analysis_cases_ready(self) -> 'List[_3962.MeasurementComponentPowerFlow]':
        '''List[MeasurementComponentPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3962.MeasurementComponentPowerFlow))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3962.MeasurementComponentPowerFlow]':
        '''List[MeasurementComponentPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3962.MeasurementComponentPowerFlow))
        return value
