'''_2530.py

CompoundHarmonicAnalysisOfSingleExcitationAnalysis
'''


from typing import Iterable

from mastapy.system_model.connections_and_sockets.couplings import (
    _2212, _2214, _2210, _2204,
    _2206, _2208
)
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _5756, _5771, _5654, _5653,
    _5655, _5661, _5672, _5673,
    _5678, _5689, _5704, _5705,
    _5709, _5710, _5660, _5714,
    _5728, _5729, _5730, _5731,
    _5732, _5738, _5739, _5740,
    _5747, _5751, _5774, _5775,
    _5748, _5682, _5684, _5706,
    _5708, _5657, _5659, _5664,
    _5666, _5667, _5668, _5669,
    _5671, _5685, _5687, _5700,
    _5702, _5703, _5711, _5713,
    _5715, _5717, _5719, _5721,
    _5722, _5724, _5725, _5727,
    _5737, _5752, _5754, _5758,
    _5760, _5761, _5763, _5764,
    _5765, _5776, _5778, _5779,
    _5781, _5696, _5698, _5742,
    _5733, _5735, _5663, _5674,
    _5676, _5679, _5681, _5690,
    _5692, _5694, _5695, _5741,
    _5749, _5745, _5744, _5755,
    _5757, _5766, _5767, _5768,
    _5769, _5770, _5772, _5773,
    _5750, _5693, _5662, _5677,
    _5688, _5718, _5736, _5746,
    _5656, _5665, _5683, _5707,
    _5759, _5670, _5686, _5658,
    _5701, _5716, _5720, _5723,
    _5726, _5753, _5762, _5777,
    _5780, _5712, _5697, _5699,
    _5743, _5734, _5675, _5680,
    _5691
)
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import (
    _2298, _2297, _2299, _2302,
    _2304, _2305, _2306, _2309,
    _2310, _2313, _2314, _2315,
    _2296, _2316, _2323, _2324,
    _2325, _2327, _2329, _2330,
    _2332, _2333, _2335, _2337,
    _2338, _2340
)
from mastapy.system_model.part_model.shaft_model import _2343
from mastapy.system_model.part_model.gears import (
    _2381, _2382, _2388, _2389,
    _2373, _2374, _2375, _2376,
    _2377, _2378, _2379, _2380,
    _2383, _2384, _2385, _2386,
    _2387, _2390, _2392, _2394,
    _2395, _2396, _2397, _2398,
    _2399, _2400, _2401, _2402,
    _2403, _2404, _2405, _2406,
    _2407, _2408, _2409, _2410,
    _2411, _2412, _2413, _2414
)
from mastapy.system_model.part_model.cycloidal import _2428, _2429, _2430
from mastapy.system_model.part_model.couplings import (
    _2448, _2449, _2436, _2438,
    _2439, _2441, _2442, _2443,
    _2444, _2446, _2447, _2450,
    _2458, _2456, _2457, _2460,
    _2461, _2462, _2464, _2465,
    _2466, _2467, _2468, _2470
)
from mastapy.system_model.connections_and_sockets import (
    _2157, _2135, _2130, _2131,
    _2134, _2143, _2149, _2154,
    _2127
)
from mastapy.system_model.connections_and_sockets.gears import (
    _2163, _2167, _2173, _2187,
    _2165, _2169, _2161, _2171,
    _2177, _2180, _2181, _2182,
    _2185, _2189, _2191, _2193,
    _2175
)
from mastapy.system_model.connections_and_sockets.cycloidal import _2197, _2200, _2203
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2479

