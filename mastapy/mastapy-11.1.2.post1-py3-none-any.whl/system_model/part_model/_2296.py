'''_2296.py

Assembly
'''


from typing import List, TypeVar, Optional

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import (
    _2326, _2306, _2302, _2305,
    _2314, _2333, _2332, _2327,
    _2329, _2297, _2298, _2299,
    _2304, _2309, _2310, _2313,
    _2315, _2316, _2323, _2324,
    _2325, _2330, _2335, _2337,
    _2338, _2340
)
from mastapy.system_model.part_model.gears import (
    _2408, _2395, _2404, _2392,
    _2386, _2384, _2389, _2412,
    _2397, _2373, _2374, _2375,
    _2376, _2377, _2378, _2379,
    _2380, _2381, _2382, _2383,
    _2385, _2387, _2388, _2390,
    _2394, _2396, _2398, _2399,
    _2400, _2401, _2402, _2403,
    _2405, _2406, _2407, _2409,
    _2410, _2411, _2413, _2414
)
from mastapy.system_model.part_model.couplings import (
    _2458, _2436, _2438, _2439,
    _2441, _2442, _2443, _2444,
    _2446, _2447, _2448, _2449,
    _2450, _2456, _2457, _2460,
    _2461, _2462, _2464, _2465,
    _2466, _2467, _2468, _2470
)
from mastapy.system_model.part_model.shaft_model import _2343
from mastapy.system_model.part_model.cycloidal import _2428, _2429, _2430
from mastapy.gears.gear_designs.creation_options import _1098, _1101
from mastapy.system_model.part_model.creation_options import (
    _2433, _2432, _2431, _2434,
    _2435
)
from mastapy._internal.python_net import python_net_import
from mastapy.gears import _304
from mastapy.gears.gear_designs.bevel import _1131
from mastapy.bearings import _1747, _1772
from mastapy.nodal_analysis import _74

_ARRAY = python_net_import('System', 'Array')
_DOUBLE = python_net_import('System', 'Double')
_STRING = python_net_import('System', 'String')
_INT_32 = python_net_import('System', 'Int32')
_SHAFT_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'ShaftCreationOptions')
_CYLINDRICAL_GEAR_LINEAR_TRAIN_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'CylindricalGearLinearTrainCreationOptions')
_CYCLOIDAL_ASSEMBLY_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'CycloidalAssemblyCreationOptions')
_BELT_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'BeltCreationOptions')
_PLANET_CARRIER_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'PlanetCarrierCreationOptions')
_CYLINDRICAL_GEAR_PAIR_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.CreationOptions', 'CylindricalGearPairCreationOptions')
_SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.CreationOptions', 'SpiralBevelGearSetCreationOptions')
_HAND = python_net_import('SMT.MastaAPI.Gears', 'Hand')
_AGMA_GLEASON_CONICAL_GEAR_GEOMETRY_METHODS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Bevel', 'AGMAGleasonConicalGearGeometryMethods')
_ROLLING_BEARING_TYPE = python_net_import('SMT.MastaAPI.Bearings', 'RollingBearingType')
_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Assembly')


__docformat__ = 'restructuredtext en'
__all__ = ('Assembly',)


