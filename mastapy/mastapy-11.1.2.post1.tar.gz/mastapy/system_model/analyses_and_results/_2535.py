'''_2535.py

CompoundMultibodyDynamicsAnalysis
'''


from typing import Iterable

from mastapy.system_model.connections_and_sockets.couplings import (
    _2212, _2214, _2210, _2204,
    _2206, _2208
)
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
    _5477, _5492, _5375, _5374,
    _5376, _5382, _5393, _5394,
    _5399, _5410, _5425, _5426,
    _5430, _5431, _5381, _5435,
    _5449, _5450, _5451, _5452,
    _5453, _5459, _5460, _5461,
    _5468, _5472, _5495, _5496,
    _5469, _5403, _5405, _5427,
    _5429, _5378, _5380, _5385,
    _5387, _5388, _5389, _5390,
    _5392, _5406, _5408, _5421,
    _5423, _5424, _5432, _5434,
    _5436, _5438, _5440, _5442,
    _5443, _5445, _5446, _5448,
    _5458, _5473, _5475, _5479,
    _5481, _5482, _5484, _5485,
    _5486, _5497, _5499, _5500,
    _5502, _5417, _5419, _5463,
    _5454, _5456, _5384, _5395,
    _5397, _5400, _5402, _5411,
    _5413, _5415, _5416, _5462,
    _5470, _5466, _5465, _5476,
    _5478, _5487, _5488, _5489,
    _5490, _5491, _5493, _5494,
    _5471, _5414, _5383, _5398,
    _5409, _5439, _5457, _5467,
    _5377, _5386, _5404, _5428,
    _5480, _5391, _5407, _5379,
    _5422, _5437, _5441, _5444,
    _5447, _5474, _5483, _5498,
    _5501, _5433, _5418, _5420,
    _5464, _5455, _5396, _5401,
    _5412
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
_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundMultibodyDynamicsAnalysis',)


