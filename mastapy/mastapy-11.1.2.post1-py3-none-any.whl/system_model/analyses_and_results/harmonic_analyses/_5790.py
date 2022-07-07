'''_5790.py

AssemblyHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2296, _2335
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6653, _6781
from mastapy.system_model.analyses_and_results.system_deflections import _2552, _2655
from mastapy.system_model.analyses_and_results.harmonic_analyses import (
    _5860, _5791, _5793, _5796,
    _5803, _5802, _5806, _5812,
    _5815, _5825, _5827, _5829,
    _5833, _5851, _5852, _5853,
    _5871, _5878, _5881, _5882,
    _5883, _5885, _5889, _5893,
    _5894, _5895, _5904, _5897,
    _5899, _5903, _5911, _5914,
    _5917, _5920, _5924, _5928,
    _5932, _5936, _5939, _5782
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'AssemblyHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyHarmonicAnalysis',)


class AssemblyHarmonicAnalysis(_5782.AbstractAssemblyHarmonicAnalysis):
    '''AssemblyHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2296.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2296.Assembly.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Assembly. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6653.AssemblyLoadCase':
        '''AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6653.AssemblyLoadCase.TYPE not in self.wrapped.AssemblyLoadCase.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to AssemblyLoadCase. Expected: {}.'.format(self.wrapped.AssemblyLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyLoadCase.__class__)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2552.AssemblySystemDeflection':
        '''AssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2552.AssemblySystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to AssemblySystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def loaded_gear_sets(self) -> 'List[_5860.GearSetHarmonicAnalysis]':
        '''List[GearSetHarmonicAnalysis]: 'LoadedGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadedGearSets, constructor.new(_5860.GearSetHarmonicAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_5791.BearingHarmonicAnalysis]':
        '''List[BearingHarmonicAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5791.BearingHarmonicAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5793.BeltDriveHarmonicAnalysis]':
        '''List[BeltDriveHarmonicAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5793.BeltDriveHarmonicAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5796.BevelDifferentialGearSetHarmonicAnalysis]':
        '''List[BevelDifferentialGearSetHarmonicAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5796.BevelDifferentialGearSetHarmonicAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5803.BoltHarmonicAnalysis]':
        '''List[BoltHarmonicAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5803.BoltHarmonicAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5802.BoltedJointHarmonicAnalysis]':
        '''List[BoltedJointHarmonicAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5802.BoltedJointHarmonicAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5806.ClutchHarmonicAnalysis]':
        '''List[ClutchHarmonicAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5806.ClutchHarmonicAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5812.ConceptCouplingHarmonicAnalysis]':
        '''List[ConceptCouplingHarmonicAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5812.ConceptCouplingHarmonicAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5815.ConceptGearSetHarmonicAnalysis]':
        '''List[ConceptGearSetHarmonicAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5815.ConceptGearSetHarmonicAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5825.CVTHarmonicAnalysis]':
        '''List[CVTHarmonicAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5825.CVTHarmonicAnalysis))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_5827.CycloidalAssemblyHarmonicAnalysis]':
        '''List[CycloidalAssemblyHarmonicAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_5827.CycloidalAssemblyHarmonicAnalysis))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_5829.CycloidalDiscHarmonicAnalysis]':
        '''List[CycloidalDiscHarmonicAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_5829.CycloidalDiscHarmonicAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5833.CylindricalGearSetHarmonicAnalysis]':
        '''List[CylindricalGearSetHarmonicAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5833.CylindricalGearSetHarmonicAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5851.FaceGearSetHarmonicAnalysis]':
        '''List[FaceGearSetHarmonicAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5851.FaceGearSetHarmonicAnalysis))
        return value

    @property
    def fe_parts(self) -> 'List[_5852.FEPartHarmonicAnalysis]':
        '''List[FEPartHarmonicAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_5852.FEPartHarmonicAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5853.FlexiblePinAssemblyHarmonicAnalysis]':
        '''List[FlexiblePinAssemblyHarmonicAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5853.FlexiblePinAssemblyHarmonicAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5871.HypoidGearSetHarmonicAnalysis]':
        '''List[HypoidGearSetHarmonicAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5871.HypoidGearSetHarmonicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5878.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5878.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5881.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5881.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5882.MassDiscHarmonicAnalysis]':
        '''List[MassDiscHarmonicAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5882.MassDiscHarmonicAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5883.MeasurementComponentHarmonicAnalysis]':
        '''List[MeasurementComponentHarmonicAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5883.MeasurementComponentHarmonicAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5885.OilSealHarmonicAnalysis]':
        '''List[OilSealHarmonicAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5885.OilSealHarmonicAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5889.PartToPartShearCouplingHarmonicAnalysis]':
        '''List[PartToPartShearCouplingHarmonicAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5889.PartToPartShearCouplingHarmonicAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5893.PlanetCarrierHarmonicAnalysis]':
        '''List[PlanetCarrierHarmonicAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5893.PlanetCarrierHarmonicAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5894.PointLoadHarmonicAnalysis]':
        '''List[PointLoadHarmonicAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5894.PointLoadHarmonicAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5895.PowerLoadHarmonicAnalysis]':
        '''List[PowerLoadHarmonicAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5895.PowerLoadHarmonicAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5904.ShaftHubConnectionHarmonicAnalysis]':
        '''List[ShaftHubConnectionHarmonicAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5904.ShaftHubConnectionHarmonicAnalysis))
        return value

    @property
    def ring_pins(self) -> 'List[_5897.RingPinsHarmonicAnalysis]':
        '''List[RingPinsHarmonicAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_5897.RingPinsHarmonicAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5899.RollingRingAssemblyHarmonicAnalysis]':
        '''List[RollingRingAssemblyHarmonicAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5899.RollingRingAssemblyHarmonicAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5903.ShaftHarmonicAnalysis]':
        '''List[ShaftHarmonicAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5903.ShaftHarmonicAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5911.SpiralBevelGearSetHarmonicAnalysis]':
        '''List[SpiralBevelGearSetHarmonicAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5911.SpiralBevelGearSetHarmonicAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5914.SpringDamperHarmonicAnalysis]':
        '''List[SpringDamperHarmonicAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5914.SpringDamperHarmonicAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5917.StraightBevelDiffGearSetHarmonicAnalysis]':
        '''List[StraightBevelDiffGearSetHarmonicAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5917.StraightBevelDiffGearSetHarmonicAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5920.StraightBevelGearSetHarmonicAnalysis]':
        '''List[StraightBevelGearSetHarmonicAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5920.StraightBevelGearSetHarmonicAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5924.SynchroniserHarmonicAnalysis]':
        '''List[SynchroniserHarmonicAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5924.SynchroniserHarmonicAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5928.TorqueConverterHarmonicAnalysis]':
        '''List[TorqueConverterHarmonicAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5928.TorqueConverterHarmonicAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5932.UnbalancedMassHarmonicAnalysis]':
        '''List[UnbalancedMassHarmonicAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5932.UnbalancedMassHarmonicAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5936.WormGearSetHarmonicAnalysis]':
        '''List[WormGearSetHarmonicAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5936.WormGearSetHarmonicAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5939.ZerolBevelGearSetHarmonicAnalysis]':
        '''List[ZerolBevelGearSetHarmonicAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5939.ZerolBevelGearSetHarmonicAnalysis))
        return value