_SPRING_DAMPER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'SpringDamperConnection')
_TORQUE_CONVERTER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'TorqueConverterConnection')
_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'PartToPartShearCouplingConnection')
_CLUTCH_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ClutchConnection')
_CONCEPT_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ConceptCouplingConnection')
_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'CouplingConnection')
_ABSTRACT_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractShaft')
_ABSTRACT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractAssembly')
_ABSTRACT_SHAFT_OR_HOUSING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractShaftOrHousing')
_BEARING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bearing')
_BOLT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bolt')
_BOLTED_JOINT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'BoltedJoint')
_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Component')
_CONNECTOR = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Connector')
_DATUM = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Datum')
_EXTERNAL_CAD_MODEL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ExternalCADModel')
_FE_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'FEPart')
_FLEXIBLE_PIN_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'FlexiblePinAssembly')
_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Assembly')
_GUIDE_DXF_MODEL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'GuideDxfModel')
_MASS_DISC = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MassDisc')
_MEASUREMENT_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MeasurementComponent')
_MOUNTABLE_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MountableComponent')
_OIL_SEAL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'OilSeal')
_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Part')
_PLANET_CARRIER = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PlanetCarrier')
_POINT_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PointLoad')
_POWER_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PowerLoad')
_ROOT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'RootAssembly')
_SPECIALISED_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'SpecialisedAssembly')
_UNBALANCED_MASS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'UnbalancedMass')
_VIRTUAL_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'VirtualComponent')
_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ShaftModel', 'Shaft')
_CONCEPT_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGear')
_CONCEPT_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGearSet')
_FACE_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGear')
_FACE_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGearSet')
_AGMA_GLEASON_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGear')
_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGearSet')
_BEVEL_DIFFERENTIAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGear')
_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGearSet')
_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialPlanetGear')
_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialSunGear')
_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGear')
_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGearSet')
_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGear')
_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGearSet')
_CYLINDRICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGear')
_CYLINDRICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGearSet')
_CYLINDRICAL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalPlanetGear')
_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'Gear')
_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'GearSet')
_HYPOID_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGear')
_HYPOID_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGearSet')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGear')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGearSet')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGear')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGearSet')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGear')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearSet')
_PLANETARY_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'PlanetaryGearSet')
_SPIRAL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGear')
_SPIRAL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGearSet')
_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGear')
_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGearSet')
_STRAIGHT_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGear')
_STRAIGHT_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGearSet')
_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelPlanetGear')
_STRAIGHT_BEVEL_SUN_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelSunGear')
_WORM_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGear')
_WORM_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGearSet')
_ZEROL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGear')
_ZEROL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGearSet')
_CYCLOIDAL_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'CycloidalAssembly')
_CYCLOIDAL_DISC = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'CycloidalDisc')
_RING_PINS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'RingPins')
_PART_TO_PART_SHEAR_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCoupling')
_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCouplingHalf')
_BELT_DRIVE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'BeltDrive')
_CLUTCH = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Clutch')
_CLUTCH_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ClutchHalf')
_CONCEPT_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCoupling')
_CONCEPT_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCouplingHalf')
_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Coupling')
_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CouplingHalf')
_CVT = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVT')
_CVT_PULLEY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVTPulley')
_PULLEY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Pulley')
_SHAFT_HUB_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ShaftHubConnection')
_ROLLING_RING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRing')
_ROLLING_RING_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRingAssembly')
_SPRING_DAMPER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamper')
_SPRING_DAMPER_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamperHalf')
_SYNCHRONISER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Synchroniser')
_SYNCHRONISER_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserHalf')
_SYNCHRONISER_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserPart')
_SYNCHRONISER_SLEEVE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserSleeve')
_TORQUE_CONVERTER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverter')
_TORQUE_CONVERTER_PUMP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterPump')
_TORQUE_CONVERTER_TURBINE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterTurbine')
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ShaftToMountableComponentConnection')
_CVT_BELT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CVTBeltConnection')
_BELT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'BeltConnection')
_COAXIAL_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CoaxialConnection')
_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'Connection')
_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'InterMountableComponentConnection')
_PLANETARY_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'PlanetaryConnection')
_ROLLING_RING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'RollingRingConnection')
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'AbstractShaftToMountableComponentConnection')
_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelDifferentialGearMesh')
_CONCEPT_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ConceptGearMesh')
_FACE_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'FaceGearMesh')
_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelDiffGearMesh')
_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelGearMesh')
_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ConicalGearMesh')
_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'AGMAGleasonConicalGearMesh')
_CYLINDRICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'CylindricalGearMesh')
_HYPOID_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'HypoidGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidConicalGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidHypoidGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearMesh')
_SPIRAL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'SpiralBevelGearMesh')
_STRAIGHT_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelGearMesh')
_WORM_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'WormGearMesh')
_ZEROL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ZerolBevelGearMesh')
_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'GearMesh')
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'CycloidalDiscCentralBearingConnection')
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'CycloidalDiscPlanetaryBearingConnection')
_RING_PINS_TO_DISC_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'RingPinsToDiscConnection')
_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundHarmonicAnalysisOfSingleExcitationAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundHarmonicAnalysisOfSingleExcitationAnalysis',)


