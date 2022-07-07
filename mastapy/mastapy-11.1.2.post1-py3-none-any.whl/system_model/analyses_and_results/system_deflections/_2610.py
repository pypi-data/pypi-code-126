'''_2610.py

FaceGearSetSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2389
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6719
from mastapy.system_model.analyses_and_results.power_flows import _3941
from mastapy.gears.rating.face import _421
from mastapy.system_model.analyses_and_results.system_deflections import _2611, _2609, _2615
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'FaceGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetSystemDeflection',)


class FaceGearSetSystemDeflection(_2615.GearSetSystemDeflection):
    '''FaceGearSetSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2389.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2389.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6719.FaceGearSetLoadCase':
        '''FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6719.FaceGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3941.FaceGearSetPowerFlow':
        '''FaceGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3941.FaceGearSetPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def rating(self) -> '_421.FaceGearSetRating':
        '''FaceGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_421.FaceGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def component_detailed_analysis(self) -> '_421.FaceGearSetRating':
        '''FaceGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_421.FaceGearSetRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def face_gears_system_deflection(self) -> 'List[_2611.FaceGearSystemDeflection]':
        '''List[FaceGearSystemDeflection]: 'FaceGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsSystemDeflection, constructor.new(_2611.FaceGearSystemDeflection))
        return value

    @property
    def face_meshes_system_deflection(self) -> 'List[_2609.FaceGearMeshSystemDeflection]':
        '''List[FaceGearMeshSystemDeflection]: 'FaceMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesSystemDeflection, constructor.new(_2609.FaceGearMeshSystemDeflection))
        return value
