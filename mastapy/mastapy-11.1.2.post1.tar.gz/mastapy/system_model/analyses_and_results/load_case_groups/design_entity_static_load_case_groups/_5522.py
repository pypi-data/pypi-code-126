'''_5522.py

PartStaticLoadCaseGroup
'''


from typing import List

from mastapy.system_model.part_model import (
    _2329, _2296, _2297, _2298,
    _2299, _2302, _2304, _2305,
    _2306, _2309, _2310, _2313,
    _2314, _2315, _2316, _2323,
    _2324, _2325, _2327, _2330,
    _2332, _2333, _2335, _2337,
    _2338, _2340
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2343
from mastapy.system_model.part_model.gears import (
    _2373, _2374, _2375, _2376,
    _2377, _2378, _2379, _2380,
    _2381, _2382, _2383, _2384,
    _2385, _2386, _2387, _2388,
    _2389, _2390, _2392, _2394,
    _2395, _2396, _2397, _2398,
    _2399, _2400, _2401, _2402,
    _2403, _2404, _2405, _2406,
    _2407, _2408, _2409, _2410,
    _2411, _2412, _2413, _2414
)
from mastapy.system_model.part_model.cycloidal import _2428, _2429, _2430
from mastapy.system_model.part_model.couplings import (
    _2436, _2438, _2439, _2441,
    _2442, _2443, _2444, _2446,
    _2447, _2448, _2449, _2450,
    _2456, _2457, _2458, _2460,
    _2461, _2462, _2464, _2465,
    _2466, _2467, _2468, _2470
)
from mastapy.system_model.analyses_and_results.static_loads import _6761
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5520
from mastapy._internal.python_net import python_net_import

_PART_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'PartStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('PartStaticLoadCaseGroup',)


class PartStaticLoadCaseGroup(_5520.DesignEntityStaticLoadCaseGroup):
    '''PartStaticLoadCaseGroup

    This is a mastapy class.
    '''

    TYPE = _PART_STATIC_LOAD_CASE_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> '_2329.Part':
        '''Part: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2329.Part.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Part. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_assembly(self) -> '_2296.Assembly':
        '''Assembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2296.Assembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Assembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_abstract_assembly(self) -> '_2297.AbstractAssembly':
        '''AbstractAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2297.AbstractAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to AbstractAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_abstract_shaft(self) -> '_2298.AbstractShaft':
        '''AbstractShaft: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2298.AbstractShaft.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to AbstractShaft. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_abstract_shaft_or_housing(self) -> '_2299.AbstractShaftOrHousing':
        '''AbstractShaftOrHousing: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2299.AbstractShaftOrHousing.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to AbstractShaftOrHousing. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bearing(self) -> '_2302.Bearing':
        '''Bearing: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2302.Bearing.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Bearing. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bolt(self) -> '_2304.Bolt':
        '''Bolt: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2304.Bolt.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Bolt. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bolted_joint(self) -> '_2305.BoltedJoint':
        '''BoltedJoint: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2305.BoltedJoint.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BoltedJoint. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_component(self) -> '_2306.Component':
        '''Component: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2306.Component.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Component. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_connector(self) -> '_2309.Connector':
        '''Connector: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2309.Connector.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Connector. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_datum(self) -> '_2310.Datum':
        '''Datum: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2310.Datum.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Datum. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_external_cad_model(self) -> '_2313.ExternalCADModel':
        '''ExternalCADModel: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2313.ExternalCADModel.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ExternalCADModel. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_fe_part(self) -> '_2314.FEPart':
        '''FEPart: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2314.FEPart.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to FEPart. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_flexible_pin_assembly(self) -> '_2315.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2315.FlexiblePinAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to FlexiblePinAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_guide_dxf_model(self) -> '_2316.GuideDxfModel':
        '''GuideDxfModel: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2316.GuideDxfModel.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to GuideDxfModel. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_mass_disc(self) -> '_2323.MassDisc':
        '''MassDisc: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2323.MassDisc.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to MassDisc. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_measurement_component(self) -> '_2324.MeasurementComponent':
        '''MeasurementComponent: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2324.MeasurementComponent.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to MeasurementComponent. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_mountable_component(self) -> '_2325.MountableComponent':
        '''MountableComponent: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2325.MountableComponent.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to MountableComponent. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_oil_seal(self) -> '_2327.OilSeal':
        '''OilSeal: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2327.OilSeal.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to OilSeal. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_planet_carrier(self) -> '_2330.PlanetCarrier':
        '''PlanetCarrier: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2330.PlanetCarrier.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PlanetCarrier. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_point_load(self) -> '_2332.PointLoad':
        '''PointLoad: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2332.PointLoad.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PointLoad. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_power_load(self) -> '_2333.PowerLoad':
        '''PowerLoad: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2333.PowerLoad.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PowerLoad. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_root_assembly(self) -> '_2335.RootAssembly':
        '''RootAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2335.RootAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to RootAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_specialised_assembly(self) -> '_2337.SpecialisedAssembly':
        '''SpecialisedAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2337.SpecialisedAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SpecialisedAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_unbalanced_mass(self) -> '_2338.UnbalancedMass':
        '''UnbalancedMass: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2338.UnbalancedMass.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to UnbalancedMass. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_virtual_component(self) -> '_2340.VirtualComponent':
        '''VirtualComponent: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2340.VirtualComponent.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to VirtualComponent. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_shaft(self) -> '_2343.Shaft':
        '''Shaft: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2343.Shaft.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Shaft. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_agma_gleason_conical_gear(self) -> '_2373.AGMAGleasonConicalGear':
        '''AGMAGleasonConicalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2373.AGMAGleasonConicalGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to AGMAGleasonConicalGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_agma_gleason_conical_gear_set(self) -> '_2374.AGMAGleasonConicalGearSet':
        '''AGMAGleasonConicalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2374.AGMAGleasonConicalGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to AGMAGleasonConicalGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_differential_gear(self) -> '_2375.BevelDifferentialGear':
        '''BevelDifferentialGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2375.BevelDifferentialGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_differential_gear_set(self) -> '_2376.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2376.BevelDifferentialGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_differential_planet_gear(self) -> '_2377.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2377.BevelDifferentialPlanetGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialPlanetGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_differential_sun_gear(self) -> '_2378.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2378.BevelDifferentialSunGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialSunGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_gear(self) -> '_2379.BevelGear':
        '''BevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2379.BevelGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_gear_set(self) -> '_2380.BevelGearSet':
        '''BevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2380.BevelGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_concept_gear(self) -> '_2381.ConceptGear':
        '''ConceptGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2381.ConceptGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_concept_gear_set(self) -> '_2382.ConceptGearSet':
        '''ConceptGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2382.ConceptGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_conical_gear(self) -> '_2383.ConicalGear':
        '''ConicalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2383.ConicalGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConicalGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_conical_gear_set(self) -> '_2384.ConicalGearSet':
        '''ConicalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2384.ConicalGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConicalGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cylindrical_gear(self) -> '_2385.CylindricalGear':
        '''CylindricalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2385.CylindricalGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CylindricalGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cylindrical_gear_set(self) -> '_2386.CylindricalGearSet':
        '''CylindricalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2386.CylindricalGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CylindricalGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cylindrical_planet_gear(self) -> '_2387.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2387.CylindricalPlanetGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CylindricalPlanetGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_face_gear(self) -> '_2388.FaceGear':
        '''FaceGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2388.FaceGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to FaceGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_face_gear_set(self) -> '_2389.FaceGearSet':
        '''FaceGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2389.FaceGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to FaceGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_gear(self) -> '_2390.Gear':
        '''Gear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2390.Gear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Gear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_gear_set(self) -> '_2392.GearSet':
        '''GearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2392.GearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to GearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_hypoid_gear(self) -> '_2394.HypoidGear':
        '''HypoidGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2394.HypoidGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to HypoidGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_hypoid_gear_set(self) -> '_2395.HypoidGearSet':
        '''HypoidGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2395.HypoidGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to HypoidGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2396.KlingelnbergCycloPalloidConicalGear':
        '''KlingelnbergCycloPalloidConicalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2396.KlingelnbergCycloPalloidConicalGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2397.KlingelnbergCycloPalloidConicalGearSet':
        '''KlingelnbergCycloPalloidConicalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2397.KlingelnbergCycloPalloidConicalGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2398.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2398.KlingelnbergCycloPalloidHypoidGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2399.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2399.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2400.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2400.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2401.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2401.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_planetary_gear_set(self) -> '_2402.PlanetaryGearSet':
        '''PlanetaryGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2402.PlanetaryGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PlanetaryGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_spiral_bevel_gear(self) -> '_2403.SpiralBevelGear':
        '''SpiralBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2403.SpiralBevelGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SpiralBevelGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_spiral_bevel_gear_set(self) -> '_2404.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2404.SpiralBevelGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SpiralBevelGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_diff_gear(self) -> '_2405.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2405.StraightBevelDiffGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelDiffGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_diff_gear_set(self) -> '_2406.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2406.StraightBevelDiffGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelDiffGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_gear(self) -> '_2407.StraightBevelGear':
        '''StraightBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2407.StraightBevelGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_gear_set(self) -> '_2408.StraightBevelGearSet':
        '''StraightBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2408.StraightBevelGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_planet_gear(self) -> '_2409.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2409.StraightBevelPlanetGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelPlanetGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_sun_gear(self) -> '_2410.StraightBevelSunGear':
        '''StraightBevelSunGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2410.StraightBevelSunGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelSunGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_worm_gear(self) -> '_2411.WormGear':
        '''WormGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2411.WormGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to WormGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_worm_gear_set(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2412.WormGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to WormGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_zerol_bevel_gear(self) -> '_2413.ZerolBevelGear':
        '''ZerolBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2413.ZerolBevelGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ZerolBevelGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_zerol_bevel_gear_set(self) -> '_2414.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2414.ZerolBevelGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ZerolBevelGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cycloidal_assembly(self) -> '_2428.CycloidalAssembly':
        '''CycloidalAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2428.CycloidalAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CycloidalAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cycloidal_disc(self) -> '_2429.CycloidalDisc':
        '''CycloidalDisc: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2429.CycloidalDisc.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CycloidalDisc. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_ring_pins(self) -> '_2430.RingPins':
        '''RingPins: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2430.RingPins.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to RingPins. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_belt_drive(self) -> '_2436.BeltDrive':
        '''BeltDrive: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2436.BeltDrive.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BeltDrive. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_clutch(self) -> '_2438.Clutch':
        '''Clutch: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2438.Clutch.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Clutch. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_clutch_half(self) -> '_2439.ClutchHalf':
        '''ClutchHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2439.ClutchHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ClutchHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_concept_coupling(self) -> '_2441.ConceptCoupling':
        '''ConceptCoupling: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2441.ConceptCoupling.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptCoupling. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_concept_coupling_half(self) -> '_2442.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2442.ConceptCouplingHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_coupling(self) -> '_2443.Coupling':
        '''Coupling: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2443.Coupling.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Coupling. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_coupling_half(self) -> '_2444.CouplingHalf':
        '''CouplingHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2444.CouplingHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CouplingHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cvt(self) -> '_2446.CVT':
        '''CVT: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2446.CVT.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CVT. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cvt_pulley(self) -> '_2447.CVTPulley':
        '''CVTPulley: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2447.CVTPulley.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CVTPulley. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_part_to_part_shear_coupling(self) -> '_2448.PartToPartShearCoupling':
        '''PartToPartShearCoupling: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2448.PartToPartShearCoupling.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PartToPartShearCoupling. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_part_to_part_shear_coupling_half(self) -> '_2449.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2449.PartToPartShearCouplingHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PartToPartShearCouplingHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_pulley(self) -> '_2450.Pulley':
        '''Pulley: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2450.Pulley.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Pulley. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_rolling_ring(self) -> '_2456.RollingRing':
        '''RollingRing: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2456.RollingRing.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to RollingRing. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_rolling_ring_assembly(self) -> '_2457.RollingRingAssembly':
        '''RollingRingAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2457.RollingRingAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to RollingRingAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_shaft_hub_connection(self) -> '_2458.ShaftHubConnection':
        '''ShaftHubConnection: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2458.ShaftHubConnection.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ShaftHubConnection. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_spring_damper(self) -> '_2460.SpringDamper':
        '''SpringDamper: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2460.SpringDamper.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SpringDamper. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_spring_damper_half(self) -> '_2461.SpringDamperHalf':
        '''SpringDamperHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2461.SpringDamperHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SpringDamperHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_synchroniser(self) -> '_2462.Synchroniser':
        '''Synchroniser: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2462.Synchroniser.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Synchroniser. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_synchroniser_half(self) -> '_2464.SynchroniserHalf':
        '''SynchroniserHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2464.SynchroniserHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SynchroniserHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_synchroniser_part(self) -> '_2465.SynchroniserPart':
        '''SynchroniserPart: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2465.SynchroniserPart.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SynchroniserPart. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_synchroniser_sleeve(self) -> '_2466.SynchroniserSleeve':
        '''SynchroniserSleeve: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2466.SynchroniserSleeve.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_torque_converter(self) -> '_2467.TorqueConverter':
        '''TorqueConverter: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2467.TorqueConverter.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to TorqueConverter. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_torque_converter_pump(self) -> '_2468.TorqueConverterPump':
        '''TorqueConverterPump: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2468.TorqueConverterPump.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to TorqueConverterPump. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_torque_converter_turbine(self) -> '_2470.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2470.TorqueConverterTurbine.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_load_cases(self) -> 'List[_6761.PartLoadCase]':
        '''List[PartLoadCase]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartLoadCases, constructor.new(_6761.PartLoadCase))
        return value

    def clear_user_specified_excitation_data_for_all_load_cases(self):
        ''' 'ClearUserSpecifiedExcitationDataForAllLoadCases' is the original name of this method.'''

        self.wrapped.ClearUserSpecifiedExcitationDataForAllLoadCases()
