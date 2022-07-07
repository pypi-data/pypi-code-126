'''_2975.py

AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
'''


from typing import List

from mastapy.system_model.part_model import _2296, _2335
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2845
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _2976, _2978, _2981, _2987,
    _2988, _2989, _2994, _2999,
    _3009, _3011, _3013, _3017,
    _3023, _3024, _3025, _3032,
    _3039, _3042, _3043, _3044,
    _3046, _3048, _3053, _3054,
    _3055, _3064, _3057, _3059,
    _3063, _3069, _3070, _3075,
    _3078, _3081, _3085, _3089,
    _3093, _3096, _2968
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'AssemblyCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundSteadyStateSynchronousResponseOnAShaft',)


class AssemblyCompoundSteadyStateSynchronousResponseOnAShaft(_2968.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft):
    '''AssemblyCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2296.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2296.Assembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

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
    def assembly_analysis_cases_ready(self) -> 'List[_2845.AssemblySteadyStateSynchronousResponseOnAShaft]':
        '''List[AssemblySteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_2845.AssemblySteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def bearings(self) -> 'List[_2976.BearingCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[BearingCompoundSteadyStateSynchronousResponseOnAShaft]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_2976.BearingCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def belt_drives(self) -> 'List[_2978.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_2978.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_2981.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_2981.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def bolts(self) -> 'List[_2987.BoltCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[BoltCompoundSteadyStateSynchronousResponseOnAShaft]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_2987.BoltCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def bolted_joints(self) -> 'List[_2988.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_2988.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def clutches(self) -> 'List[_2989.ClutchCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[ClutchCompoundSteadyStateSynchronousResponseOnAShaft]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_2989.ClutchCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def concept_couplings(self) -> 'List[_2994.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_2994.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_2999.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_2999.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def cv_ts(self) -> 'List[_3009.CVTCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[CVTCompoundSteadyStateSynchronousResponseOnAShaft]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3009.CVTCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_3011.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_3011.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_3013.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_3013.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3017.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3017.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3023.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3023.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def fe_parts(self) -> 'List[_3024.FEPartCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[FEPartCompoundSteadyStateSynchronousResponseOnAShaft]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_3024.FEPartCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3025.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3025.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3032.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3032.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3039.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3039.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3042.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3042.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def mass_discs(self) -> 'List[_3043.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[MassDiscCompoundSteadyStateSynchronousResponseOnAShaft]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3043.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def measurement_components(self) -> 'List[_3044.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3044.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def oil_seals(self) -> 'List[_3046.OilSealCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[OilSealCompoundSteadyStateSynchronousResponseOnAShaft]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3046.OilSealCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_3048.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_3048.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def planet_carriers(self) -> 'List[_3053.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3053.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def point_loads(self) -> 'List[_3054.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[PointLoadCompoundSteadyStateSynchronousResponseOnAShaft]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3054.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def power_loads(self) -> 'List[_3055.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3055.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3064.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3064.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def ring_pins(self) -> 'List[_3057.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[RingPinsCompoundSteadyStateSynchronousResponseOnAShaft]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_3057.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3059.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3059.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def shafts(self) -> 'List[_3063.ShaftCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[ShaftCompoundSteadyStateSynchronousResponseOnAShaft]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3063.ShaftCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3069.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3069.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def spring_dampers(self) -> 'List[_3070.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3070.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3075.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3075.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3078.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3078.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def synchronisers(self) -> 'List[_3081.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3081.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def torque_converters(self) -> 'List[_3085.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3085.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3089.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3089.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3093.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3093.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3096.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3096.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2845.AssemblySteadyStateSynchronousResponseOnAShaft]':
        '''List[AssemblySteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_2845.AssemblySteadyStateSynchronousResponseOnAShaft))
        return value
