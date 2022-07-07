'''_2629.py

KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
'''


from mastapy.system_model.connections_and_sockets.gears import _2182
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6752
from mastapy.system_model.analyses_and_results.power_flows import _3958
from mastapy.gears.rating.klingelnberg_spiral_bevel import _376
from mastapy.system_model.analyses_and_results.system_deflections import _2623
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection',)


class KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection(_2623.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection):
    '''KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2182.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        '''KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2182.KlingelnbergCycloPalloidSpiralBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6752.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase':
        '''KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6752.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3958.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow':
        '''KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3958.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def rating(self) -> '_376.KlingelnbergCycloPalloidSpiralBevelGearMeshRating':
        '''KlingelnbergCycloPalloidSpiralBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_376.KlingelnbergCycloPalloidSpiralBevelGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def component_detailed_analysis(self) -> '_376.KlingelnbergCycloPalloidSpiralBevelGearMeshRating':
        '''KlingelnbergCycloPalloidSpiralBevelGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_376.KlingelnbergCycloPalloidSpiralBevelGearMeshRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