class Assembly(_2297.AbstractAssembly):
    '''Assembly

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Assembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width_of_widest_cylindrical_gear(self) -> 'float':
        '''float: 'FaceWidthOfWidestCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FaceWidthOfWidestCylindricalGear

    @property
    def mass_of_gears(self) -> 'float':
        '''float: 'MassOfGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MassOfGears

    @property
    def mass_of_bearings(self) -> 'float':
        '''float: 'MassOfBearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MassOfBearings

    @property
    def mass_of_shafts(self) -> 'float':
        '''float: 'MassOfShafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MassOfShafts

    @property
    def mass_of_fe_part_shafts(self) -> 'float':
        '''float: 'MassOfFEPartShafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MassOfFEPartShafts

    @property
    def mass_of_fe_part_housings(self) -> 'float':
        '''float: 'MassOfFEPartHousings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MassOfFEPartHousings

    @property
    def mass_of_other_parts(self) -> 'float':
        '''float: 'MassOfOtherParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MassOfOtherParts

    @property
    def smallest_number_of_teeth(self) -> 'int':
        '''int: 'SmallestNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SmallestNumberOfTeeth

    @property
    def largest_number_of_teeth(self) -> 'int':
        '''int: 'LargestNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LargestNumberOfTeeth

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self) -> 'float':
        '''float: 'TransverseAndAxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TransverseAndAxialContactRatioRatingForNVH

    @property
    def transverse_contact_ratio_rating_for_nvh(self) -> 'float':
        '''float: 'TransverseContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TransverseContactRatioRatingForNVH

    @property
    def axial_contact_ratio_rating_for_nvh(self) -> 'float':
        '''float: 'AxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AxialContactRatioRatingForNVH

    @property
    def minimum_tip_thickness(self) -> 'float':
        '''float: 'MinimumTipThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MinimumTipThickness

    @property
    def oil_level_specification(self) -> '_2326.OilLevelSpecification':
        '''OilLevelSpecification: 'OilLevelSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2326.OilLevelSpecification)(self.wrapped.OilLevelSpecification) if self.wrapped.OilLevelSpecification is not None else None

    @property
    def components_with_unknown_scalar_mass(self) -> 'List[_2306.Component]':
        '''List[Component]: 'ComponentsWithUnknownScalarMass' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentsWithUnknownScalarMass, constructor.new(_2306.Component))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_2408.StraightBevelGearSet]':
        '''List[StraightBevelGearSet]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_2408.StraightBevelGearSet))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_2395.HypoidGearSet]':
        '''List[HypoidGearSet]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_2395.HypoidGearSet))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_2404.SpiralBevelGearSet]':
        '''List[SpiralBevelGearSet]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_2404.SpiralBevelGearSet))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_2458.ShaftHubConnection]':
        '''List[ShaftHubConnection]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_2458.ShaftHubConnection))
        return value

    @property
    def gear_sets(self) -> 'List[_2392.GearSet]':
        '''List[GearSet]: 'GearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearSets, constructor.new(_2392.GearSet))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_2386.CylindricalGearSet]':
        '''List[CylindricalGearSet]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_2386.CylindricalGearSet))
        return value

    @property
    def conical_gear_sets(self) -> 'List[_2384.ConicalGearSet]':
        '''List[ConicalGearSet]: 'ConicalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConicalGearSets, constructor.new(_2384.ConicalGearSet))
        return value

    @property
    def face_gear_sets(self) -> 'List[_2389.FaceGearSet]':
        '''List[FaceGearSet]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_2389.FaceGearSet))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_2412.WormGearSet]':
        '''List[WormGearSet]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_2412.WormGearSet))
        return value

    @property
    def klingelnberg_cyclo_palloid_gear_sets(self) -> 'List[_2397.KlingelnbergCycloPalloidConicalGearSet]':
        '''List[KlingelnbergCycloPalloidConicalGearSet]: 'KlingelnbergCycloPalloidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidGearSets, constructor.new(_2397.KlingelnbergCycloPalloidConicalGearSet))
        return value

    @property
    def shafts(self) -> 'List[_2343.Shaft]':
        '''List[Shaft]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_2343.Shaft))
        return value

    @property
    def bearings(self) -> 'List[_2302.Bearing]':
        '''List[Bearing]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_2302.Bearing))
        return value

    @property
    def bolted_joints(self) -> 'List[_2305.BoltedJoint]':
        '''List[BoltedJoint]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_2305.BoltedJoint))
        return value

    @property
    def fe_parts(self) -> 'List[_2314.FEPart]':
        '''List[FEPart]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_2314.FEPart))
        return value

    @property
    def component_details(self) -> 'List[_2306.Component]':
        '''List[Component]: 'ComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentDetails, constructor.new(_2306.Component))
        return value

    @property
    def power_loads(self) -> 'List[_2333.PowerLoad]':
        '''List[PowerLoad]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_2333.PowerLoad))
        return value

    @property
    def point_loads(self) -> 'List[_2332.PointLoad]':
        '''List[PointLoad]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_2332.PointLoad))
        return value

    @property
    def oil_seals(self) -> 'List[_2327.OilSeal]':
        '''List[OilSeal]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_2327.OilSeal))
        return value

    def get_part_named(self, name: 'str') -> '_2329.Part':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Part
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2329.Part.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_assembly(self, name: 'str') -> 'Assembly':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Assembly
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[Assembly.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_abstract_assembly(self, name: 'str') -> '_2297.AbstractAssembly':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.AbstractAssembly
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2297.AbstractAssembly.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_abstract_shaft(self, name: 'str') -> '_2298.AbstractShaft':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.AbstractShaft
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2298.AbstractShaft.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_abstract_shaft_or_housing(self, name: 'str') -> '_2299.AbstractShaftOrHousing':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.AbstractShaftOrHousing
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2299.AbstractShaftOrHousing.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_bearing(self, name: 'str') -> '_2302.Bearing':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2302.Bearing.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_bolt(self, name: 'str') -> '_2304.Bolt':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Bolt
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2304.Bolt.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_bolted_joint(self, name: 'str') -> '_2305.BoltedJoint':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.BoltedJoint
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2305.BoltedJoint.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_component(self, name: 'str') -> '_2306.Component':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Component
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2306.Component.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_connector(self, name: 'str') -> '_2309.Connector':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Connector
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2309.Connector.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_datum(self, name: 'str') -> '_2310.Datum':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Datum
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2310.Datum.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_external_cad_model(self, name: 'str') -> '_2313.ExternalCADModel':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.ExternalCADModel
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2313.ExternalCADModel.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_fe_part(self, name: 'str') -> '_2314.FEPart':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.FEPart
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2314.FEPart.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_flexible_pin_assembly(self, name: 'str') -> '_2315.FlexiblePinAssembly':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.FlexiblePinAssembly
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2315.FlexiblePinAssembly.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_guide_dxf_model(self, name: 'str') -> '_2316.GuideDxfModel':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.GuideDxfModel
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2316.GuideDxfModel.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_mass_disc(self, name: 'str') -> '_2323.MassDisc':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.MassDisc
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2323.MassDisc.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_measurement_component(self, name: 'str') -> '_2324.MeasurementComponent':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.MeasurementComponent
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2324.MeasurementComponent.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_mountable_component(self, name: 'str') -> '_2325.MountableComponent':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.MountableComponent
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2325.MountableComponent.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_oil_seal(self, name: 'str') -> '_2327.OilSeal':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.OilSeal
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2327.OilSeal.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_planet_carrier(self, name: 'str') -> '_2330.PlanetCarrier':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.PlanetCarrier
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2330.PlanetCarrier.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_point_load(self, name: 'str') -> '_2332.PointLoad':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.PointLoad
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2332.PointLoad.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_power_load(self, name: 'str') -> '_2333.PowerLoad':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.PowerLoad
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2333.PowerLoad.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_root_assembly(self, name: 'str') -> '_2335.RootAssembly':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.RootAssembly
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2335.RootAssembly.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_specialised_assembly(self, name: 'str') -> '_2337.SpecialisedAssembly':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.SpecialisedAssembly
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2337.SpecialisedAssembly.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_unbalanced_mass(self, name: 'str') -> '_2338.UnbalancedMass':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.UnbalancedMass
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2338.UnbalancedMass.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_virtual_component(self, name: 'str') -> '_2340.VirtualComponent':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.VirtualComponent
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2340.VirtualComponent.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_shaft(self, name: 'str') -> '_2343.Shaft':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.shaft_model.Shaft
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2343.Shaft.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_agma_gleason_conical_gear(self, name: 'str') -> '_2373.AGMAGleasonConicalGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.AGMAGleasonConicalGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2373.AGMAGleasonConicalGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_agma_gleason_conical_gear_set(self, name: 'str') -> '_2374.AGMAGleasonConicalGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2374.AGMAGleasonConicalGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_gear(self, name: 'str') -> '_2375.BevelDifferentialGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2375.BevelDifferentialGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_gear_set(self, name: 'str') -> '_2376.BevelDifferentialGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2376.BevelDifferentialGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_planet_gear(self, name: 'str') -> '_2377.BevelDifferentialPlanetGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2377.BevelDifferentialPlanetGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_sun_gear(self, name: 'str') -> '_2378.BevelDifferentialSunGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialSunGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2378.BevelDifferentialSunGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_gear(self, name: 'str') -> '_2379.BevelGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2379.BevelGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_gear_set(self, name: 'str') -> '_2380.BevelGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2380.BevelGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_gear(self, name: 'str') -> '_2381.ConceptGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ConceptGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2381.ConceptGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_gear_set(self, name: 'str') -> '_2382.ConceptGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ConceptGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2382.ConceptGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_conical_gear(self, name: 'str') -> '_2383.ConicalGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ConicalGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2383.ConicalGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_conical_gear_set(self, name: 'str') -> '_2384.ConicalGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ConicalGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2384.ConicalGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_cylindrical_gear(self, name: 'str') -> '_2385.CylindricalGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2385.CylindricalGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_cylindrical_gear_set(self, name: 'str') -> '_2386.CylindricalGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2386.CylindricalGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_cylindrical_planet_gear(self, name: 'str') -> '_2387.CylindricalPlanetGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalPlanetGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2387.CylindricalPlanetGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_face_gear(self, name: 'str') -> '_2388.FaceGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.FaceGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2388.FaceGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_face_gear_set(self, name: 'str') -> '_2389.FaceGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.FaceGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2389.FaceGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_gear(self, name: 'str') -> '_2390.Gear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.Gear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2390.Gear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_gear_set(self, name: 'str') -> '_2392.GearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.GearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2392.GearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_hypoid_gear(self, name: 'str') -> '_2394.HypoidGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.HypoidGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2394.HypoidGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_hypoid_gear_set(self, name: 'str') -> '_2395.HypoidGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.HypoidGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2395.HypoidGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_conical_gear(self, name: 'str') -> '_2396.KlingelnbergCycloPalloidConicalGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2396.KlingelnbergCycloPalloidConicalGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self, name: 'str') -> '_2397.KlingelnbergCycloPalloidConicalGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2397.KlingelnbergCycloPalloidConicalGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self, name: 'str') -> '_2398.KlingelnbergCycloPalloidHypoidGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2398.KlingelnbergCycloPalloidHypoidGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self, name: 'str') -> '_2399.KlingelnbergCycloPalloidHypoidGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2399.KlingelnbergCycloPalloidHypoidGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, name: 'str') -> '_2400.KlingelnbergCycloPalloidSpiralBevelGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2400.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, name: 'str') -> '_2401.KlingelnbergCycloPalloidSpiralBevelGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2401.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_planetary_gear_set(self, name: 'str') -> '_2402.PlanetaryGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.PlanetaryGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2402.PlanetaryGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_spiral_bevel_gear(self, name: 'str') -> '_2403.SpiralBevelGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2403.SpiralBevelGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_spiral_bevel_gear_set(self, name: 'str') -> '_2404.SpiralBevelGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2404.SpiralBevelGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_diff_gear(self, name: 'str') -> '_2405.StraightBevelDiffGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelDiffGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2405.StraightBevelDiffGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_diff_gear_set(self, name: 'str') -> '_2406.StraightBevelDiffGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelDiffGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2406.StraightBevelDiffGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_gear(self, name: 'str') -> '_2407.StraightBevelGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2407.StraightBevelGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_gear_set(self, name: 'str') -> '_2408.StraightBevelGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2408.StraightBevelGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_planet_gear(self, name: 'str') -> '_2409.StraightBevelPlanetGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelPlanetGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2409.StraightBevelPlanetGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_sun_gear(self, name: 'str') -> '_2410.StraightBevelSunGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelSunGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2410.StraightBevelSunGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_worm_gear(self, name: 'str') -> '_2411.WormGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.WormGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2411.WormGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_worm_gear_set(self, name: 'str') -> '_2412.WormGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.WormGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2412.WormGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_zerol_bevel_gear(self, name: 'str') -> '_2413.ZerolBevelGear':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ZerolBevelGear
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2413.ZerolBevelGear.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_zerol_bevel_gear_set(self, name: 'str') -> '_2414.ZerolBevelGearSet':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ZerolBevelGearSet
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2414.ZerolBevelGearSet.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_cycloidal_assembly(self, name: 'str') -> '_2428.CycloidalAssembly':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalAssembly
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2428.CycloidalAssembly.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_cycloidal_disc(self, name: 'str') -> '_2429.CycloidalDisc':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalDisc
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2429.CycloidalDisc.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_ring_pins(self, name: 'str') -> '_2430.RingPins':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.cycloidal.RingPins
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2430.RingPins.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_belt_drive(self, name: 'str') -> '_2436.BeltDrive':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.BeltDrive
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2436.BeltDrive.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_clutch(self, name: 'str') -> '_2438.Clutch':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.Clutch
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2438.Clutch.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_clutch_half(self, name: 'str') -> '_2439.ClutchHalf':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ClutchHalf
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2439.ClutchHalf.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_coupling(self, name: 'str') -> '_2441.ConceptCoupling':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ConceptCoupling
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2441.ConceptCoupling.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_coupling_half(self, name: 'str') -> '_2442.ConceptCouplingHalf':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ConceptCouplingHalf
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2442.ConceptCouplingHalf.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_coupling(self, name: 'str') -> '_2443.Coupling':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.Coupling
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2443.Coupling.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_coupling_half(self, name: 'str') -> '_2444.CouplingHalf':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.CouplingHalf
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2444.CouplingHalf.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_cvt(self, name: 'str') -> '_2446.CVT':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.CVT
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2446.CVT.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_cvt_pulley(self, name: 'str') -> '_2447.CVTPulley':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.CVTPulley
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2447.CVTPulley.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_part_to_part_shear_coupling(self, name: 'str') -> '_2448.PartToPartShearCoupling':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.PartToPartShearCoupling
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2448.PartToPartShearCoupling.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_part_to_part_shear_coupling_half(self, name: 'str') -> '_2449.PartToPartShearCouplingHalf':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2449.PartToPartShearCouplingHalf.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_pulley(self, name: 'str') -> '_2450.Pulley':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.Pulley
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2450.Pulley.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_rolling_ring(self, name: 'str') -> '_2456.RollingRing':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.RollingRing
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2456.RollingRing.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_rolling_ring_assembly(self, name: 'str') -> '_2457.RollingRingAssembly':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.RollingRingAssembly
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2457.RollingRingAssembly.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_shaft_hub_connection(self, name: 'str') -> '_2458.ShaftHubConnection':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ShaftHubConnection
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2458.ShaftHubConnection.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_spring_damper(self, name: 'str') -> '_2460.SpringDamper':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.SpringDamper
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2460.SpringDamper.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_spring_damper_half(self, name: 'str') -> '_2461.SpringDamperHalf':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.SpringDamperHalf
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2461.SpringDamperHalf.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser(self, name: 'str') -> '_2462.Synchroniser':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.Synchroniser
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2462.Synchroniser.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser_half(self, name: 'str') -> '_2464.SynchroniserHalf':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.SynchroniserHalf
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2464.SynchroniserHalf.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser_part(self, name: 'str') -> '_2465.SynchroniserPart':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.SynchroniserPart
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2465.SynchroniserPart.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser_sleeve(self, name: 'str') -> '_2466.SynchroniserSleeve':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.SynchroniserSleeve
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2466.SynchroniserSleeve.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_torque_converter(self, name: 'str') -> '_2467.TorqueConverter':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.TorqueConverter
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2467.TorqueConverter.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_torque_converter_pump(self, name: 'str') -> '_2468.TorqueConverterPump':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.TorqueConverterPump
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2468.TorqueConverterPump.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def get_part_named_of_type_torque_converter_turbine(self, name: 'str') -> '_2470.TorqueConverterTurbine':
        ''' 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.TorqueConverterTurbine
        '''

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2470.TorqueConverterTurbine.TYPE](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_part(self, part_type: 'Assembly.PartType', name: 'str') -> '_2329.Part':
        ''' 'AddPart' is the original name of this method.

        Args:
            part_type (mastapy.system_model.part_model.Assembly.PartType)
            name (str)

        Returns:
            mastapy.system_model.part_model.Part
        '''

        part_type = conversion.mp_to_pn_enum(part_type)
        name = str(name)
        method_result = self.wrapped.AddPart(part_type, name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def all_parts(self) -> 'List[_2329.Part]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Part]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2329.Part.TYPE](), constructor.new(_2329.Part))

    def all_parts_of_type_assembly(self) -> 'List[Assembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Assembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[Assembly.TYPE](), constructor.new(Assembly))

    def all_parts_of_type_abstract_assembly(self) -> 'List[_2297.AbstractAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2297.AbstractAssembly.TYPE](), constructor.new(_2297.AbstractAssembly))

    def all_parts_of_type_abstract_shaft(self) -> 'List[_2298.AbstractShaft]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaft]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2298.AbstractShaft.TYPE](), constructor.new(_2298.AbstractShaft))

    def all_parts_of_type_abstract_shaft_or_housing(self) -> 'List[_2299.AbstractShaftOrHousing]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaftOrHousing]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2299.AbstractShaftOrHousing.TYPE](), constructor.new(_2299.AbstractShaftOrHousing))

    def all_parts_of_type_bearing(self) -> 'List[_2302.Bearing]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bearing]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2302.Bearing.TYPE](), constructor.new(_2302.Bearing))

    def all_parts_of_type_bolt(self) -> 'List[_2304.Bolt]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bolt]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2304.Bolt.TYPE](), constructor.new(_2304.Bolt))

    def all_parts_of_type_bolted_joint(self) -> 'List[_2305.BoltedJoint]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.BoltedJoint]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2305.BoltedJoint.TYPE](), constructor.new(_2305.BoltedJoint))

    def all_parts_of_type_component(self) -> 'List[_2306.Component]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Component]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2306.Component.TYPE](), constructor.new(_2306.Component))

    def all_parts_of_type_connector(self) -> 'List[_2309.Connector]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Connector]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2309.Connector.TYPE](), constructor.new(_2309.Connector))

    def all_parts_of_type_datum(self) -> 'List[_2310.Datum]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Datum]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2310.Datum.TYPE](), constructor.new(_2310.Datum))

    def all_parts_of_type_external_cad_model(self) -> 'List[_2313.ExternalCADModel]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.ExternalCADModel]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2313.ExternalCADModel.TYPE](), constructor.new(_2313.ExternalCADModel))

    def all_parts_of_type_fe_part(self) -> 'List[_2314.FEPart]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FEPart]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2314.FEPart.TYPE](), constructor.new(_2314.FEPart))

    def all_parts_of_type_flexible_pin_assembly(self) -> 'List[_2315.FlexiblePinAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FlexiblePinAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2315.FlexiblePinAssembly.TYPE](), constructor.new(_2315.FlexiblePinAssembly))

    def all_parts_of_type_guide_dxf_model(self) -> 'List[_2316.GuideDxfModel]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.GuideDxfModel]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2316.GuideDxfModel.TYPE](), constructor.new(_2316.GuideDxfModel))

    def all_parts_of_type_mass_disc(self) -> 'List[_2323.MassDisc]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MassDisc]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2323.MassDisc.TYPE](), constructor.new(_2323.MassDisc))

    def all_parts_of_type_measurement_component(self) -> 'List[_2324.MeasurementComponent]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MeasurementComponent]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2324.MeasurementComponent.TYPE](), constructor.new(_2324.MeasurementComponent))

    def all_parts_of_type_mountable_component(self) -> 'List[_2325.MountableComponent]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MountableComponent]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2325.MountableComponent.TYPE](), constructor.new(_2325.MountableComponent))

    def all_parts_of_type_oil_seal(self) -> 'List[_2327.OilSeal]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.OilSeal]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2327.OilSeal.TYPE](), constructor.new(_2327.OilSeal))

    def all_parts_of_type_planet_carrier(self) -> 'List[_2330.PlanetCarrier]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PlanetCarrier]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2330.PlanetCarrier.TYPE](), constructor.new(_2330.PlanetCarrier))

    def all_parts_of_type_point_load(self) -> 'List[_2332.PointLoad]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PointLoad]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2332.PointLoad.TYPE](), constructor.new(_2332.PointLoad))

    def all_parts_of_type_power_load(self) -> 'List[_2333.PowerLoad]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PowerLoad]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2333.PowerLoad.TYPE](), constructor.new(_2333.PowerLoad))

    def all_parts_of_type_root_assembly(self) -> 'List[_2335.RootAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.RootAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2335.RootAssembly.TYPE](), constructor.new(_2335.RootAssembly))

    def all_parts_of_type_specialised_assembly(self) -> 'List[_2337.SpecialisedAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.SpecialisedAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2337.SpecialisedAssembly.TYPE](), constructor.new(_2337.SpecialisedAssembly))

    def all_parts_of_type_unbalanced_mass(self) -> 'List[_2338.UnbalancedMass]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.UnbalancedMass]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2338.UnbalancedMass.TYPE](), constructor.new(_2338.UnbalancedMass))

    def all_parts_of_type_virtual_component(self) -> 'List[_2340.VirtualComponent]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.VirtualComponent]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2340.VirtualComponent.TYPE](), constructor.new(_2340.VirtualComponent))

    def all_parts_of_type_shaft(self) -> 'List[_2343.Shaft]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.shaft_model.Shaft]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2343.Shaft.TYPE](), constructor.new(_2343.Shaft))

    def all_parts_of_type_agma_gleason_conical_gear(self) -> 'List[_2373.AGMAGleasonConicalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2373.AGMAGleasonConicalGear.TYPE](), constructor.new(_2373.AGMAGleasonConicalGear))

    def all_parts_of_type_agma_gleason_conical_gear_set(self) -> 'List[_2374.AGMAGleasonConicalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2374.AGMAGleasonConicalGearSet.TYPE](), constructor.new(_2374.AGMAGleasonConicalGearSet))

    def all_parts_of_type_bevel_differential_gear(self) -> 'List[_2375.BevelDifferentialGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2375.BevelDifferentialGear.TYPE](), constructor.new(_2375.BevelDifferentialGear))

    def all_parts_of_type_bevel_differential_gear_set(self) -> 'List[_2376.BevelDifferentialGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2376.BevelDifferentialGearSet.TYPE](), constructor.new(_2376.BevelDifferentialGearSet))

    def all_parts_of_type_bevel_differential_planet_gear(self) -> 'List[_2377.BevelDifferentialPlanetGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2377.BevelDifferentialPlanetGear.TYPE](), constructor.new(_2377.BevelDifferentialPlanetGear))

    def all_parts_of_type_bevel_differential_sun_gear(self) -> 'List[_2378.BevelDifferentialSunGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialSunGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2378.BevelDifferentialSunGear.TYPE](), constructor.new(_2378.BevelDifferentialSunGear))

    def all_parts_of_type_bevel_gear(self) -> 'List[_2379.BevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2379.BevelGear.TYPE](), constructor.new(_2379.BevelGear))

    def all_parts_of_type_bevel_gear_set(self) -> 'List[_2380.BevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2380.BevelGearSet.TYPE](), constructor.new(_2380.BevelGearSet))

    def all_parts_of_type_concept_gear(self) -> 'List[_2381.ConceptGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2381.ConceptGear.TYPE](), constructor.new(_2381.ConceptGear))

    def all_parts_of_type_concept_gear_set(self) -> 'List[_2382.ConceptGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2382.ConceptGearSet.TYPE](), constructor.new(_2382.ConceptGearSet))

    def all_parts_of_type_conical_gear(self) -> 'List[_2383.ConicalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2383.ConicalGear.TYPE](), constructor.new(_2383.ConicalGear))

    def all_parts_of_type_conical_gear_set(self) -> 'List[_2384.ConicalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2384.ConicalGearSet.TYPE](), constructor.new(_2384.ConicalGearSet))

    def all_parts_of_type_cylindrical_gear(self) -> 'List[_2385.CylindricalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2385.CylindricalGear.TYPE](), constructor.new(_2385.CylindricalGear))

    def all_parts_of_type_cylindrical_gear_set(self) -> 'List[_2386.CylindricalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2386.CylindricalGearSet.TYPE](), constructor.new(_2386.CylindricalGearSet))

    def all_parts_of_type_cylindrical_planet_gear(self) -> 'List[_2387.CylindricalPlanetGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalPlanetGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2387.CylindricalPlanetGear.TYPE](), constructor.new(_2387.CylindricalPlanetGear))

    def all_parts_of_type_face_gear(self) -> 'List[_2388.FaceGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2388.FaceGear.TYPE](), constructor.new(_2388.FaceGear))

    def all_parts_of_type_face_gear_set(self) -> 'List[_2389.FaceGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2389.FaceGearSet.TYPE](), constructor.new(_2389.FaceGearSet))

    def all_parts_of_type_gear(self) -> 'List[_2390.Gear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.Gear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2390.Gear.TYPE](), constructor.new(_2390.Gear))

    def all_parts_of_type_gear_set(self) -> 'List[_2392.GearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.GearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2392.GearSet.TYPE](), constructor.new(_2392.GearSet))

    def all_parts_of_type_hypoid_gear(self) -> 'List[_2394.HypoidGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2394.HypoidGear.TYPE](), constructor.new(_2394.HypoidGear))

    def all_parts_of_type_hypoid_gear_set(self) -> 'List[_2395.HypoidGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2395.HypoidGearSet.TYPE](), constructor.new(_2395.HypoidGearSet))

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> 'List[_2396.KlingelnbergCycloPalloidConicalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2396.KlingelnbergCycloPalloidConicalGear.TYPE](), constructor.new(_2396.KlingelnbergCycloPalloidConicalGear))

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> 'List[_2397.KlingelnbergCycloPalloidConicalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2397.KlingelnbergCycloPalloidConicalGearSet.TYPE](), constructor.new(_2397.KlingelnbergCycloPalloidConicalGearSet))

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> 'List[_2398.KlingelnbergCycloPalloidHypoidGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2398.KlingelnbergCycloPalloidHypoidGear.TYPE](), constructor.new(_2398.KlingelnbergCycloPalloidHypoidGear))

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> 'List[_2399.KlingelnbergCycloPalloidHypoidGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2399.KlingelnbergCycloPalloidHypoidGearSet.TYPE](), constructor.new(_2399.KlingelnbergCycloPalloidHypoidGearSet))

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> 'List[_2400.KlingelnbergCycloPalloidSpiralBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2400.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](), constructor.new(_2400.KlingelnbergCycloPalloidSpiralBevelGear))

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> 'List[_2401.KlingelnbergCycloPalloidSpiralBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2401.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](), constructor.new(_2401.KlingelnbergCycloPalloidSpiralBevelGearSet))

    def all_parts_of_type_planetary_gear_set(self) -> 'List[_2402.PlanetaryGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.PlanetaryGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2402.PlanetaryGearSet.TYPE](), constructor.new(_2402.PlanetaryGearSet))

    def all_parts_of_type_spiral_bevel_gear(self) -> 'List[_2403.SpiralBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2403.SpiralBevelGear.TYPE](), constructor.new(_2403.SpiralBevelGear))

    def all_parts_of_type_spiral_bevel_gear_set(self) -> 'List[_2404.SpiralBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2404.SpiralBevelGearSet.TYPE](), constructor.new(_2404.SpiralBevelGearSet))

    def all_parts_of_type_straight_bevel_diff_gear(self) -> 'List[_2405.StraightBevelDiffGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2405.StraightBevelDiffGear.TYPE](), constructor.new(_2405.StraightBevelDiffGear))

    def all_parts_of_type_straight_bevel_diff_gear_set(self) -> 'List[_2406.StraightBevelDiffGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2406.StraightBevelDiffGearSet.TYPE](), constructor.new(_2406.StraightBevelDiffGearSet))

    def all_parts_of_type_straight_bevel_gear(self) -> 'List[_2407.StraightBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2407.StraightBevelGear.TYPE](), constructor.new(_2407.StraightBevelGear))

    def all_parts_of_type_straight_bevel_gear_set(self) -> 'List[_2408.StraightBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2408.StraightBevelGearSet.TYPE](), constructor.new(_2408.StraightBevelGearSet))

    def all_parts_of_type_straight_bevel_planet_gear(self) -> 'List[_2409.StraightBevelPlanetGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelPlanetGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2409.StraightBevelPlanetGear.TYPE](), constructor.new(_2409.StraightBevelPlanetGear))

    def all_parts_of_type_straight_bevel_sun_gear(self) -> 'List[_2410.StraightBevelSunGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelSunGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2410.StraightBevelSunGear.TYPE](), constructor.new(_2410.StraightBevelSunGear))

    def all_parts_of_type_worm_gear(self) -> 'List[_2411.WormGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2411.WormGear.TYPE](), constructor.new(_2411.WormGear))

    def all_parts_of_type_worm_gear_set(self) -> 'List[_2412.WormGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2412.WormGearSet.TYPE](), constructor.new(_2412.WormGearSet))

    def all_parts_of_type_zerol_bevel_gear(self) -> 'List[_2413.ZerolBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2413.ZerolBevelGear.TYPE](), constructor.new(_2413.ZerolBevelGear))

    def all_parts_of_type_zerol_bevel_gear_set(self) -> 'List[_2414.ZerolBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2414.ZerolBevelGearSet.TYPE](), constructor.new(_2414.ZerolBevelGearSet))

    def all_parts_of_type_cycloidal_assembly(self) -> 'List[_2428.CycloidalAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2428.CycloidalAssembly.TYPE](), constructor.new(_2428.CycloidalAssembly))

    def all_parts_of_type_cycloidal_disc(self) -> 'List[_2429.CycloidalDisc]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalDisc]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2429.CycloidalDisc.TYPE](), constructor.new(_2429.CycloidalDisc))

    def all_parts_of_type_ring_pins(self) -> 'List[_2430.RingPins]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.RingPins]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2430.RingPins.TYPE](), constructor.new(_2430.RingPins))

    def all_parts_of_type_belt_drive(self) -> 'List[_2436.BeltDrive]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.BeltDrive]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2436.BeltDrive.TYPE](), constructor.new(_2436.BeltDrive))

    def all_parts_of_type_clutch(self) -> 'List[_2438.Clutch]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Clutch]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2438.Clutch.TYPE](), constructor.new(_2438.Clutch))

    def all_parts_of_type_clutch_half(self) -> 'List[_2439.ClutchHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ClutchHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2439.ClutchHalf.TYPE](), constructor.new(_2439.ClutchHalf))

    def all_parts_of_type_concept_coupling(self) -> 'List[_2441.ConceptCoupling]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCoupling]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2441.ConceptCoupling.TYPE](), constructor.new(_2441.ConceptCoupling))

    def all_parts_of_type_concept_coupling_half(self) -> 'List[_2442.ConceptCouplingHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCouplingHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2442.ConceptCouplingHalf.TYPE](), constructor.new(_2442.ConceptCouplingHalf))

    def all_parts_of_type_coupling(self) -> 'List[_2443.Coupling]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Coupling]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2443.Coupling.TYPE](), constructor.new(_2443.Coupling))

    def all_parts_of_type_coupling_half(self) -> 'List[_2444.CouplingHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CouplingHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2444.CouplingHalf.TYPE](), constructor.new(_2444.CouplingHalf))

    def all_parts_of_type_cvt(self) -> 'List[_2446.CVT]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVT]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2446.CVT.TYPE](), constructor.new(_2446.CVT))

    def all_parts_of_type_cvt_pulley(self) -> 'List[_2447.CVTPulley]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVTPulley]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2447.CVTPulley.TYPE](), constructor.new(_2447.CVTPulley))

    def all_parts_of_type_part_to_part_shear_coupling(self) -> 'List[_2448.PartToPartShearCoupling]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCoupling]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2448.PartToPartShearCoupling.TYPE](), constructor.new(_2448.PartToPartShearCoupling))

    def all_parts_of_type_part_to_part_shear_coupling_half(self) -> 'List[_2449.PartToPartShearCouplingHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2449.PartToPartShearCouplingHalf.TYPE](), constructor.new(_2449.PartToPartShearCouplingHalf))

    def all_parts_of_type_pulley(self) -> 'List[_2450.Pulley]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Pulley]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2450.Pulley.TYPE](), constructor.new(_2450.Pulley))

    def all_parts_of_type_rolling_ring(self) -> 'List[_2456.RollingRing]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRing]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2456.RollingRing.TYPE](), constructor.new(_2456.RollingRing))

    def all_parts_of_type_rolling_ring_assembly(self) -> 'List[_2457.RollingRingAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRingAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2457.RollingRingAssembly.TYPE](), constructor.new(_2457.RollingRingAssembly))

    def all_parts_of_type_shaft_hub_connection(self) -> 'List[_2458.ShaftHubConnection]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ShaftHubConnection]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2458.ShaftHubConnection.TYPE](), constructor.new(_2458.ShaftHubConnection))

    def all_parts_of_type_spring_damper(self) -> 'List[_2460.SpringDamper]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamper]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2460.SpringDamper.TYPE](), constructor.new(_2460.SpringDamper))

    def all_parts_of_type_spring_damper_half(self) -> 'List[_2461.SpringDamperHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamperHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2461.SpringDamperHalf.TYPE](), constructor.new(_2461.SpringDamperHalf))

    def all_parts_of_type_synchroniser(self) -> 'List[_2462.Synchroniser]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Synchroniser]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2462.Synchroniser.TYPE](), constructor.new(_2462.Synchroniser))

    def all_parts_of_type_synchroniser_half(self) -> 'List[_2464.SynchroniserHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2464.SynchroniserHalf.TYPE](), constructor.new(_2464.SynchroniserHalf))

    def all_parts_of_type_synchroniser_part(self) -> 'List[_2465.SynchroniserPart]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserPart]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2465.SynchroniserPart.TYPE](), constructor.new(_2465.SynchroniserPart))

    def all_parts_of_type_synchroniser_sleeve(self) -> 'List[_2466.SynchroniserSleeve]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserSleeve]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2466.SynchroniserSleeve.TYPE](), constructor.new(_2466.SynchroniserSleeve))

    def all_parts_of_type_torque_converter(self) -> 'List[_2467.TorqueConverter]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverter]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2467.TorqueConverter.TYPE](), constructor.new(_2467.TorqueConverter))

    def all_parts_of_type_torque_converter_pump(self) -> 'List[_2468.TorqueConverterPump]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterPump]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2468.TorqueConverterPump.TYPE](), constructor.new(_2468.TorqueConverterPump))

    def all_parts_of_type_torque_converter_turbine(self) -> 'List[_2470.TorqueConverterTurbine]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterTurbine]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2470.TorqueConverterTurbine.TYPE](), constructor.new(_2470.TorqueConverterTurbine))

    def add_shaft(self, length: Optional['float'] = 0.1, outer_diameter: Optional['float'] = 0.025, bore: Optional['float'] = 0.0, name: Optional['str'] = 'Shaft') -> '_2343.Shaft':
        ''' 'AddShaft' is the original name of this method.

        Args:
            length (float, optional)
            outer_diameter (float, optional)
            bore (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.shaft_model.Shaft
        '''

        length = float(length)
        outer_diameter = float(outer_diameter)
        bore = float(bore)
        name = str(name)
        method_result = self.wrapped.AddShaft.Overloads[_DOUBLE, _DOUBLE, _DOUBLE, _STRING](length if length else 0.0, outer_diameter if outer_diameter else 0.0, bore if bore else 0.0, name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_cylindrical_gear_pair_with_options(self, cylindrical_gear_pair_creation_options: Optional['_1098.CylindricalGearPairCreationOptions'] = None) -> '_2386.CylindricalGearSet':
        ''' 'AddCylindricalGearPair' is the original name of this method.

        Args:
            cylindrical_gear_pair_creation_options (mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        '''

        method_result = self.wrapped.AddCylindricalGearPair.Overloads[_CYLINDRICAL_GEAR_PAIR_CREATION_OPTIONS](cylindrical_gear_pair_creation_options.wrapped if cylindrical_gear_pair_creation_options else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_cylindrical_gear_pair(self, centre_distance: 'float') -> '_2386.CylindricalGearSet':
        ''' 'AddCylindricalGearPair' is the original name of this method.

        Args:
            centre_distance (float)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        '''

        centre_distance = float(centre_distance)
        method_result = self.wrapped.AddCylindricalGearPair.Overloads[_DOUBLE](centre_distance if centre_distance else 0.0)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_cylindrical_gear_set_with_options(self, cylindrical_gear_linear_train_creation_options: Optional['_2433.CylindricalGearLinearTrainCreationOptions'] = None) -> '_2386.CylindricalGearSet':
        ''' 'AddCylindricalGearSet' is the original name of this method.

        Args:
            cylindrical_gear_linear_train_creation_options (mastapy.system_model.part_model.creation_options.CylindricalGearLinearTrainCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        '''

        method_result = self.wrapped.AddCylindricalGearSet.Overloads[_CYLINDRICAL_GEAR_LINEAR_TRAIN_CREATION_OPTIONS](cylindrical_gear_linear_train_creation_options.wrapped if cylindrical_gear_linear_train_creation_options else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_cylindrical_gear_set(self, name: 'str', centre_distances: 'List[float]') -> '_2386.CylindricalGearSet':
        ''' 'AddCylindricalGearSet' is the original name of this method.

        Args:
            name (str)
            centre_distances (List[float])

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        '''

        name = str(name)
        centre_distances = conversion.mp_to_pn_array_float(centre_distances)
        method_result = self.wrapped.AddCylindricalGearSet.Overloads[_STRING, _ARRAY[_DOUBLE]](name if name else '', centre_distances)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_cylindrical_gear_set_extended(self, name: 'str', normal_pressure_angle: 'float', helix_angle: 'float', normal_module: 'float', pinion_hand: '_304.Hand', centre_distances: 'List[float]') -> '_2386.CylindricalGearSet':
        ''' 'AddCylindricalGearSet' is the original name of this method.

        Args:
            name (str)
            normal_pressure_angle (float)
            helix_angle (float)
            normal_module (float)
            pinion_hand (mastapy.gears.Hand)
            centre_distances (List[float])

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        '''

        name = str(name)
        normal_pressure_angle = float(normal_pressure_angle)
        helix_angle = float(helix_angle)
        normal_module = float(normal_module)
        pinion_hand = conversion.mp_to_pn_enum(pinion_hand)
        centre_distances = conversion.mp_to_pn_array_float(centre_distances)
        method_result = self.wrapped.AddCylindricalGearSet.Overloads[_STRING, _DOUBLE, _DOUBLE, _DOUBLE, _HAND, _ARRAY[_DOUBLE]](name if name else '', normal_pressure_angle if normal_pressure_angle else 0.0, helix_angle if helix_angle else 0.0, normal_module if normal_module else 0.0, pinion_hand, centre_distances)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_spiral_bevel_gear_set_with_options(self, spiral_bevel_gear_set_creation_options: Optional['_1101.SpiralBevelGearSetCreationOptions'] = None) -> '_2404.SpiralBevelGearSet':
        ''' 'AddSpiralBevelGearSet' is the original name of this method.

        Args:
            spiral_bevel_gear_set_creation_options (mastapy.gears.gear_designs.creation_options.SpiralBevelGearSetCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        '''

        method_result = self.wrapped.AddSpiralBevelGearSet.Overloads[_SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS](spiral_bevel_gear_set_creation_options.wrapped if spiral_bevel_gear_set_creation_options else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_spiral_bevel_gear_set_detailed(self, name: Optional['str'] = 'Spiral Bevel Gear Set', outer_transverse_module: Optional['float'] = 0.00635, pressure_angle: Optional['float'] = 0.02, mean_spiral_angle: Optional['float'] = 0.523599, wheel_number_of_teeth: Optional['int'] = 43, pinion_number_of_teeth: Optional['int'] = 14, wheel_face_width: Optional['float'] = 0.02, pinion_face_width: Optional['float'] = 0.02, pinion_face_width_offset: Optional['float'] = 0.0, shaft_angle: Optional['float'] = 1.5708) -> '_2404.SpiralBevelGearSet':
        ''' 'AddSpiralBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)
            outer_transverse_module (float, optional)
            pressure_angle (float, optional)
            mean_spiral_angle (float, optional)
            wheel_number_of_teeth (int, optional)
            pinion_number_of_teeth (int, optional)
            wheel_face_width (float, optional)
            pinion_face_width (float, optional)
            pinion_face_width_offset (float, optional)
            shaft_angle (float, optional)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        '''

        name = str(name)
        outer_transverse_module = float(outer_transverse_module)
        pressure_angle = float(pressure_angle)
        mean_spiral_angle = float(mean_spiral_angle)
        wheel_number_of_teeth = int(wheel_number_of_teeth)
        pinion_number_of_teeth = int(pinion_number_of_teeth)
        wheel_face_width = float(wheel_face_width)
        pinion_face_width = float(pinion_face_width)
        pinion_face_width_offset = float(pinion_face_width_offset)
        shaft_angle = float(shaft_angle)
        method_result = self.wrapped.AddSpiralBevelGearSet.Overloads[_STRING, _DOUBLE, _DOUBLE, _DOUBLE, _INT_32, _INT_32, _DOUBLE, _DOUBLE, _DOUBLE, _DOUBLE](name if name else '', outer_transverse_module if outer_transverse_module else 0.0, pressure_angle if pressure_angle else 0.0, mean_spiral_angle if mean_spiral_angle else 0.0, wheel_number_of_teeth if wheel_number_of_teeth else 0, pinion_number_of_teeth if pinion_number_of_teeth else 0, wheel_face_width if wheel_face_width else 0.0, pinion_face_width if pinion_face_width else 0.0, pinion_face_width_offset if pinion_face_width_offset else 0.0, shaft_angle if shaft_angle else 0.0)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_hypoid_gear_set_detailed(self, name: Optional['str'] = 'Hypoid Gear Set', pinion_number_of_teeth: Optional['int'] = 7, wheel_number_of_teeth: Optional['int'] = 41, outer_transverse_module: Optional['float'] = 0.0109756, wheel_face_width: Optional['float'] = 0.072, offset: Optional['float'] = 0.045, average_pressure_angle: Optional['float'] = 0.3926991, design_method: Optional['_1131.AGMAGleasonConicalGearGeometryMethods'] = _1131.AGMAGleasonConicalGearGeometryMethods.GLEASON) -> '_2395.HypoidGearSet':
        ''' 'AddHypoidGearSet' is the original name of this method.

        Args:
            name (str, optional)
            pinion_number_of_teeth (int, optional)
            wheel_number_of_teeth (int, optional)
            outer_transverse_module (float, optional)
            wheel_face_width (float, optional)
            offset (float, optional)
            average_pressure_angle (float, optional)
            design_method (mastapy.gears.gear_designs.bevel.AGMAGleasonConicalGearGeometryMethods, optional)

        Returns:
            mastapy.system_model.part_model.gears.HypoidGearSet
        '''

        name = str(name)
        pinion_number_of_teeth = int(pinion_number_of_teeth)
        wheel_number_of_teeth = int(wheel_number_of_teeth)
        outer_transverse_module = float(outer_transverse_module)
        wheel_face_width = float(wheel_face_width)
        offset = float(offset)
        average_pressure_angle = float(average_pressure_angle)
        design_method = conversion.mp_to_pn_enum(design_method)
        method_result = self.wrapped.AddHypoidGearSet.Overloads[_STRING, _INT_32, _INT_32, _DOUBLE, _DOUBLE, _DOUBLE, _DOUBLE, _AGMA_GLEASON_CONICAL_GEAR_GEOMETRY_METHODS](name if name else '', pinion_number_of_teeth if pinion_number_of_teeth else 0, wheel_number_of_teeth if wheel_number_of_teeth else 0, outer_transverse_module if outer_transverse_module else 0.0, wheel_face_width if wheel_face_width else 0.0, offset if offset else 0.0, average_pressure_angle if average_pressure_angle else 0.0, design_method)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_bearing(self, name: 'str') -> '_2302.Bearing':
        ''' 'AddBearing' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        '''

        name = str(name)
        method_result = self.wrapped.AddBearing.Overloads[_STRING](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_cycloidal_assembly_with_options(self, cycloidal_assembly_creation_options: Optional['_2432.CycloidalAssemblyCreationOptions'] = None) -> '_2428.CycloidalAssembly':
        ''' 'AddCycloidalAssembly' is the original name of this method.

        Args:
            cycloidal_assembly_creation_options (mastapy.system_model.part_model.creation_options.CycloidalAssemblyCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalAssembly
        '''

        method_result = self.wrapped.AddCycloidalAssembly.Overloads[_CYCLOIDAL_ASSEMBLY_CREATION_OPTIONS](cycloidal_assembly_creation_options.wrapped if cycloidal_assembly_creation_options else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_cycloidal_assembly(self, number_of_discs: Optional['int'] = 1, number_of_pins: Optional['int'] = 10, name: Optional['str'] = 'Cycloidal Assembly') -> '_2428.CycloidalAssembly':
        ''' 'AddCycloidalAssembly' is the original name of this method.

        Args:
            number_of_discs (int, optional)
            number_of_pins (int, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalAssembly
        '''

        number_of_discs = int(number_of_discs)
        number_of_pins = int(number_of_pins)
        name = str(name)
        method_result = self.wrapped.AddCycloidalAssembly.Overloads[_INT_32, _INT_32, _STRING](number_of_discs if number_of_discs else 0, number_of_pins if number_of_pins else 0, name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_axial_clearance_bearing(self, name: 'str', contact_diameter: 'float') -> '_2302.Bearing':
        ''' 'AddAxialClearanceBearing' is the original name of this method.

        Args:
            name (str)
            contact_diameter (float)

        Returns:
            mastapy.system_model.part_model.Bearing
        '''

        name = str(name)
        contact_diameter = float(contact_diameter)
        method_result = self.wrapped.AddAxialClearanceBearing(name if name else '', contact_diameter if contact_diameter else 0.0)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_shaft_hub_connection(self, name: 'str') -> '_2458.ShaftHubConnection':
        ''' 'AddShaftHubConnection' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ShaftHubConnection
        '''

        name = str(name)
        method_result = self.wrapped.AddShaftHubConnection(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_rolling_bearing_from_catalogue(self, catalogue: '_1747.BearingCatalog', designation: 'str', name: 'str') -> '_2302.Bearing':
        ''' 'AddRollingBearingFromCatalogue' is the original name of this method.

        Args:
            catalogue (mastapy.bearings.BearingCatalog)
            designation (str)
            name (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        '''

        catalogue = conversion.mp_to_pn_enum(catalogue)
        designation = str(designation)
        name = str(name)
        method_result = self.wrapped.AddRollingBearingFromCatalogue(catalogue, designation if designation else '', name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_bearing_with_name_and_rolling_bearing_type(self, name: 'str', type_: '_1772.RollingBearingType') -> '_2302.Bearing':
        ''' 'AddBearing' is the original name of this method.

        Args:
            name (str)
            type_ (mastapy.bearings.RollingBearingType)

        Returns:
            mastapy.system_model.part_model.Bearing
        '''

        name = str(name)
        type_ = conversion.mp_to_pn_enum(type_)
        method_result = self.wrapped.AddBearing.Overloads[_STRING, _ROLLING_BEARING_TYPE](name if name else '', type_)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_bearing_with_name_rolling_bearing_type_and_designation(self, name: 'str', type_: '_1772.RollingBearingType', designation: 'str') -> '_2302.Bearing':
        ''' 'AddBearing' is the original name of this method.

        Args:
            name (str)
            type_ (mastapy.bearings.RollingBearingType)
            designation (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        '''

        name = str(name)
        type_ = conversion.mp_to_pn_enum(type_)
        designation = str(designation)
        method_result = self.wrapped.AddBearing.Overloads[_STRING, _ROLLING_BEARING_TYPE, _STRING](name if name else '', type_, designation if designation else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_linear_bearing(self, name: 'str', width: 'float') -> '_2302.Bearing':
        ''' 'AddLinearBearing' is the original name of this method.

        Args:
            name (str)
            width (float)

        Returns:
            mastapy.system_model.part_model.Bearing
        '''

        name = str(name)
        width = float(width)
        method_result = self.wrapped.AddLinearBearing(name if name else '', width if width else 0.0)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def import_fe_mesh_from_file(self, file_name: 'str', stiffness_matrix: '_74.NodalMatrix') -> '_2314.FEPart':
        ''' 'ImportFEMeshFromFile' is the original name of this method.

        Args:
            file_name (str)
            stiffness_matrix (mastapy.nodal_analysis.NodalMatrix)

        Returns:
            mastapy.system_model.part_model.FEPart
        '''

        file_name = str(file_name)
        method_result = self.wrapped.ImportFEMeshFromFile(file_name if file_name else '', stiffness_matrix.wrapped if stiffness_matrix else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_assembly(self, name: Optional['str'] = 'Assembly') -> 'Assembly':
        ''' 'AddAssembly' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.Assembly
        '''

        name = str(name)
        method_result = self.wrapped.AddAssembly(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_oil_seal(self, name: Optional['str'] = 'Oil Seal') -> '_2327.OilSeal':
        ''' 'AddOilSeal' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.OilSeal
        '''

        name = str(name)
        method_result = self.wrapped.AddOilSeal(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_power_load(self, name: Optional['str'] = 'Power Load') -> '_2333.PowerLoad':
        ''' 'AddPowerLoad' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.PowerLoad
        '''

        name = str(name)
        method_result = self.wrapped.AddPowerLoad(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_point_load(self, name: Optional['str'] = 'Point Load') -> '_2332.PointLoad':
        ''' 'AddPointLoad' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.PointLoad
        '''

        name = str(name)
        method_result = self.wrapped.AddPointLoad(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_datum(self, name: Optional['str'] = 'Datum') -> '_2310.Datum':
        ''' 'AddDatum' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.Datum
        '''

        name = str(name)
        method_result = self.wrapped.AddDatum(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_imported_fe_component(self, name: Optional['str'] = 'Imported FE') -> '_2314.FEPart':
        ''' 'AddImportedFEComponent' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.FEPart
        '''

        name = str(name)
        method_result = self.wrapped.AddImportedFEComponent(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_measurement_component(self, name: Optional['str'] = 'Measurement Component') -> '_2324.MeasurementComponent':
        ''' 'AddMeasurementComponent' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.MeasurementComponent
        '''

        name = str(name)
        method_result = self.wrapped.AddMeasurementComponent(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_mass_disc(self, name: Optional['str'] = 'Mass Disc') -> '_2323.MassDisc':
        ''' 'AddMassDisc' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.MassDisc
        '''

        name = str(name)
        method_result = self.wrapped.AddMassDisc(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_unbalanced_mass(self, name: Optional['str'] = 'Unbalanced Mass') -> '_2338.UnbalancedMass':
        ''' 'AddUnbalancedMass' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.UnbalancedMass
        '''

        name = str(name)
        method_result = self.wrapped.AddUnbalancedMass(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_straight_bevel_differential_gear_set(self, name: Optional['str'] = 'Straight Bevel Differential Gear Set') -> '_2406.StraightBevelDiffGearSet':
        ''' 'AddStraightBevelDifferentialGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelDiffGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddStraightBevelDifferentialGearSet(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_spiral_bevel_differential_gear_set(self, name: Optional['str'] = 'Spiral Bevel Differential Gear Set') -> '_2376.BevelDifferentialGearSet':
        ''' 'AddSpiralBevelDifferentialGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddSpiralBevelDifferentialGearSet(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_zerol_bevel_differential_gear_set(self, name: Optional['str'] = 'Zerol Bevel Differential Gear Set') -> '_2376.BevelDifferentialGearSet':
        ''' 'AddZerolBevelDifferentialGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddZerolBevelDifferentialGearSet(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_planetary_gear_set(self, name: Optional['str'] = 'Planetary Gear Set') -> '_2402.PlanetaryGearSet':
        ''' 'AddPlanetaryGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.PlanetaryGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddPlanetaryGearSet(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_spiral_bevel_gear_set(self, name: Optional['str'] = 'Spiral Bevel Gear Set') -> '_2404.SpiralBevelGearSet':
        ''' 'AddSpiralBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddSpiralBevelGearSet.Overloads[_STRING](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, name: Optional['str'] = 'Klingelnberg Cyclo Palloid Spiral Bevel Gear Set') -> '_2401.KlingelnbergCycloPalloidSpiralBevelGearSet':
        ''' 'AddKlingelnbergCycloPalloidSpiralBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddKlingelnbergCycloPalloidSpiralBevelGearSet(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_klingelnberg_cyclo_palloid_hypoid_gear_set(self, name: Optional['str'] = 'Klingelnberg Cyclo Palloid Hypoid Gear Set') -> '_2399.KlingelnbergCycloPalloidHypoidGearSet':
        ''' 'AddKlingelnbergCycloPalloidHypoidGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddKlingelnbergCycloPalloidHypoidGearSet(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_straight_bevel_gear_set(self, name: Optional['str'] = 'Straight Bevel Gear Set') -> '_2408.StraightBevelGearSet':
        ''' 'AddStraightBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddStraightBevelGearSet(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_hypoid_gear_set(self, name: Optional['str'] = 'Hypoid Gear Set') -> '_2395.HypoidGearSet':
        ''' 'AddHypoidGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.HypoidGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddHypoidGearSet.Overloads[_STRING](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_face_gear_set(self, name: Optional['str'] = 'Face Gear Set') -> '_2389.FaceGearSet':
        ''' 'AddFaceGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.FaceGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddFaceGearSet(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_worm_gear_set(self, name: Optional['str'] = 'Worm Gear Set') -> '_2412.WormGearSet':
        ''' 'AddWormGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.WormGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddWormGearSet(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_zerol_bevel_gear_set(self, name: Optional['str'] = 'Zerol Bevel Gear Set') -> '_2414.ZerolBevelGearSet':
        ''' 'AddZerolBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.ZerolBevelGearSet
        '''

        name = str(name)
        method_result = self.wrapped.AddZerolBevelGearSet(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_clutch(self, name: Optional['str'] = 'Clutch') -> '_2438.Clutch':
        ''' 'AddClutch' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.Clutch
        '''

        name = str(name)
        method_result = self.wrapped.AddClutch(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_synchroniser(self, name: Optional['str'] = 'Synchroniser') -> '_2462.Synchroniser':
        ''' 'AddSynchroniser' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.Synchroniser
        '''

        name = str(name)
        method_result = self.wrapped.AddSynchroniser(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_rolling_ring(self, name: Optional['str'] = 'Rolling Ring') -> '_2456.RollingRing':
        ''' 'AddRollingRing' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.RollingRing
        '''

        name = str(name)
        method_result = self.wrapped.AddRollingRing(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_concept_coupling(self, name: Optional['str'] = 'Concept Coupling') -> '_2441.ConceptCoupling':
        ''' 'AddConceptCoupling' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.ConceptCoupling
        '''

        name = str(name)
        method_result = self.wrapped.AddConceptCoupling(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_cvt(self, name: Optional['str'] = 'CVT') -> '_2446.CVT':
        ''' 'AddCVT' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.CVT
        '''

        name = str(name)
        method_result = self.wrapped.AddCVT(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_spring_damper(self, name: Optional['str'] = 'Spring Damper') -> '_2460.SpringDamper':
        ''' 'AddSpringDamper' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.SpringDamper
        '''

        name = str(name)
        method_result = self.wrapped.AddSpringDamper(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_torque_converter(self, name: Optional['str'] = 'Torque Converter') -> '_2467.TorqueConverter':
        ''' 'AddTorqueConverter' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.TorqueConverter
        '''

        name = str(name)
        method_result = self.wrapped.AddTorqueConverter(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_bolted_joint(self, name: Optional['str'] = 'Bolted Joint') -> '_2305.BoltedJoint':
        ''' 'AddBoltedJoint' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.BoltedJoint
        '''

        name = str(name)
        method_result = self.wrapped.AddBoltedJoint(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_belt_drive_with_options(self, belt_creation_options: Optional['_2431.BeltCreationOptions'] = None) -> '_2436.BeltDrive':
        ''' 'AddBeltDrive' is the original name of this method.

        Args:
            belt_creation_options (mastapy.system_model.part_model.creation_options.BeltCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.couplings.BeltDrive
        '''

        method_result = self.wrapped.AddBeltDrive.Overloads[_BELT_CREATION_OPTIONS](belt_creation_options.wrapped if belt_creation_options else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_belt_drive(self, centre_distance: Optional['float'] = 0.1, pulley_a_diameter: Optional['float'] = 0.08, pulley_b_diameter: Optional['float'] = 0.08, name: Optional['str'] = 'Belt Drive') -> '_2436.BeltDrive':
        ''' 'AddBeltDrive' is the original name of this method.

        Args:
            centre_distance (float, optional)
            pulley_a_diameter (float, optional)
            pulley_b_diameter (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.BeltDrive
        '''

        centre_distance = float(centre_distance)
        pulley_a_diameter = float(pulley_a_diameter)
        pulley_b_diameter = float(pulley_b_diameter)
        name = str(name)
        method_result = self.wrapped.AddBeltDrive.Overloads[_DOUBLE, _DOUBLE, _DOUBLE, _STRING](centre_distance if centre_distance else 0.0, pulley_a_diameter if pulley_a_diameter else 0.0, pulley_b_diameter if pulley_b_diameter else 0.0, name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_planet_carrier_with_options(self, planet_carrier_creation_options: Optional['_2434.PlanetCarrierCreationOptions'] = None) -> '_2330.PlanetCarrier':
        ''' 'AddPlanetCarrier' is the original name of this method.

        Args:
            planet_carrier_creation_options (mastapy.system_model.part_model.creation_options.PlanetCarrierCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.PlanetCarrier
        '''

        method_result = self.wrapped.AddPlanetCarrier.Overloads[_PLANET_CARRIER_CREATION_OPTIONS](planet_carrier_creation_options.wrapped if planet_carrier_creation_options else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_planet_carrier(self, number_of_planets: Optional['int'] = 3, diameter: Optional['float'] = 0.05) -> '_2330.PlanetCarrier':
        ''' 'AddPlanetCarrier' is the original name of this method.

        Args:
            number_of_planets (int, optional)
            diameter (float, optional)

        Returns:
            mastapy.system_model.part_model.PlanetCarrier
        '''

        number_of_planets = int(number_of_planets)
        diameter = float(diameter)
        method_result = self.wrapped.AddPlanetCarrier.Overloads[_INT_32, _DOUBLE](number_of_planets if number_of_planets else 0, diameter if diameter else 0.0)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_shaft_with_options(self, shaft_creation_options: '_2435.ShaftCreationOptions') -> '_2343.Shaft':
        ''' 'AddShaft' is the original name of this method.

        Args:
            shaft_creation_options (mastapy.system_model.part_model.creation_options.ShaftCreationOptions)

        Returns:
            mastapy.system_model.part_model.shaft_model.Shaft
        '''

        method_result = self.wrapped.AddShaft.Overloads[_SHAFT_CREATION_OPTIONS](shaft_creation_options.wrapped if shaft_creation_options else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None
