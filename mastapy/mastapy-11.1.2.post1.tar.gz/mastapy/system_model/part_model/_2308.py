'''_2308.py

ConnectedSockets
'''


from mastapy.system_model.connections_and_sockets import (
    _2158, _2128, _2129, _2136,
    _2138, _2140, _2141, _2142,
    _2144, _2145, _2146, _2147,
    _2148, _2150, _2151, _2152,
    _2155, _2156, _2134, _2127,
    _2130, _2131, _2135, _2143,
    _2149, _2154, _2157
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.gears import (
    _2162, _2164, _2166, _2168,
    _2170, _2172, _2174, _2176,
    _2178, _2179, _2183, _2184,
    _2186, _2188, _2190, _2192,
    _2194, _2161, _2163, _2165,
    _2167, _2169, _2171, _2173,
    _2175, _2177, _2180, _2181,
    _2182, _2185, _2187, _2189,
    _2191, _2193
)
from mastapy.system_model.connections_and_sockets.cycloidal import (
    _2195, _2196, _2198, _2199,
    _2201, _2202, _2197, _2200,
    _2203
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _2205, _2207, _2209, _2211,
    _2213, _2215, _2216, _2204,
    _2206, _2208, _2210, _2212,
    _2214
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CONNECTED_SOCKETS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ConnectedSockets')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectedSockets',)


class ConnectedSockets(_0.APIBase):
    '''ConnectedSockets

    This is a mastapy class.
    '''

    TYPE = _CONNECTED_SOCKETS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectedSockets.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def socket_a(self) -> '_2158.Socket':
        '''Socket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2158.Socket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to Socket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_bearing_inner_socket(self) -> '_2128.BearingInnerSocket':
        '''BearingInnerSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2128.BearingInnerSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BearingInnerSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_bearing_outer_socket(self) -> '_2129.BearingOuterSocket':
        '''BearingOuterSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2129.BearingOuterSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BearingOuterSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_cvt_pulley_socket(self) -> '_2136.CVTPulleySocket':
        '''CVTPulleySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2136.CVTPulleySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CVTPulleySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_cylindrical_socket(self) -> '_2138.CylindricalSocket':
        '''CylindricalSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2138.CylindricalSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CylindricalSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_electric_machine_stator_socket(self) -> '_2140.ElectricMachineStatorSocket':
        '''ElectricMachineStatorSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2140.ElectricMachineStatorSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ElectricMachineStatorSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_inner_shaft_socket(self) -> '_2141.InnerShaftSocket':
        '''InnerShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2141.InnerShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to InnerShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_inner_shaft_socket_base(self) -> '_2142.InnerShaftSocketBase':
        '''InnerShaftSocketBase: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2142.InnerShaftSocketBase.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to InnerShaftSocketBase. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_mountable_component_inner_socket(self) -> '_2144.MountableComponentInnerSocket':
        '''MountableComponentInnerSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2144.MountableComponentInnerSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to MountableComponentInnerSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_mountable_component_outer_socket(self) -> '_2145.MountableComponentOuterSocket':
        '''MountableComponentOuterSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2145.MountableComponentOuterSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to MountableComponentOuterSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_mountable_component_socket(self) -> '_2146.MountableComponentSocket':
        '''MountableComponentSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2146.MountableComponentSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to MountableComponentSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_outer_shaft_socket(self) -> '_2147.OuterShaftSocket':
        '''OuterShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2147.OuterShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to OuterShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_outer_shaft_socket_base(self) -> '_2148.OuterShaftSocketBase':
        '''OuterShaftSocketBase: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2148.OuterShaftSocketBase.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to OuterShaftSocketBase. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_planetary_socket(self) -> '_2150.PlanetarySocket':
        '''PlanetarySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2150.PlanetarySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PlanetarySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_planetary_socket_base(self) -> '_2151.PlanetarySocketBase':
        '''PlanetarySocketBase: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2151.PlanetarySocketBase.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PlanetarySocketBase. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_pulley_socket(self) -> '_2152.PulleySocket':
        '''PulleySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2152.PulleySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PulleySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_rolling_ring_socket(self) -> '_2155.RollingRingSocket':
        '''RollingRingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2155.RollingRingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to RollingRingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_shaft_socket(self) -> '_2156.ShaftSocket':
        '''ShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2156.ShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_2162.AGMAGleasonConicalGearTeethSocket':
        '''AGMAGleasonConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2162.AGMAGleasonConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_bevel_differential_gear_teeth_socket(self) -> '_2164.BevelDifferentialGearTeethSocket':
        '''BevelDifferentialGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2164.BevelDifferentialGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BevelDifferentialGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_bevel_gear_teeth_socket(self) -> '_2166.BevelGearTeethSocket':
        '''BevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2166.BevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_concept_gear_teeth_socket(self) -> '_2168.ConceptGearTeethSocket':
        '''ConceptGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2168.ConceptGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConceptGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_conical_gear_teeth_socket(self) -> '_2170.ConicalGearTeethSocket':
        '''ConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2170.ConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_cylindrical_gear_teeth_socket(self) -> '_2172.CylindricalGearTeethSocket':
        '''CylindricalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2172.CylindricalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CylindricalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_face_gear_teeth_socket(self) -> '_2174.FaceGearTeethSocket':
        '''FaceGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2174.FaceGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to FaceGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_gear_teeth_socket(self) -> '_2176.GearTeethSocket':
        '''GearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2176.GearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to GearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_hypoid_gear_teeth_socket(self) -> '_2178.HypoidGearTeethSocket':
        '''HypoidGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2178.HypoidGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to HypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_2179.KlingelnbergConicalGearTeethSocket':
        '''KlingelnbergConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.KlingelnbergConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_2183.KlingelnbergHypoidGearTeethSocket':
        '''KlingelnbergHypoidGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2183.KlingelnbergHypoidGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_2184.KlingelnbergSpiralBevelGearTeethSocket':
        '''KlingelnbergSpiralBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2184.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_spiral_bevel_gear_teeth_socket(self) -> '_2186.SpiralBevelGearTeethSocket':
        '''SpiralBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2186.SpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to SpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_2188.StraightBevelDiffGearTeethSocket':
        '''StraightBevelDiffGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2188.StraightBevelDiffGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_straight_bevel_gear_teeth_socket(self) -> '_2190.StraightBevelGearTeethSocket':
        '''StraightBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2190.StraightBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to StraightBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_worm_gear_teeth_socket(self) -> '_2192.WormGearTeethSocket':
        '''WormGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2192.WormGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to WormGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_zerol_bevel_gear_teeth_socket(self) -> '_2194.ZerolBevelGearTeethSocket':
        '''ZerolBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2194.ZerolBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ZerolBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_cycloidal_disc_axial_left_socket(self) -> '_2195.CycloidalDiscAxialLeftSocket':
        '''CycloidalDiscAxialLeftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2195.CycloidalDiscAxialLeftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_cycloidal_disc_axial_right_socket(self) -> '_2196.CycloidalDiscAxialRightSocket':
        '''CycloidalDiscAxialRightSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2196.CycloidalDiscAxialRightSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscAxialRightSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_cycloidal_disc_inner_socket(self) -> '_2198.CycloidalDiscInnerSocket':
        '''CycloidalDiscInnerSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2198.CycloidalDiscInnerSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscInnerSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_cycloidal_disc_outer_socket(self) -> '_2199.CycloidalDiscOuterSocket':
        '''CycloidalDiscOuterSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2199.CycloidalDiscOuterSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscOuterSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2201.CycloidalDiscPlanetaryBearingSocket':
        '''CycloidalDiscPlanetaryBearingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2201.CycloidalDiscPlanetaryBearingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_ring_pins_socket(self) -> '_2202.RingPinsSocket':
        '''RingPinsSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2202.RingPinsSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to RingPinsSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_clutch_socket(self) -> '_2205.ClutchSocket':
        '''ClutchSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2205.ClutchSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ClutchSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_concept_coupling_socket(self) -> '_2207.ConceptCouplingSocket':
        '''ConceptCouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2207.ConceptCouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConceptCouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_coupling_socket(self) -> '_2209.CouplingSocket':
        '''CouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2209.CouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_part_to_part_shear_coupling_socket(self) -> '_2211.PartToPartShearCouplingSocket':
        '''PartToPartShearCouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2211.PartToPartShearCouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PartToPartShearCouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_spring_damper_socket(self) -> '_2213.SpringDamperSocket':
        '''SpringDamperSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2213.SpringDamperSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to SpringDamperSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_torque_converter_pump_socket(self) -> '_2215.TorqueConverterPumpSocket':
        '''TorqueConverterPumpSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2215.TorqueConverterPumpSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to TorqueConverterPumpSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_a_of_type_torque_converter_turbine_socket(self) -> '_2216.TorqueConverterTurbineSocket':
        '''TorqueConverterTurbineSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2216.TorqueConverterTurbineSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to TorqueConverterTurbineSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA is not None else None

    @property
    def socket_b(self) -> '_2158.Socket':
        '''Socket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2158.Socket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to Socket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_bearing_inner_socket(self) -> '_2128.BearingInnerSocket':
        '''BearingInnerSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2128.BearingInnerSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BearingInnerSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_bearing_outer_socket(self) -> '_2129.BearingOuterSocket':
        '''BearingOuterSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2129.BearingOuterSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BearingOuterSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_cvt_pulley_socket(self) -> '_2136.CVTPulleySocket':
        '''CVTPulleySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2136.CVTPulleySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CVTPulleySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_cylindrical_socket(self) -> '_2138.CylindricalSocket':
        '''CylindricalSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2138.CylindricalSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CylindricalSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_electric_machine_stator_socket(self) -> '_2140.ElectricMachineStatorSocket':
        '''ElectricMachineStatorSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2140.ElectricMachineStatorSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ElectricMachineStatorSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_inner_shaft_socket(self) -> '_2141.InnerShaftSocket':
        '''InnerShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2141.InnerShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to InnerShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_inner_shaft_socket_base(self) -> '_2142.InnerShaftSocketBase':
        '''InnerShaftSocketBase: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2142.InnerShaftSocketBase.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to InnerShaftSocketBase. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_mountable_component_inner_socket(self) -> '_2144.MountableComponentInnerSocket':
        '''MountableComponentInnerSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2144.MountableComponentInnerSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to MountableComponentInnerSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_mountable_component_outer_socket(self) -> '_2145.MountableComponentOuterSocket':
        '''MountableComponentOuterSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2145.MountableComponentOuterSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to MountableComponentOuterSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_mountable_component_socket(self) -> '_2146.MountableComponentSocket':
        '''MountableComponentSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2146.MountableComponentSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to MountableComponentSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_outer_shaft_socket(self) -> '_2147.OuterShaftSocket':
        '''OuterShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2147.OuterShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to OuterShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_outer_shaft_socket_base(self) -> '_2148.OuterShaftSocketBase':
        '''OuterShaftSocketBase: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2148.OuterShaftSocketBase.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to OuterShaftSocketBase. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_planetary_socket(self) -> '_2150.PlanetarySocket':
        '''PlanetarySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2150.PlanetarySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PlanetarySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_planetary_socket_base(self) -> '_2151.PlanetarySocketBase':
        '''PlanetarySocketBase: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2151.PlanetarySocketBase.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PlanetarySocketBase. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_pulley_socket(self) -> '_2152.PulleySocket':
        '''PulleySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2152.PulleySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PulleySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_rolling_ring_socket(self) -> '_2155.RollingRingSocket':
        '''RollingRingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2155.RollingRingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to RollingRingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_shaft_socket(self) -> '_2156.ShaftSocket':
        '''ShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2156.ShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_2162.AGMAGleasonConicalGearTeethSocket':
        '''AGMAGleasonConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2162.AGMAGleasonConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_bevel_differential_gear_teeth_socket(self) -> '_2164.BevelDifferentialGearTeethSocket':
        '''BevelDifferentialGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2164.BevelDifferentialGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BevelDifferentialGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_bevel_gear_teeth_socket(self) -> '_2166.BevelGearTeethSocket':
        '''BevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2166.BevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_concept_gear_teeth_socket(self) -> '_2168.ConceptGearTeethSocket':
        '''ConceptGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2168.ConceptGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConceptGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_conical_gear_teeth_socket(self) -> '_2170.ConicalGearTeethSocket':
        '''ConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2170.ConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_cylindrical_gear_teeth_socket(self) -> '_2172.CylindricalGearTeethSocket':
        '''CylindricalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2172.CylindricalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CylindricalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_face_gear_teeth_socket(self) -> '_2174.FaceGearTeethSocket':
        '''FaceGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2174.FaceGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to FaceGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_gear_teeth_socket(self) -> '_2176.GearTeethSocket':
        '''GearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2176.GearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to GearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_hypoid_gear_teeth_socket(self) -> '_2178.HypoidGearTeethSocket':
        '''HypoidGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2178.HypoidGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to HypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_2179.KlingelnbergConicalGearTeethSocket':
        '''KlingelnbergConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.KlingelnbergConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_2183.KlingelnbergHypoidGearTeethSocket':
        '''KlingelnbergHypoidGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2183.KlingelnbergHypoidGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_2184.KlingelnbergSpiralBevelGearTeethSocket':
        '''KlingelnbergSpiralBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2184.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_spiral_bevel_gear_teeth_socket(self) -> '_2186.SpiralBevelGearTeethSocket':
        '''SpiralBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2186.SpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to SpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_2188.StraightBevelDiffGearTeethSocket':
        '''StraightBevelDiffGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2188.StraightBevelDiffGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_straight_bevel_gear_teeth_socket(self) -> '_2190.StraightBevelGearTeethSocket':
        '''StraightBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2190.StraightBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to StraightBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_worm_gear_teeth_socket(self) -> '_2192.WormGearTeethSocket':
        '''WormGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2192.WormGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to WormGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_zerol_bevel_gear_teeth_socket(self) -> '_2194.ZerolBevelGearTeethSocket':
        '''ZerolBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2194.ZerolBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ZerolBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_cycloidal_disc_axial_left_socket(self) -> '_2195.CycloidalDiscAxialLeftSocket':
        '''CycloidalDiscAxialLeftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2195.CycloidalDiscAxialLeftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_cycloidal_disc_axial_right_socket(self) -> '_2196.CycloidalDiscAxialRightSocket':
        '''CycloidalDiscAxialRightSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2196.CycloidalDiscAxialRightSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscAxialRightSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_cycloidal_disc_inner_socket(self) -> '_2198.CycloidalDiscInnerSocket':
        '''CycloidalDiscInnerSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2198.CycloidalDiscInnerSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscInnerSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_cycloidal_disc_outer_socket(self) -> '_2199.CycloidalDiscOuterSocket':
        '''CycloidalDiscOuterSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2199.CycloidalDiscOuterSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscOuterSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2201.CycloidalDiscPlanetaryBearingSocket':
        '''CycloidalDiscPlanetaryBearingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2201.CycloidalDiscPlanetaryBearingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_ring_pins_socket(self) -> '_2202.RingPinsSocket':
        '''RingPinsSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2202.RingPinsSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to RingPinsSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_clutch_socket(self) -> '_2205.ClutchSocket':
        '''ClutchSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2205.ClutchSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ClutchSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_concept_coupling_socket(self) -> '_2207.ConceptCouplingSocket':
        '''ConceptCouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2207.ConceptCouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConceptCouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_coupling_socket(self) -> '_2209.CouplingSocket':
        '''CouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2209.CouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_part_to_part_shear_coupling_socket(self) -> '_2211.PartToPartShearCouplingSocket':
        '''PartToPartShearCouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2211.PartToPartShearCouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PartToPartShearCouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_spring_damper_socket(self) -> '_2213.SpringDamperSocket':
        '''SpringDamperSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2213.SpringDamperSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to SpringDamperSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_torque_converter_pump_socket(self) -> '_2215.TorqueConverterPumpSocket':
        '''TorqueConverterPumpSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2215.TorqueConverterPumpSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to TorqueConverterPumpSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def socket_b_of_type_torque_converter_turbine_socket(self) -> '_2216.TorqueConverterTurbineSocket':
        '''TorqueConverterTurbineSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2216.TorqueConverterTurbineSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to TorqueConverterTurbineSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB is not None else None

    @property
    def connection(self) -> '_2134.Connection':
        '''Connection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2134.Connection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to Connection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_abstract_shaft_to_mountable_component_connection(self) -> '_2127.AbstractShaftToMountableComponentConnection':
        '''AbstractShaftToMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2127.AbstractShaftToMountableComponentConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to AbstractShaftToMountableComponentConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_belt_connection(self) -> '_2130.BeltConnection':
        '''BeltConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2130.BeltConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BeltConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_coaxial_connection(self) -> '_2131.CoaxialConnection':
        '''CoaxialConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2131.CoaxialConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CoaxialConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_cvt_belt_connection(self) -> '_2135.CVTBeltConnection':
        '''CVTBeltConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2135.CVTBeltConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CVTBeltConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_inter_mountable_component_connection(self) -> '_2143.InterMountableComponentConnection':
        '''InterMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2143.InterMountableComponentConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to InterMountableComponentConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_planetary_connection(self) -> '_2149.PlanetaryConnection':
        '''PlanetaryConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2149.PlanetaryConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to PlanetaryConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_rolling_ring_connection(self) -> '_2154.RollingRingConnection':
        '''RollingRingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2154.RollingRingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to RollingRingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_shaft_to_mountable_component_connection(self) -> '_2157.ShaftToMountableComponentConnection':
        '''ShaftToMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2157.ShaftToMountableComponentConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ShaftToMountableComponentConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_agma_gleason_conical_gear_mesh(self) -> '_2161.AGMAGleasonConicalGearMesh':
        '''AGMAGleasonConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2161.AGMAGleasonConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to AGMAGleasonConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_bevel_differential_gear_mesh(self) -> '_2163.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2163.BevelDifferentialGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BevelDifferentialGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_bevel_gear_mesh(self) -> '_2165.BevelGearMesh':
        '''BevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2165.BevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_concept_gear_mesh(self) -> '_2167.ConceptGearMesh':
        '''ConceptGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2167.ConceptGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConceptGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_conical_gear_mesh(self) -> '_2169.ConicalGearMesh':
        '''ConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2169.ConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_cylindrical_gear_mesh(self) -> '_2171.CylindricalGearMesh':
        '''CylindricalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2171.CylindricalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CylindricalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_face_gear_mesh(self) -> '_2173.FaceGearMesh':
        '''FaceGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2173.FaceGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to FaceGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_gear_mesh(self) -> '_2175.GearMesh':
        '''GearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2175.GearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to GearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_hypoid_gear_mesh(self) -> '_2177.HypoidGearMesh':
        '''HypoidGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2177.HypoidGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to HypoidGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_2180.KlingelnbergCycloPalloidConicalGearMesh':
        '''KlingelnbergCycloPalloidConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2180.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2181.KlingelnbergCycloPalloidHypoidGearMesh':
        '''KlingelnbergCycloPalloidHypoidGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2181.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2182.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        '''KlingelnbergCycloPalloidSpiralBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2182.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_spiral_bevel_gear_mesh(self) -> '_2185.SpiralBevelGearMesh':
        '''SpiralBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2185.SpiralBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to SpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_straight_bevel_diff_gear_mesh(self) -> '_2187.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2187.StraightBevelDiffGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to StraightBevelDiffGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_straight_bevel_gear_mesh(self) -> '_2189.StraightBevelGearMesh':
        '''StraightBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2189.StraightBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to StraightBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_worm_gear_mesh(self) -> '_2191.WormGearMesh':
        '''WormGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2191.WormGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to WormGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_zerol_bevel_gear_mesh(self) -> '_2193.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2193.ZerolBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ZerolBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_cycloidal_disc_central_bearing_connection(self) -> '_2197.CycloidalDiscCentralBearingConnection':
        '''CycloidalDiscCentralBearingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2197.CycloidalDiscCentralBearingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CycloidalDiscCentralBearingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_cycloidal_disc_planetary_bearing_connection(self) -> '_2200.CycloidalDiscPlanetaryBearingConnection':
        '''CycloidalDiscPlanetaryBearingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2200.CycloidalDiscPlanetaryBearingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CycloidalDiscPlanetaryBearingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_ring_pins_to_disc_connection(self) -> '_2203.RingPinsToDiscConnection':
        '''RingPinsToDiscConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2203.RingPinsToDiscConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to RingPinsToDiscConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_clutch_connection(self) -> '_2204.ClutchConnection':
        '''ClutchConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2204.ClutchConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ClutchConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_concept_coupling_connection(self) -> '_2206.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2206.ConceptCouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConceptCouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_coupling_connection(self) -> '_2208.CouplingConnection':
        '''CouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2208.CouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_part_to_part_shear_coupling_connection(self) -> '_2210.PartToPartShearCouplingConnection':
        '''PartToPartShearCouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2210.PartToPartShearCouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to PartToPartShearCouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_spring_damper_connection(self) -> '_2212.SpringDamperConnection':
        '''SpringDamperConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2212.SpringDamperConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to SpringDamperConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None

    @property
    def connection_of_type_torque_converter_connection(self) -> '_2214.TorqueConverterConnection':
        '''TorqueConverterConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2214.TorqueConverterConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to TorqueConverterConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection is not None else None
