'''_2668.py

StraightBevelDiffGearMeshSystemDeflection
'''


from mastapy.system_model.connections_and_sockets.gears import _2187
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6793
from mastapy.system_model.analyses_and_results.power_flows import _3993
from mastapy.gears.rating.straight_bevel_diff import _366
from mastapy.system_model.analyses_and_results.system_deflections import _2561
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'StraightBevelDiffGearMeshSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMeshSystemDeflection',)


class StraightBevelDiffGearMeshSystemDeflection(_2561.BevelGearMeshSystemDeflection):
    '''StraightBevelDiffGearMeshSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMeshSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2187.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2187.StraightBevelDiffGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6793.StraightBevelDiffGearMeshLoadCase':
        '''StraightBevelDiffGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6793.StraightBevelDiffGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3993.StraightBevelDiffGearMeshPowerFlow':
        '''StraightBevelDiffGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3993.StraightBevelDiffGearMeshPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def rating(self) -> '_366.StraightBevelDiffGearMeshRating':
        '''StraightBevelDiffGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_366.StraightBevelDiffGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def component_detailed_analysis(self) -> '_366.StraightBevelDiffGearMeshRating':
        '''StraightBevelDiffGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_366.StraightBevelDiffGearMeshRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
