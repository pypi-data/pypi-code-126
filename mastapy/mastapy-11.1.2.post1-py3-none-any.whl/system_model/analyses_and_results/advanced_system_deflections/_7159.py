'''_7159.py

FaceGearAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2388
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6717
from mastapy.gears.rating.face import _419
from mastapy.system_model.analyses_and_results.system_deflections import _2611
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7164
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'FaceGearAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearAdvancedSystemDeflection',)


class FaceGearAdvancedSystemDeflection(_7164.GearAdvancedSystemDeflection):
    '''FaceGearAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2388.FaceGear':
        '''FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2388.FaceGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6717.FaceGearLoadCase':
        '''FaceGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6717.FaceGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def component_detailed_analysis(self) -> '_419.FaceGearRating':
        '''FaceGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_419.FaceGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2611.FaceGearSystemDeflection]':
        '''List[FaceGearSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2611.FaceGearSystemDeflection))
        return value