class CompoundHarmonicAnalysisOfSingleExcitationAnalysis(_2479.CompoundAnalysis):
    '''CompoundHarmonicAnalysisOfSingleExcitationAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundHarmonicAnalysisOfSingleExcitationAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_spring_damper_connection(self, design_entity: '_2212.SpringDamperConnection') -> 'Iterable[_5756.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5756.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_torque_converter_connection(self, design_entity: '_2214.TorqueConverterConnection') -> 'Iterable[_5771.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5771.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_abstract_shaft(self, design_entity: '_2298.AbstractShaft') -> 'Iterable[_5654.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](design_entity.wrapped if design_entity else None), constructor.new(_5654.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_abstract_assembly(self, design_entity: '_2297.AbstractAssembly') -> 'Iterable[_5653.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5653.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2299.AbstractShaftOrHousing') -> 'Iterable[_5655.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](design_entity.wrapped if design_entity else None), constructor.new(_5655.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bearing(self, design_entity: '_2302.Bearing') -> 'Iterable[_5661.BearingCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BearingCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEARING](design_entity.wrapped if design_entity else None), constructor.new(_5661.BearingCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bolt(self, design_entity: '_2304.Bolt') -> 'Iterable[_5672.BoltCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BoltCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BOLT](design_entity.wrapped if design_entity else None), constructor.new(_5672.BoltCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bolted_joint(self, design_entity: '_2305.BoltedJoint') -> 'Iterable[_5673.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](design_entity.wrapped if design_entity else None), constructor.new(_5673.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_component(self, design_entity: '_2306.Component') -> 'Iterable[_5678.ComponentCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ComponentCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5678.ComponentCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_connector(self, design_entity: '_2309.Connector') -> 'Iterable[_5689.ConnectorCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConnectorCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONNECTOR](design_entity.wrapped if design_entity else None), constructor.new(_5689.ConnectorCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_datum(self, design_entity: '_2310.Datum') -> 'Iterable[_5704.DatumCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.DatumCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_DATUM](design_entity.wrapped if design_entity else None), constructor.new(_5704.DatumCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_external_cad_model(self, design_entity: '_2313.ExternalCADModel') -> 'Iterable[_5705.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](design_entity.wrapped if design_entity else None), constructor.new(_5705.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_fe_part(self, design_entity: '_2314.FEPart') -> 'Iterable[_5709.FEPartCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.FEPartCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FE_PART](design_entity.wrapped if design_entity else None), constructor.new(_5709.FEPartCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_flexible_pin_assembly(self, design_entity: '_2315.FlexiblePinAssembly') -> 'Iterable[_5710.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5710.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_assembly(self, design_entity: '_2296.Assembly') -> 'Iterable[_5660.AssemblyCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AssemblyCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5660.AssemblyCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_guide_dxf_model(self, design_entity: '_2316.GuideDxfModel') -> 'Iterable[_5714.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](design_entity.wrapped if design_entity else None), constructor.new(_5714.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_mass_disc(self, design_entity: '_2323.MassDisc') -> 'Iterable[_5728.MassDiscCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.MassDiscCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MASS_DISC](design_entity.wrapped if design_entity else None), constructor.new(_5728.MassDiscCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_measurement_component(self, design_entity: '_2324.MeasurementComponent') -> 'Iterable[_5729.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5729.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_mountable_component(self, design_entity: '_2325.MountableComponent') -> 'Iterable[_5730.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5730.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_oil_seal(self, design_entity: '_2327.OilSeal') -> 'Iterable[_5731.OilSealCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.OilSealCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_OIL_SEAL](design_entity.wrapped if design_entity else None), constructor.new(_5731.OilSealCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_part(self, design_entity: '_2329.Part') -> 'Iterable[_5732.PartCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PartCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART](design_entity.wrapped if design_entity else None), constructor.new(_5732.PartCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_planet_carrier(self, design_entity: '_2330.PlanetCarrier') -> 'Iterable[_5738.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](design_entity.wrapped if design_entity else None), constructor.new(_5738.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_point_load(self, design_entity: '_2332.PointLoad') -> 'Iterable[_5739.PointLoadCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PointLoadCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_POINT_LOAD](design_entity.wrapped if design_entity else None), constructor.new(_5739.PointLoadCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_power_load(self, design_entity: '_2333.PowerLoad') -> 'Iterable[_5740.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_POWER_LOAD](design_entity.wrapped if design_entity else None), constructor.new(_5740.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_root_assembly(self, design_entity: '_2335.RootAssembly') -> 'Iterable[_5747.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5747.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_specialised_assembly(self, design_entity: '_2337.SpecialisedAssembly') -> 'Iterable[_5751.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5751.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_unbalanced_mass(self, design_entity: '_2338.UnbalancedMass') -> 'Iterable[_5774.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](design_entity.wrapped if design_entity else None), constructor.new(_5774.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_virtual_component(self, design_entity: '_2340.VirtualComponent') -> 'Iterable[_5775.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5775.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_shaft(self, design_entity: '_2343.Shaft') -> 'Iterable[_5748.ShaftCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ShaftCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT](design_entity.wrapped if design_entity else None), constructor.new(_5748.ShaftCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_concept_gear(self, design_entity: '_2381.ConceptGear') -> 'Iterable[_5682.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5682.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_concept_gear_set(self, design_entity: '_2382.ConceptGearSet') -> 'Iterable[_5684.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5684.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_face_gear(self, design_entity: '_2388.FaceGear') -> 'Iterable[_5706.FaceGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.FaceGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5706.FaceGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_face_gear_set(self, design_entity: '_2389.FaceGearSet') -> 'Iterable[_5708.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5708.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2373.AGMAGleasonConicalGear') -> 'Iterable[_5657.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5657.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2374.AGMAGleasonConicalGearSet') -> 'Iterable[_5659.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5659.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bevel_differential_gear(self, design_entity: '_2375.BevelDifferentialGear') -> 'Iterable[_5664.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5664.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2376.BevelDifferentialGearSet') -> 'Iterable[_5666.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5666.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2377.BevelDifferentialPlanetGear') -> 'Iterable[_5667.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5667.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2378.BevelDifferentialSunGear') -> 'Iterable[_5668.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5668.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bevel_gear(self, design_entity: '_2379.BevelGear') -> 'Iterable[_5669.BevelGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5669.BevelGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bevel_gear_set(self, design_entity: '_2380.BevelGearSet') -> 'Iterable[_5671.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5671.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_conical_gear(self, design_entity: '_2383.ConicalGear') -> 'Iterable[_5685.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5685.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_conical_gear_set(self, design_entity: '_2384.ConicalGearSet') -> 'Iterable[_5687.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5687.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cylindrical_gear(self, design_entity: '_2385.CylindricalGear') -> 'Iterable[_5700.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5700.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cylindrical_gear_set(self, design_entity: '_2386.CylindricalGearSet') -> 'Iterable[_5702.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5702.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2387.CylindricalPlanetGear') -> 'Iterable[_5703.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5703.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_gear(self, design_entity: '_2390.Gear') -> 'Iterable[_5711.GearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.GearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5711.GearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_gear_set(self, design_entity: '_2392.GearSet') -> 'Iterable[_5713.GearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.GearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5713.GearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_hypoid_gear(self, design_entity: '_2394.HypoidGear') -> 'Iterable[_5715.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5715.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_hypoid_gear_set(self, design_entity: '_2395.HypoidGearSet') -> 'Iterable[_5717.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5717.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2396.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_5719.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5719.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2397.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_5721.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5721.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2398.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_5722.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5722.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2399.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_5724.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5724.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2400.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_5725.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5725.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2401.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_5727.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5727.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_planetary_gear_set(self, design_entity: '_2402.PlanetaryGearSet') -> 'Iterable[_5737.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5737.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_spiral_bevel_gear(self, design_entity: '_2403.SpiralBevelGear') -> 'Iterable[_5752.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5752.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2404.SpiralBevelGearSet') -> 'Iterable[_5754.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5754.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2405.StraightBevelDiffGear') -> 'Iterable[_5758.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5758.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2406.StraightBevelDiffGearSet') -> 'Iterable[_5760.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5760.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_straight_bevel_gear(self, design_entity: '_2407.StraightBevelGear') -> 'Iterable[_5761.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5761.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2408.StraightBevelGearSet') -> 'Iterable[_5763.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5763.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2409.StraightBevelPlanetGear') -> 'Iterable[_5764.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5764.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2410.StraightBevelSunGear') -> 'Iterable[_5765.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5765.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_worm_gear(self, design_entity: '_2411.WormGear') -> 'Iterable[_5776.WormGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.WormGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5776.WormGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_worm_gear_set(self, design_entity: '_2412.WormGearSet') -> 'Iterable[_5778.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5778.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_zerol_bevel_gear(self, design_entity: '_2413.ZerolBevelGear') -> 'Iterable[_5779.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5779.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2414.ZerolBevelGearSet') -> 'Iterable[_5781.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5781.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cycloidal_assembly(self, design_entity: '_2428.CycloidalAssembly') -> 'Iterable[_5696.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5696.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cycloidal_disc(self, design_entity: '_2429.CycloidalDisc') -> 'Iterable[_5698.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](design_entity.wrapped if design_entity else None), constructor.new(_5698.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_ring_pins(self, design_entity: '_2430.RingPins') -> 'Iterable[_5742.RingPinsCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RingPinsCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_RING_PINS](design_entity.wrapped if design_entity else None), constructor.new(_5742.RingPinsCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2448.PartToPartShearCoupling') -> 'Iterable[_5733.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](design_entity.wrapped if design_entity else None), constructor.new(_5733.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2449.PartToPartShearCouplingHalf') -> 'Iterable[_5735.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5735.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_belt_drive(self, design_entity: '_2436.BeltDrive') -> 'Iterable[_5663.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](design_entity.wrapped if design_entity else None), constructor.new(_5663.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_clutch(self, design_entity: '_2438.Clutch') -> 'Iterable[_5674.ClutchCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ClutchCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH](design_entity.wrapped if design_entity else None), constructor.new(_5674.ClutchCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_clutch_half(self, design_entity: '_2439.ClutchHalf') -> 'Iterable[_5676.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5676.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_concept_coupling(self, design_entity: '_2441.ConceptCoupling') -> 'Iterable[_5679.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](design_entity.wrapped if design_entity else None), constructor.new(_5679.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_concept_coupling_half(self, design_entity: '_2442.ConceptCouplingHalf') -> 'Iterable[_5681.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5681.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_coupling(self, design_entity: '_2443.Coupling') -> 'Iterable[_5690.CouplingCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CouplingCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING](design_entity.wrapped if design_entity else None), constructor.new(_5690.CouplingCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_coupling_half(self, design_entity: '_2444.CouplingHalf') -> 'Iterable[_5692.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5692.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cvt(self, design_entity: '_2446.CVT') -> 'Iterable[_5694.CVTCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CVTCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT](design_entity.wrapped if design_entity else None), constructor.new(_5694.CVTCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cvt_pulley(self, design_entity: '_2447.CVTPulley') -> 'Iterable[_5695.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](design_entity.wrapped if design_entity else None), constructor.new(_5695.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_pulley(self, design_entity: '_2450.Pulley') -> 'Iterable[_5741.PulleyCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PulleyCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PULLEY](design_entity.wrapped if design_entity else None), constructor.new(_5741.PulleyCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_shaft_hub_connection(self, design_entity: '_2458.ShaftHubConnection') -> 'Iterable[_5749.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5749.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_rolling_ring(self, design_entity: '_2456.RollingRing') -> 'Iterable[_5745.RollingRingCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RollingRingCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING](design_entity.wrapped if design_entity else None), constructor.new(_5745.RollingRingCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_rolling_ring_assembly(self, design_entity: '_2457.RollingRingAssembly') -> 'Iterable[_5744.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5744.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_spring_damper(self, design_entity: '_2460.SpringDamper') -> 'Iterable[_5755.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](design_entity.wrapped if design_entity else None), constructor.new(_5755.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_spring_damper_half(self, design_entity: '_2461.SpringDamperHalf') -> 'Iterable[_5757.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5757.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_synchroniser(self, design_entity: '_2462.Synchroniser') -> 'Iterable[_5766.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](design_entity.wrapped if design_entity else None), constructor.new(_5766.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_synchroniser_half(self, design_entity: '_2464.SynchroniserHalf') -> 'Iterable[_5767.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5767.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_synchroniser_part(self, design_entity: '_2465.SynchroniserPart') -> 'Iterable[_5768.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](design_entity.wrapped if design_entity else None), constructor.new(_5768.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_synchroniser_sleeve(self, design_entity: '_2466.SynchroniserSleeve') -> 'Iterable[_5769.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](design_entity.wrapped if design_entity else None), constructor.new(_5769.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_torque_converter(self, design_entity: '_2467.TorqueConverter') -> 'Iterable[_5770.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](design_entity.wrapped if design_entity else None), constructor.new(_5770.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_torque_converter_pump(self, design_entity: '_2468.TorqueConverterPump') -> 'Iterable[_5772.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](design_entity.wrapped if design_entity else None), constructor.new(_5772.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_torque_converter_turbine(self, design_entity: '_2470.TorqueConverterTurbine') -> 'Iterable[_5773.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](design_entity.wrapped if design_entity else None), constructor.new(_5773.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_2157.ShaftToMountableComponentConnection') -> 'Iterable[_5750.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5750.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cvt_belt_connection(self, design_entity: '_2135.CVTBeltConnection') -> 'Iterable[_5693.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5693.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_belt_connection(self, design_entity: '_2130.BeltConnection') -> 'Iterable[_5662.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5662.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_coaxial_connection(self, design_entity: '_2131.CoaxialConnection') -> 'Iterable[_5677.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5677.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_connection(self, design_entity: '_2134.Connection') -> 'Iterable[_5688.ConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5688.ConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_inter_mountable_component_connection(self, design_entity: '_2143.InterMountableComponentConnection') -> 'Iterable[_5718.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5718.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_planetary_connection(self, design_entity: '_2149.PlanetaryConnection') -> 'Iterable[_5736.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5736.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_rolling_ring_connection(self, design_entity: '_2154.RollingRingConnection') -> 'Iterable[_5746.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5746.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_abstract_shaft_to_mountable_component_connection(self, design_entity: '_2127.AbstractShaftToMountableComponentConnection') -> 'Iterable[_5656.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5656.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_2163.BevelDifferentialGearMesh') -> 'Iterable[_5665.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5665.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_concept_gear_mesh(self, design_entity: '_2167.ConceptGearMesh') -> 'Iterable[_5683.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5683.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_face_gear_mesh(self, design_entity: '_2173.FaceGearMesh') -> 'Iterable[_5707.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5707.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_2187.StraightBevelDiffGearMesh') -> 'Iterable[_5759.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5759.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_bevel_gear_mesh(self, design_entity: '_2165.BevelGearMesh') -> 'Iterable[_5670.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5670.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_conical_gear_mesh(self, design_entity: '_2169.ConicalGearMesh') -> 'Iterable[_5686.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5686.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_2161.AGMAGleasonConicalGearMesh') -> 'Iterable[_5658.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5658.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_2171.CylindricalGearMesh') -> 'Iterable[_5701.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5701.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_hypoid_gear_mesh(self, design_entity: '_2177.HypoidGearMesh') -> 'Iterable[_5716.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5716.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_2180.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_5720.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5720.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_2181.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_5723.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5723.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_2182.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_5726.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5726.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_2185.SpiralBevelGearMesh') -> 'Iterable[_5753.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5753.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_2189.StraightBevelGearMesh') -> 'Iterable[_5762.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5762.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_worm_gear_mesh(self, design_entity: '_2191.WormGearMesh') -> 'Iterable[_5777.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5777.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_2193.ZerolBevelGearMesh') -> 'Iterable[_5780.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5780.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_gear_mesh(self, design_entity: '_2175.GearMesh') -> 'Iterable[_5712.GearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.GearMeshCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5712.GearMeshCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cycloidal_disc_central_bearing_connection(self, design_entity: '_2197.CycloidalDiscCentralBearingConnection') -> 'Iterable[_5697.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5697.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_cycloidal_disc_planetary_bearing_connection(self, design_entity: '_2200.CycloidalDiscPlanetaryBearingConnection') -> 'Iterable[_5699.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5699.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_ring_pins_to_disc_connection(self, design_entity: '_2203.RingPinsToDiscConnection') -> 'Iterable[_5743.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5743.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_2210.PartToPartShearCouplingConnection') -> 'Iterable[_5734.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5734.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_clutch_connection(self, design_entity: '_2204.ClutchConnection') -> 'Iterable[_5675.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5675.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_concept_coupling_connection(self, design_entity: '_2206.ConceptCouplingConnection') -> 'Iterable[_5680.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5680.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation))

    def results_for_coupling_connection(self, design_entity: '_2208.CouplingConnection') -> 'Iterable[_5691.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5691.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation))
