'''_4947.py

AssemblyModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2296, _2335
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6653, _6781
from mastapy.system_model.analyses_and_results.system_deflections import _2552, _2655
from mastapy.system_model.analyses_and_results.modal_analyses import (
    _4997, _4948, _4950, _4953,
    _4960, _4959, _4963, _4968,
    _4971, _4982, _4984, _4986,
    _4990, _4996, _4998, _5006,
    _5013, _5016, _5017, _5018,
    _5023, _5028, _5031, _5032,
    _5033, _5041, _5035, _5037,
    _5042, _5048, _5051, _5054,
    _5057, _5061, _5065, _5068,
    _5077, _5080, _4940
)
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _5081
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'AssemblyModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyModalAnalysis',)


class AssemblyModalAnalysis(_4940.AbstractAssemblyModalAnalysis):
    '''AssemblyModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyModalAnalysis.TYPE'):
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
    def full_fe_meshes_for_calculating_modes(self) -> 'List[_4997.FEPartModalAnalysis]':
        '''List[FEPartModalAnalysis]: 'FullFEMeshesForCalculatingModes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FullFEMeshesForCalculatingModes, constructor.new(_4997.FEPartModalAnalysis))
        return value

    @property
    def calculate_full_fe_results_by_mode(self) -> 'List[_5081.CalculateFullFEResultsForMode]':
        '''List[CalculateFullFEResultsForMode]: 'CalculateFullFEResultsByMode' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CalculateFullFEResultsByMode, constructor.new(_5081.CalculateFullFEResultsForMode))
        return value

    @property
    def bearings(self) -> 'List[_4948.BearingModalAnalysis]':
        '''List[BearingModalAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_4948.BearingModalAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_4950.BeltDriveModalAnalysis]':
        '''List[BeltDriveModalAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_4950.BeltDriveModalAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4953.BevelDifferentialGearSetModalAnalysis]':
        '''List[BevelDifferentialGearSetModalAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_4953.BevelDifferentialGearSetModalAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_4960.BoltModalAnalysis]':
        '''List[BoltModalAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_4960.BoltModalAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_4959.BoltedJointModalAnalysis]':
        '''List[BoltedJointModalAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_4959.BoltedJointModalAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_4963.ClutchModalAnalysis]':
        '''List[ClutchModalAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_4963.ClutchModalAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_4968.ConceptCouplingModalAnalysis]':
        '''List[ConceptCouplingModalAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_4968.ConceptCouplingModalAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4971.ConceptGearSetModalAnalysis]':
        '''List[ConceptGearSetModalAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_4971.ConceptGearSetModalAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_4982.CVTModalAnalysis]':
        '''List[CVTModalAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_4982.CVTModalAnalysis))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_4984.CycloidalAssemblyModalAnalysis]':
        '''List[CycloidalAssemblyModalAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_4984.CycloidalAssemblyModalAnalysis))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_4986.CycloidalDiscModalAnalysis]':
        '''List[CycloidalDiscModalAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_4986.CycloidalDiscModalAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4990.CylindricalGearSetModalAnalysis]':
        '''List[CylindricalGearSetModalAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_4990.CylindricalGearSetModalAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_4996.FaceGearSetModalAnalysis]':
        '''List[FaceGearSetModalAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_4996.FaceGearSetModalAnalysis))
        return value

    @property
    def fe_parts(self) -> 'List[_4997.FEPartModalAnalysis]':
        '''List[FEPartModalAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_4997.FEPartModalAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4998.FlexiblePinAssemblyModalAnalysis]':
        '''List[FlexiblePinAssemblyModalAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_4998.FlexiblePinAssemblyModalAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5006.HypoidGearSetModalAnalysis]':
        '''List[HypoidGearSetModalAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5006.HypoidGearSetModalAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5013.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetModalAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5013.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5016.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5016.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5017.MassDiscModalAnalysis]':
        '''List[MassDiscModalAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5017.MassDiscModalAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5018.MeasurementComponentModalAnalysis]':
        '''List[MeasurementComponentModalAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5018.MeasurementComponentModalAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5023.OilSealModalAnalysis]':
        '''List[OilSealModalAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5023.OilSealModalAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5028.PartToPartShearCouplingModalAnalysis]':
        '''List[PartToPartShearCouplingModalAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5028.PartToPartShearCouplingModalAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5031.PlanetCarrierModalAnalysis]':
        '''List[PlanetCarrierModalAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5031.PlanetCarrierModalAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5032.PointLoadModalAnalysis]':
        '''List[PointLoadModalAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5032.PointLoadModalAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5033.PowerLoadModalAnalysis]':
        '''List[PowerLoadModalAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5033.PowerLoadModalAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5041.ShaftHubConnectionModalAnalysis]':
        '''List[ShaftHubConnectionModalAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5041.ShaftHubConnectionModalAnalysis))
        return value

    @property
    def ring_pins(self) -> 'List[_5035.RingPinsModalAnalysis]':
        '''List[RingPinsModalAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_5035.RingPinsModalAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5037.RollingRingAssemblyModalAnalysis]':
        '''List[RollingRingAssemblyModalAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5037.RollingRingAssemblyModalAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5042.ShaftModalAnalysis]':
        '''List[ShaftModalAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5042.ShaftModalAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5048.SpiralBevelGearSetModalAnalysis]':
        '''List[SpiralBevelGearSetModalAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5048.SpiralBevelGearSetModalAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5051.SpringDamperModalAnalysis]':
        '''List[SpringDamperModalAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5051.SpringDamperModalAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5054.StraightBevelDiffGearSetModalAnalysis]':
        '''List[StraightBevelDiffGearSetModalAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5054.StraightBevelDiffGearSetModalAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5057.StraightBevelGearSetModalAnalysis]':
        '''List[StraightBevelGearSetModalAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5057.StraightBevelGearSetModalAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5061.SynchroniserModalAnalysis]':
        '''List[SynchroniserModalAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5061.SynchroniserModalAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5065.TorqueConverterModalAnalysis]':
        '''List[TorqueConverterModalAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5065.TorqueConverterModalAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5068.UnbalancedMassModalAnalysis]':
        '''List[UnbalancedMassModalAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5068.UnbalancedMassModalAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5077.WormGearSetModalAnalysis]':
        '''List[WormGearSetModalAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5077.WormGearSetModalAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5080.ZerolBevelGearSetModalAnalysis]':
        '''List[ZerolBevelGearSetModalAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5080.ZerolBevelGearSetModalAnalysis))
        return value

    def calculate_all_selected_strain_and_kinetic_energies(self):
        ''' 'CalculateAllSelectedStrainAndKineticEnergies' is the original name of this method.'''

        self.wrapped.CalculateAllSelectedStrainAndKineticEnergies()

    def calculate_all_strain_and_kinetic_energies(self):
        ''' 'CalculateAllStrainAndKineticEnergies' is the original name of this method.'''

        self.wrapped.CalculateAllStrainAndKineticEnergies()