class CompoundMultibodyDynamicsAnalysis(_2479.CompoundAnalysis):
    '''CompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_spring_damper_connection(self, design_entity: '_2212.SpringDamperConnection') -> 'Iterable[_5477.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5477.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_torque_converter_connection(self, design_entity: '_2214.TorqueConverterConnection') -> 'Iterable[_5492.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5492.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_abstract_shaft(self, design_entity: '_2298.AbstractShaft') -> 'Iterable[_5375.AbstractShaftCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractShaftCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](design_entity.wrapped if design_entity else None), constructor.new(_5375.AbstractShaftCompoundMultibodyDynamicsAnalysis))

    def results_for_abstract_assembly(self, design_entity: '_2297.AbstractAssembly') -> 'Iterable[_5374.AbstractAssemblyCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractAssemblyCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5374.AbstractAssemblyCompoundMultibodyDynamicsAnalysis))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2299.AbstractShaftOrHousing') -> 'Iterable[_5376.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](design_entity.wrapped if design_entity else None), constructor.new(_5376.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis))

    def results_for_bearing(self, design_entity: '_2302.Bearing') -> 'Iterable[_5382.BearingCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BearingCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEARING](design_entity.wrapped if design_entity else None), constructor.new(_5382.BearingCompoundMultibodyDynamicsAnalysis))

    def results_for_bolt(self, design_entity: '_2304.Bolt') -> 'Iterable[_5393.BoltCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BoltCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BOLT](design_entity.wrapped if design_entity else None), constructor.new(_5393.BoltCompoundMultibodyDynamicsAnalysis))

    def results_for_bolted_joint(self, design_entity: '_2305.BoltedJoint') -> 'Iterable[_5394.BoltedJointCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BoltedJointCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](design_entity.wrapped if design_entity else None), constructor.new(_5394.BoltedJointCompoundMultibodyDynamicsAnalysis))

    def results_for_component(self, design_entity: '_2306.Component') -> 'Iterable[_5399.ComponentCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ComponentCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5399.ComponentCompoundMultibodyDynamicsAnalysis))

    def results_for_connector(self, design_entity: '_2309.Connector') -> 'Iterable[_5410.ConnectorCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConnectorCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONNECTOR](design_entity.wrapped if design_entity else None), constructor.new(_5410.ConnectorCompoundMultibodyDynamicsAnalysis))

    def results_for_datum(self, design_entity: '_2310.Datum') -> 'Iterable[_5425.DatumCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.DatumCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_DATUM](design_entity.wrapped if design_entity else None), constructor.new(_5425.DatumCompoundMultibodyDynamicsAnalysis))

    def results_for_external_cad_model(self, design_entity: '_2313.ExternalCADModel') -> 'Iterable[_5426.ExternalCADModelCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ExternalCADModelCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](design_entity.wrapped if design_entity else None), constructor.new(_5426.ExternalCADModelCompoundMultibodyDynamicsAnalysis))

    def results_for_fe_part(self, design_entity: '_2314.FEPart') -> 'Iterable[_5430.FEPartCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FEPartCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FE_PART](design_entity.wrapped if design_entity else None), constructor.new(_5430.FEPartCompoundMultibodyDynamicsAnalysis))

    def results_for_flexible_pin_assembly(self, design_entity: '_2315.FlexiblePinAssembly') -> 'Iterable[_5431.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5431.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis))

    def results_for_assembly(self, design_entity: '_2296.Assembly') -> 'Iterable[_5381.AssemblyCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AssemblyCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5381.AssemblyCompoundMultibodyDynamicsAnalysis))

    def results_for_guide_dxf_model(self, design_entity: '_2316.GuideDxfModel') -> 'Iterable[_5435.GuideDxfModelCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GuideDxfModelCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](design_entity.wrapped if design_entity else None), constructor.new(_5435.GuideDxfModelCompoundMultibodyDynamicsAnalysis))

    def results_for_mass_disc(self, design_entity: '_2323.MassDisc') -> 'Iterable[_5449.MassDiscCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.MassDiscCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MASS_DISC](design_entity.wrapped if design_entity else None), constructor.new(_5449.MassDiscCompoundMultibodyDynamicsAnalysis))

    def results_for_measurement_component(self, design_entity: '_2324.MeasurementComponent') -> 'Iterable[_5450.MeasurementComponentCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.MeasurementComponentCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5450.MeasurementComponentCompoundMultibodyDynamicsAnalysis))

    def results_for_mountable_component(self, design_entity: '_2325.MountableComponent') -> 'Iterable[_5451.MountableComponentCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.MountableComponentCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5451.MountableComponentCompoundMultibodyDynamicsAnalysis))

    def results_for_oil_seal(self, design_entity: '_2327.OilSeal') -> 'Iterable[_5452.OilSealCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.OilSealCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_OIL_SEAL](design_entity.wrapped if design_entity else None), constructor.new(_5452.OilSealCompoundMultibodyDynamicsAnalysis))

    def results_for_part(self, design_entity: '_2329.Part') -> 'Iterable[_5453.PartCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART](design_entity.wrapped if design_entity else None), constructor.new(_5453.PartCompoundMultibodyDynamicsAnalysis))

    def results_for_planet_carrier(self, design_entity: '_2330.PlanetCarrier') -> 'Iterable[_5459.PlanetCarrierCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PlanetCarrierCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](design_entity.wrapped if design_entity else None), constructor.new(_5459.PlanetCarrierCompoundMultibodyDynamicsAnalysis))

    def results_for_point_load(self, design_entity: '_2332.PointLoad') -> 'Iterable[_5460.PointLoadCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PointLoadCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_POINT_LOAD](design_entity.wrapped if design_entity else None), constructor.new(_5460.PointLoadCompoundMultibodyDynamicsAnalysis))

    def results_for_power_load(self, design_entity: '_2333.PowerLoad') -> 'Iterable[_5461.PowerLoadCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PowerLoadCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_POWER_LOAD](design_entity.wrapped if design_entity else None), constructor.new(_5461.PowerLoadCompoundMultibodyDynamicsAnalysis))

    def results_for_root_assembly(self, design_entity: '_2335.RootAssembly') -> 'Iterable[_5468.RootAssemblyCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RootAssemblyCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5468.RootAssemblyCompoundMultibodyDynamicsAnalysis))

    def results_for_specialised_assembly(self, design_entity: '_2337.SpecialisedAssembly') -> 'Iterable[_5472.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5472.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis))

    def results_for_unbalanced_mass(self, design_entity: '_2338.UnbalancedMass') -> 'Iterable[_5495.UnbalancedMassCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.UnbalancedMassCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](design_entity.wrapped if design_entity else None), constructor.new(_5495.UnbalancedMassCompoundMultibodyDynamicsAnalysis))

    def results_for_virtual_component(self, design_entity: '_2340.VirtualComponent') -> 'Iterable[_5496.VirtualComponentCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.VirtualComponentCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5496.VirtualComponentCompoundMultibodyDynamicsAnalysis))

    def results_for_shaft(self, design_entity: '_2343.Shaft') -> 'Iterable[_5469.ShaftCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ShaftCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT](design_entity.wrapped if design_entity else None), constructor.new(_5469.ShaftCompoundMultibodyDynamicsAnalysis))

    def results_for_concept_gear(self, design_entity: '_2381.ConceptGear') -> 'Iterable[_5403.ConceptGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5403.ConceptGearCompoundMultibodyDynamicsAnalysis))

    def results_for_concept_gear_set(self, design_entity: '_2382.ConceptGearSet') -> 'Iterable[_5405.ConceptGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5405.ConceptGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_face_gear(self, design_entity: '_2388.FaceGear') -> 'Iterable[_5427.FaceGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5427.FaceGearCompoundMultibodyDynamicsAnalysis))

    def results_for_face_gear_set(self, design_entity: '_2389.FaceGearSet') -> 'Iterable[_5429.FaceGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5429.FaceGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2373.AGMAGleasonConicalGear') -> 'Iterable[_5378.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5378.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2374.AGMAGleasonConicalGearSet') -> 'Iterable[_5380.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5380.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_bevel_differential_gear(self, design_entity: '_2375.BevelDifferentialGear') -> 'Iterable[_5385.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5385.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2376.BevelDifferentialGearSet') -> 'Iterable[_5387.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5387.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2377.BevelDifferentialPlanetGear') -> 'Iterable[_5388.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5388.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2378.BevelDifferentialSunGear') -> 'Iterable[_5389.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5389.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis))

    def results_for_bevel_gear(self, design_entity: '_2379.BevelGear') -> 'Iterable[_5390.BevelGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5390.BevelGearCompoundMultibodyDynamicsAnalysis))

    def results_for_bevel_gear_set(self, design_entity: '_2380.BevelGearSet') -> 'Iterable[_5392.BevelGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5392.BevelGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_conical_gear(self, design_entity: '_2383.ConicalGear') -> 'Iterable[_5406.ConicalGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConicalGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5406.ConicalGearCompoundMultibodyDynamicsAnalysis))

    def results_for_conical_gear_set(self, design_entity: '_2384.ConicalGearSet') -> 'Iterable[_5408.ConicalGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConicalGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5408.ConicalGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_cylindrical_gear(self, design_entity: '_2385.CylindricalGear') -> 'Iterable[_5421.CylindricalGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5421.CylindricalGearCompoundMultibodyDynamicsAnalysis))

    def results_for_cylindrical_gear_set(self, design_entity: '_2386.CylindricalGearSet') -> 'Iterable[_5423.CylindricalGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5423.CylindricalGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2387.CylindricalPlanetGear') -> 'Iterable[_5424.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5424.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis))

    def results_for_gear(self, design_entity: '_2390.Gear') -> 'Iterable[_5432.GearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5432.GearCompoundMultibodyDynamicsAnalysis))

    def results_for_gear_set(self, design_entity: '_2392.GearSet') -> 'Iterable[_5434.GearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5434.GearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_hypoid_gear(self, design_entity: '_2394.HypoidGear') -> 'Iterable[_5436.HypoidGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.HypoidGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5436.HypoidGearCompoundMultibodyDynamicsAnalysis))

    def results_for_hypoid_gear_set(self, design_entity: '_2395.HypoidGearSet') -> 'Iterable[_5438.HypoidGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.HypoidGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5438.HypoidGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2396.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_5440.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5440.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2397.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_5442.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5442.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2398.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_5443.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5443.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2399.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_5445.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5445.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2400.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_5446.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5446.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2401.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_5448.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5448.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_planetary_gear_set(self, design_entity: '_2402.PlanetaryGearSet') -> 'Iterable[_5458.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5458.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_spiral_bevel_gear(self, design_entity: '_2403.SpiralBevelGear') -> 'Iterable[_5473.SpiralBevelGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpiralBevelGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5473.SpiralBevelGearCompoundMultibodyDynamicsAnalysis))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2404.SpiralBevelGearSet') -> 'Iterable[_5475.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5475.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2405.StraightBevelDiffGear') -> 'Iterable[_5479.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5479.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2406.StraightBevelDiffGearSet') -> 'Iterable[_5481.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5481.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_straight_bevel_gear(self, design_entity: '_2407.StraightBevelGear') -> 'Iterable[_5482.StraightBevelGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5482.StraightBevelGearCompoundMultibodyDynamicsAnalysis))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2408.StraightBevelGearSet') -> 'Iterable[_5484.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5484.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2409.StraightBevelPlanetGear') -> 'Iterable[_5485.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5485.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2410.StraightBevelSunGear') -> 'Iterable[_5486.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5486.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis))

    def results_for_worm_gear(self, design_entity: '_2411.WormGear') -> 'Iterable[_5497.WormGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5497.WormGearCompoundMultibodyDynamicsAnalysis))

    def results_for_worm_gear_set(self, design_entity: '_2412.WormGearSet') -> 'Iterable[_5499.WormGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5499.WormGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_zerol_bevel_gear(self, design_entity: '_2413.ZerolBevelGear') -> 'Iterable[_5500.ZerolBevelGearCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5500.ZerolBevelGearCompoundMultibodyDynamicsAnalysis))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2414.ZerolBevelGearSet') -> 'Iterable[_5502.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5502.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis))

    def results_for_cycloidal_assembly(self, design_entity: '_2428.CycloidalAssembly') -> 'Iterable[_5417.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5417.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis))

    def results_for_cycloidal_disc(self, design_entity: '_2429.CycloidalDisc') -> 'Iterable[_5419.CycloidalDiscCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalDiscCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](design_entity.wrapped if design_entity else None), constructor.new(_5419.CycloidalDiscCompoundMultibodyDynamicsAnalysis))

    def results_for_ring_pins(self, design_entity: '_2430.RingPins') -> 'Iterable[_5463.RingPinsCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RingPinsCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_RING_PINS](design_entity.wrapped if design_entity else None), constructor.new(_5463.RingPinsCompoundMultibodyDynamicsAnalysis))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2448.PartToPartShearCoupling') -> 'Iterable[_5454.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](design_entity.wrapped if design_entity else None), constructor.new(_5454.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2449.PartToPartShearCouplingHalf') -> 'Iterable[_5456.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5456.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis))

    def results_for_belt_drive(self, design_entity: '_2436.BeltDrive') -> 'Iterable[_5384.BeltDriveCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BeltDriveCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](design_entity.wrapped if design_entity else None), constructor.new(_5384.BeltDriveCompoundMultibodyDynamicsAnalysis))

    def results_for_clutch(self, design_entity: '_2438.Clutch') -> 'Iterable[_5395.ClutchCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ClutchCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH](design_entity.wrapped if design_entity else None), constructor.new(_5395.ClutchCompoundMultibodyDynamicsAnalysis))

    def results_for_clutch_half(self, design_entity: '_2439.ClutchHalf') -> 'Iterable[_5397.ClutchHalfCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ClutchHalfCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5397.ClutchHalfCompoundMultibodyDynamicsAnalysis))

    def results_for_concept_coupling(self, design_entity: '_2441.ConceptCoupling') -> 'Iterable[_5400.ConceptCouplingCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptCouplingCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](design_entity.wrapped if design_entity else None), constructor.new(_5400.ConceptCouplingCompoundMultibodyDynamicsAnalysis))

    def results_for_concept_coupling_half(self, design_entity: '_2442.ConceptCouplingHalf') -> 'Iterable[_5402.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5402.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis))

    def results_for_coupling(self, design_entity: '_2443.Coupling') -> 'Iterable[_5411.CouplingCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CouplingCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING](design_entity.wrapped if design_entity else None), constructor.new(_5411.CouplingCompoundMultibodyDynamicsAnalysis))

    def results_for_coupling_half(self, design_entity: '_2444.CouplingHalf') -> 'Iterable[_5413.CouplingHalfCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CouplingHalfCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5413.CouplingHalfCompoundMultibodyDynamicsAnalysis))

    def results_for_cvt(self, design_entity: '_2446.CVT') -> 'Iterable[_5415.CVTCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CVTCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT](design_entity.wrapped if design_entity else None), constructor.new(_5415.CVTCompoundMultibodyDynamicsAnalysis))

    def results_for_cvt_pulley(self, design_entity: '_2447.CVTPulley') -> 'Iterable[_5416.CVTPulleyCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CVTPulleyCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](design_entity.wrapped if design_entity else None), constructor.new(_5416.CVTPulleyCompoundMultibodyDynamicsAnalysis))

    def results_for_pulley(self, design_entity: '_2450.Pulley') -> 'Iterable[_5462.PulleyCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PulleyCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PULLEY](design_entity.wrapped if design_entity else None), constructor.new(_5462.PulleyCompoundMultibodyDynamicsAnalysis))

    def results_for_shaft_hub_connection(self, design_entity: '_2458.ShaftHubConnection') -> 'Iterable[_5470.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5470.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_rolling_ring(self, design_entity: '_2456.RollingRing') -> 'Iterable[_5466.RollingRingCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RollingRingCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING](design_entity.wrapped if design_entity else None), constructor.new(_5466.RollingRingCompoundMultibodyDynamicsAnalysis))

    def results_for_rolling_ring_assembly(self, design_entity: '_2457.RollingRingAssembly') -> 'Iterable[_5465.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5465.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis))

    def results_for_spring_damper(self, design_entity: '_2460.SpringDamper') -> 'Iterable[_5476.SpringDamperCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpringDamperCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](design_entity.wrapped if design_entity else None), constructor.new(_5476.SpringDamperCompoundMultibodyDynamicsAnalysis))

    def results_for_spring_damper_half(self, design_entity: '_2461.SpringDamperHalf') -> 'Iterable[_5478.SpringDamperHalfCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpringDamperHalfCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5478.SpringDamperHalfCompoundMultibodyDynamicsAnalysis))

    def results_for_synchroniser(self, design_entity: '_2462.Synchroniser') -> 'Iterable[_5487.SynchroniserCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](design_entity.wrapped if design_entity else None), constructor.new(_5487.SynchroniserCompoundMultibodyDynamicsAnalysis))

    def results_for_synchroniser_half(self, design_entity: '_2464.SynchroniserHalf') -> 'Iterable[_5488.SynchroniserHalfCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserHalfCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5488.SynchroniserHalfCompoundMultibodyDynamicsAnalysis))

    def results_for_synchroniser_part(self, design_entity: '_2465.SynchroniserPart') -> 'Iterable[_5489.SynchroniserPartCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserPartCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](design_entity.wrapped if design_entity else None), constructor.new(_5489.SynchroniserPartCompoundMultibodyDynamicsAnalysis))

    def results_for_synchroniser_sleeve(self, design_entity: '_2466.SynchroniserSleeve') -> 'Iterable[_5490.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](design_entity.wrapped if design_entity else None), constructor.new(_5490.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis))

    def results_for_torque_converter(self, design_entity: '_2467.TorqueConverter') -> 'Iterable[_5491.TorqueConverterCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](design_entity.wrapped if design_entity else None), constructor.new(_5491.TorqueConverterCompoundMultibodyDynamicsAnalysis))

    def results_for_torque_converter_pump(self, design_entity: '_2468.TorqueConverterPump') -> 'Iterable[_5493.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](design_entity.wrapped if design_entity else None), constructor.new(_5493.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis))

    def results_for_torque_converter_turbine(self, design_entity: '_2470.TorqueConverterTurbine') -> 'Iterable[_5494.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](design_entity.wrapped if design_entity else None), constructor.new(_5494.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_2157.ShaftToMountableComponentConnection') -> 'Iterable[_5471.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5471.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_cvt_belt_connection(self, design_entity: '_2135.CVTBeltConnection') -> 'Iterable[_5414.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5414.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_belt_connection(self, design_entity: '_2130.BeltConnection') -> 'Iterable[_5383.BeltConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BeltConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5383.BeltConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_coaxial_connection(self, design_entity: '_2131.CoaxialConnection') -> 'Iterable[_5398.CoaxialConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CoaxialConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5398.CoaxialConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_connection(self, design_entity: '_2134.Connection') -> 'Iterable[_5409.ConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5409.ConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_inter_mountable_component_connection(self, design_entity: '_2143.InterMountableComponentConnection') -> 'Iterable[_5439.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5439.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_planetary_connection(self, design_entity: '_2149.PlanetaryConnection') -> 'Iterable[_5457.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5457.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_rolling_ring_connection(self, design_entity: '_2154.RollingRingConnection') -> 'Iterable[_5467.RollingRingConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RollingRingConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5467.RollingRingConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_abstract_shaft_to_mountable_component_connection(self, design_entity: '_2127.AbstractShaftToMountableComponentConnection') -> 'Iterable[_5377.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5377.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_2163.BevelDifferentialGearMesh') -> 'Iterable[_5386.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5386.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_concept_gear_mesh(self, design_entity: '_2167.ConceptGearMesh') -> 'Iterable[_5404.ConceptGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5404.ConceptGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_face_gear_mesh(self, design_entity: '_2173.FaceGearMesh') -> 'Iterable[_5428.FaceGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5428.FaceGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_2187.StraightBevelDiffGearMesh') -> 'Iterable[_5480.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5480.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_bevel_gear_mesh(self, design_entity: '_2165.BevelGearMesh') -> 'Iterable[_5391.BevelGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5391.BevelGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_conical_gear_mesh(self, design_entity: '_2169.ConicalGearMesh') -> 'Iterable[_5407.ConicalGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConicalGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5407.ConicalGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_2161.AGMAGleasonConicalGearMesh') -> 'Iterable[_5379.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5379.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_2171.CylindricalGearMesh') -> 'Iterable[_5422.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5422.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_hypoid_gear_mesh(self, design_entity: '_2177.HypoidGearMesh') -> 'Iterable[_5437.HypoidGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.HypoidGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5437.HypoidGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_2180.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_5441.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5441.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_2181.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_5444.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5444.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_2182.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_5447.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5447.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_2185.SpiralBevelGearMesh') -> 'Iterable[_5474.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5474.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_2189.StraightBevelGearMesh') -> 'Iterable[_5483.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5483.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_worm_gear_mesh(self, design_entity: '_2191.WormGearMesh') -> 'Iterable[_5498.WormGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5498.WormGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_2193.ZerolBevelGearMesh') -> 'Iterable[_5501.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5501.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_gear_mesh(self, design_entity: '_2175.GearMesh') -> 'Iterable[_5433.GearMeshCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GearMeshCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5433.GearMeshCompoundMultibodyDynamicsAnalysis))

    def results_for_cycloidal_disc_central_bearing_connection(self, design_entity: '_2197.CycloidalDiscCentralBearingConnection') -> 'Iterable[_5418.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5418.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_cycloidal_disc_planetary_bearing_connection(self, design_entity: '_2200.CycloidalDiscPlanetaryBearingConnection') -> 'Iterable[_5420.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5420.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_ring_pins_to_disc_connection(self, design_entity: '_2203.RingPinsToDiscConnection') -> 'Iterable[_5464.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5464.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_2210.PartToPartShearCouplingConnection') -> 'Iterable[_5455.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5455.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_clutch_connection(self, design_entity: '_2204.ClutchConnection') -> 'Iterable[_5396.ClutchConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ClutchConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5396.ClutchConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_concept_coupling_connection(self, design_entity: '_2206.ConceptCouplingConnection') -> 'Iterable[_5401.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5401.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis))

    def results_for_coupling_connection(self, design_entity: '_2208.CouplingConnection') -> 'Iterable[_5412.CouplingConnectionCompoundMultibodyDynamicsAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CouplingConnectionCompoundMultibodyDynamicsAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5412.CouplingConnectionCompoundMultibodyDynamicsAnalysis))
