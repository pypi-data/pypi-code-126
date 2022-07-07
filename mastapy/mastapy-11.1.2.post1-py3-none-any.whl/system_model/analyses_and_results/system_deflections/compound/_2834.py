'''_2834.py

ZerolBevelGearCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2413
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2696
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2722
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ZerolBevelGearCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearCompoundSystemDeflection',)


class ZerolBevelGearCompoundSystemDeflection(_2722.BevelGearCompoundSystemDeflection):
    '''ZerolBevelGearCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2413.ZerolBevelGear':
        '''ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2413.ZerolBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2696.ZerolBevelGearSystemDeflection]':
        '''List[ZerolBevelGearSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_2696.ZerolBevelGearSystemDeflection))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2696.ZerolBevelGearSystemDeflection]':
        '''List[ZerolBevelGearSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_2696.ZerolBevelGearSystemDeflection))
        return value
