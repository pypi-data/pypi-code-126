'''_4223.py

KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2181
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6749
from mastapy.system_model.analyses_and_results.system_deflections import _2626
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4220
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool',)


class KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool(_4220.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool):
    '''KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2181.KlingelnbergCycloPalloidHypoidGearMesh':
        '''KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2181.KlingelnbergCycloPalloidHypoidGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6749.KlingelnbergCycloPalloidHypoidGearMeshLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6749.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2626.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2626.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection))
        return value
