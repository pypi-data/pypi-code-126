'''_2132.py

ComponentConnection
'''


from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import (
    _2306, _2298, _2299, _2302,
    _2304, _2309, _2310, _2313,
    _2314, _2316, _2323, _2324,
    _2325, _2327, _2330, _2332,
    _2333, _2338, _2340
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2343
from mastapy.system_model.part_model.gears import (
    _2373, _2375, _2377, _2378,
    _2379, _2381, _2383, _2385,
    _2387, _2388, _2390, _2394,
    _2396, _2398, _2400, _2403,
    _2405, _2407, _2409, _2410,
    _2411, _2413
)
from mastapy.system_model.part_model.cycloidal import _2429, _2430
from mastapy.system_model.part_model.couplings import (
    _2439, _2442, _2444, _2447,
    _2449, _2450, _2456, _2458,
    _2461, _2464, _2465, _2466,
    _2468, _2470
)
from mastapy.system_model.connections_and_sockets import _2133
from mastapy._internal.python_net import python_net_import

_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ComponentConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentConnection',)


class ComponentConnection(_2133.ComponentMeasurer):
    '''ComponentConnection

    This is a mastapy class.
    '''

    TYPE = _COMPONENT_CONNECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ComponentConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def socket(self) -> 'str':
        '''str: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Socket

    @property
    def connected_components_socket(self) -> 'str':
        '''str: 'ConnectedComponentsSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ConnectedComponentsSocket

    @property
    def assembly_view(self) -> 'Image':
        '''Image: 'AssemblyView' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_smt_bitmap(self.wrapped.AssemblyView)
        return value

    @property
    def detail_view(self) -> 'Image':
        '''Image: 'DetailView' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_smt_bitmap(self.wrapped.DetailView)
        return value

    @property
    def connected_component(self) -> '_2306.Component':
        '''Component: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2306.Component.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to Component. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_abstract_shaft(self) -> '_2298.AbstractShaft':
        '''AbstractShaft: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2298.AbstractShaft.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to AbstractShaft. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_abstract_shaft_or_housing(self) -> '_2299.AbstractShaftOrHousing':
        '''AbstractShaftOrHousing: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2299.AbstractShaftOrHousing.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to AbstractShaftOrHousing. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_bearing(self) -> '_2302.Bearing':
        '''Bearing: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2302.Bearing.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to Bearing. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_bolt(self) -> '_2304.Bolt':
        '''Bolt: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2304.Bolt.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to Bolt. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_connector(self) -> '_2309.Connector':
        '''Connector: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2309.Connector.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to Connector. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_datum(self) -> '_2310.Datum':
        '''Datum: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2310.Datum.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to Datum. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_external_cad_model(self) -> '_2313.ExternalCADModel':
        '''ExternalCADModel: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2313.ExternalCADModel.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to ExternalCADModel. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_fe_part(self) -> '_2314.FEPart':
        '''FEPart: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2314.FEPart.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to FEPart. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_guide_dxf_model(self) -> '_2316.GuideDxfModel':
        '''GuideDxfModel: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2316.GuideDxfModel.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to GuideDxfModel. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_mass_disc(self) -> '_2323.MassDisc':
        '''MassDisc: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2323.MassDisc.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to MassDisc. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_measurement_component(self) -> '_2324.MeasurementComponent':
        '''MeasurementComponent: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2324.MeasurementComponent.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to MeasurementComponent. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_mountable_component(self) -> '_2325.MountableComponent':
        '''MountableComponent: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2325.MountableComponent.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to MountableComponent. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_oil_seal(self) -> '_2327.OilSeal':
        '''OilSeal: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2327.OilSeal.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to OilSeal. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_planet_carrier(self) -> '_2330.PlanetCarrier':
        '''PlanetCarrier: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2330.PlanetCarrier.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to PlanetCarrier. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_point_load(self) -> '_2332.PointLoad':
        '''PointLoad: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2332.PointLoad.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to PointLoad. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_power_load(self) -> '_2333.PowerLoad':
        '''PowerLoad: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2333.PowerLoad.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to PowerLoad. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_unbalanced_mass(self) -> '_2338.UnbalancedMass':
        '''UnbalancedMass: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2338.UnbalancedMass.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to UnbalancedMass. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_virtual_component(self) -> '_2340.VirtualComponent':
        '''VirtualComponent: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2340.VirtualComponent.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to VirtualComponent. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_shaft(self) -> '_2343.Shaft':
        '''Shaft: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2343.Shaft.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to Shaft. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_agma_gleason_conical_gear(self) -> '_2373.AGMAGleasonConicalGear':
        '''AGMAGleasonConicalGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2373.AGMAGleasonConicalGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to AGMAGleasonConicalGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_bevel_differential_gear(self) -> '_2375.BevelDifferentialGear':
        '''BevelDifferentialGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2375.BevelDifferentialGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to BevelDifferentialGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_bevel_differential_planet_gear(self) -> '_2377.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2377.BevelDifferentialPlanetGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to BevelDifferentialPlanetGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_bevel_differential_sun_gear(self) -> '_2378.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2378.BevelDifferentialSunGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to BevelDifferentialSunGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_bevel_gear(self) -> '_2379.BevelGear':
        '''BevelGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2379.BevelGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to BevelGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_concept_gear(self) -> '_2381.ConceptGear':
        '''ConceptGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2381.ConceptGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to ConceptGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_conical_gear(self) -> '_2383.ConicalGear':
        '''ConicalGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2383.ConicalGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to ConicalGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_cylindrical_gear(self) -> '_2385.CylindricalGear':
        '''CylindricalGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2385.CylindricalGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to CylindricalGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_cylindrical_planet_gear(self) -> '_2387.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2387.CylindricalPlanetGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to CylindricalPlanetGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_face_gear(self) -> '_2388.FaceGear':
        '''FaceGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2388.FaceGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to FaceGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_gear(self) -> '_2390.Gear':
        '''Gear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2390.Gear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to Gear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_hypoid_gear(self) -> '_2394.HypoidGear':
        '''HypoidGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2394.HypoidGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to HypoidGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2396.KlingelnbergCycloPalloidConicalGear':
        '''KlingelnbergCycloPalloidConicalGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2396.KlingelnbergCycloPalloidConicalGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2398.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2398.KlingelnbergCycloPalloidHypoidGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2400.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2400.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_spiral_bevel_gear(self) -> '_2403.SpiralBevelGear':
        '''SpiralBevelGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2403.SpiralBevelGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to SpiralBevelGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_straight_bevel_diff_gear(self) -> '_2405.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2405.StraightBevelDiffGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to StraightBevelDiffGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_straight_bevel_gear(self) -> '_2407.StraightBevelGear':
        '''StraightBevelGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2407.StraightBevelGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to StraightBevelGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_straight_bevel_planet_gear(self) -> '_2409.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2409.StraightBevelPlanetGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to StraightBevelPlanetGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_straight_bevel_sun_gear(self) -> '_2410.StraightBevelSunGear':
        '''StraightBevelSunGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2410.StraightBevelSunGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to StraightBevelSunGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_worm_gear(self) -> '_2411.WormGear':
        '''WormGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2411.WormGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to WormGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_zerol_bevel_gear(self) -> '_2413.ZerolBevelGear':
        '''ZerolBevelGear: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2413.ZerolBevelGear.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to ZerolBevelGear. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_cycloidal_disc(self) -> '_2429.CycloidalDisc':
        '''CycloidalDisc: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2429.CycloidalDisc.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to CycloidalDisc. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_ring_pins(self) -> '_2430.RingPins':
        '''RingPins: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2430.RingPins.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to RingPins. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_clutch_half(self) -> '_2439.ClutchHalf':
        '''ClutchHalf: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2439.ClutchHalf.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to ClutchHalf. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_concept_coupling_half(self) -> '_2442.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2442.ConceptCouplingHalf.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_coupling_half(self) -> '_2444.CouplingHalf':
        '''CouplingHalf: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2444.CouplingHalf.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to CouplingHalf. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_cvt_pulley(self) -> '_2447.CVTPulley':
        '''CVTPulley: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2447.CVTPulley.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to CVTPulley. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_part_to_part_shear_coupling_half(self) -> '_2449.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2449.PartToPartShearCouplingHalf.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to PartToPartShearCouplingHalf. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_pulley(self) -> '_2450.Pulley':
        '''Pulley: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2450.Pulley.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to Pulley. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_rolling_ring(self) -> '_2456.RollingRing':
        '''RollingRing: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2456.RollingRing.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to RollingRing. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_shaft_hub_connection(self) -> '_2458.ShaftHubConnection':
        '''ShaftHubConnection: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2458.ShaftHubConnection.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to ShaftHubConnection. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_spring_damper_half(self) -> '_2461.SpringDamperHalf':
        '''SpringDamperHalf: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2461.SpringDamperHalf.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to SpringDamperHalf. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_synchroniser_half(self) -> '_2464.SynchroniserHalf':
        '''SynchroniserHalf: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2464.SynchroniserHalf.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to SynchroniserHalf. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_synchroniser_part(self) -> '_2465.SynchroniserPart':
        '''SynchroniserPart: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2465.SynchroniserPart.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to SynchroniserPart. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_synchroniser_sleeve(self) -> '_2466.SynchroniserSleeve':
        '''SynchroniserSleeve: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2466.SynchroniserSleeve.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_torque_converter_pump(self) -> '_2468.TorqueConverterPump':
        '''TorqueConverterPump: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2468.TorqueConverterPump.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to TorqueConverterPump. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    @property
    def connected_component_of_type_torque_converter_turbine(self) -> '_2470.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2470.TorqueConverterTurbine.TYPE not in self.wrapped.ConnectedComponent.__class__.__mro__:
            raise CastException('Failed to cast connected_component to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.ConnectedComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectedComponent.__class__)(self.wrapped.ConnectedComponent) if self.wrapped.ConnectedComponent is not None else None

    def delete(self):
        ''' 'Delete' is the original name of this method.'''

        self.wrapped.Delete()

    def swap(self):
        ''' 'Swap' is the original name of this method.'''

        self.wrapped.Swap()
