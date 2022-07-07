'''_2325.py

MountableComponent
'''


from typing import Optional

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import (
    _2138, _2128, _2129, _2136,
    _2141, _2142, _2144, _2145,
    _2146, _2147, _2148, _2150,
    _2151, _2152, _2155, _2156,
    _2134, _2127, _2130, _2131,
    _2135, _2143, _2149, _2154,
    _2157
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.gears import (
    _2172, _2161, _2163, _2165,
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
from mastapy.system_model.part_model import _2298, _2307, _2306
from mastapy.system_model.part_model.shaft_model import _2343
from mastapy.system_model.part_model.cycloidal import _2429
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MountableComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponent',)


class MountableComponent(_2306.Component):
    '''MountableComponent

    This is a mastapy class.
    '''

    TYPE = _MOUNTABLE_COMPONENT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MountableComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotation_about_axis(self) -> 'float':
        '''float: 'RotationAboutAxis' is the original name of this property.'''

        return self.wrapped.RotationAboutAxis

    @rotation_about_axis.setter
    def rotation_about_axis(self, value: 'float'):
        self.wrapped.RotationAboutAxis = float(value) if value else 0.0

    @property
    def inner_socket(self) -> '_2138.CylindricalSocket':
        '''CylindricalSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2138.CylindricalSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CylindricalSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_bearing_inner_socket(self) -> '_2128.BearingInnerSocket':
        '''BearingInnerSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2128.BearingInnerSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to BearingInnerSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_bearing_outer_socket(self) -> '_2129.BearingOuterSocket':
        '''BearingOuterSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2129.BearingOuterSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to BearingOuterSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_cvt_pulley_socket(self) -> '_2136.CVTPulleySocket':
        '''CVTPulleySocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2136.CVTPulleySocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CVTPulleySocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_inner_shaft_socket(self) -> '_2141.InnerShaftSocket':
        '''InnerShaftSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2141.InnerShaftSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to InnerShaftSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_inner_shaft_socket_base(self) -> '_2142.InnerShaftSocketBase':
        '''InnerShaftSocketBase: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2142.InnerShaftSocketBase.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to InnerShaftSocketBase. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_mountable_component_inner_socket(self) -> '_2144.MountableComponentInnerSocket':
        '''MountableComponentInnerSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2144.MountableComponentInnerSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to MountableComponentInnerSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_mountable_component_outer_socket(self) -> '_2145.MountableComponentOuterSocket':
        '''MountableComponentOuterSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2145.MountableComponentOuterSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to MountableComponentOuterSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_mountable_component_socket(self) -> '_2146.MountableComponentSocket':
        '''MountableComponentSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2146.MountableComponentSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to MountableComponentSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_outer_shaft_socket(self) -> '_2147.OuterShaftSocket':
        '''OuterShaftSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2147.OuterShaftSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to OuterShaftSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_outer_shaft_socket_base(self) -> '_2148.OuterShaftSocketBase':
        '''OuterShaftSocketBase: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2148.OuterShaftSocketBase.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to OuterShaftSocketBase. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_planetary_socket(self) -> '_2150.PlanetarySocket':
        '''PlanetarySocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2150.PlanetarySocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to PlanetarySocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_planetary_socket_base(self) -> '_2151.PlanetarySocketBase':
        '''PlanetarySocketBase: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2151.PlanetarySocketBase.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to PlanetarySocketBase. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_pulley_socket(self) -> '_2152.PulleySocket':
        '''PulleySocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2152.PulleySocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to PulleySocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_rolling_ring_socket(self) -> '_2155.RollingRingSocket':
        '''RollingRingSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2155.RollingRingSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to RollingRingSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_shaft_socket(self) -> '_2156.ShaftSocket':
        '''ShaftSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2156.ShaftSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to ShaftSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_cylindrical_gear_teeth_socket(self) -> '_2172.CylindricalGearTeethSocket':
        '''CylindricalGearTeethSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2172.CylindricalGearTeethSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CylindricalGearTeethSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_cycloidal_disc_axial_left_socket(self) -> '_2195.CycloidalDiscAxialLeftSocket':
        '''CycloidalDiscAxialLeftSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2195.CycloidalDiscAxialLeftSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_cycloidal_disc_axial_right_socket(self) -> '_2196.CycloidalDiscAxialRightSocket':
        '''CycloidalDiscAxialRightSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2196.CycloidalDiscAxialRightSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CycloidalDiscAxialRightSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_cycloidal_disc_inner_socket(self) -> '_2198.CycloidalDiscInnerSocket':
        '''CycloidalDiscInnerSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2198.CycloidalDiscInnerSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CycloidalDiscInnerSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_cycloidal_disc_outer_socket(self) -> '_2199.CycloidalDiscOuterSocket':
        '''CycloidalDiscOuterSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2199.CycloidalDiscOuterSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CycloidalDiscOuterSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2201.CycloidalDiscPlanetaryBearingSocket':
        '''CycloidalDiscPlanetaryBearingSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2201.CycloidalDiscPlanetaryBearingSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_ring_pins_socket(self) -> '_2202.RingPinsSocket':
        '''RingPinsSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2202.RingPinsSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to RingPinsSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_clutch_socket(self) -> '_2205.ClutchSocket':
        '''ClutchSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2205.ClutchSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to ClutchSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_concept_coupling_socket(self) -> '_2207.ConceptCouplingSocket':
        '''ConceptCouplingSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2207.ConceptCouplingSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to ConceptCouplingSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_coupling_socket(self) -> '_2209.CouplingSocket':
        '''CouplingSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2209.CouplingSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CouplingSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_part_to_part_shear_coupling_socket(self) -> '_2211.PartToPartShearCouplingSocket':
        '''PartToPartShearCouplingSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2211.PartToPartShearCouplingSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to PartToPartShearCouplingSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_spring_damper_socket(self) -> '_2213.SpringDamperSocket':
        '''SpringDamperSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2213.SpringDamperSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to SpringDamperSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_torque_converter_pump_socket(self) -> '_2215.TorqueConverterPumpSocket':
        '''TorqueConverterPumpSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2215.TorqueConverterPumpSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to TorqueConverterPumpSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_socket_of_type_torque_converter_turbine_socket(self) -> '_2216.TorqueConverterTurbineSocket':
        '''TorqueConverterTurbineSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2216.TorqueConverterTurbineSocket.TYPE not in self.wrapped.InnerSocket.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to TorqueConverterTurbineSocket. Expected: {}.'.format(self.wrapped.InnerSocket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerSocket.__class__)(self.wrapped.InnerSocket) if self.wrapped.InnerSocket is not None else None

    @property
    def inner_connection(self) -> '_2134.Connection':
        '''Connection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2134.Connection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to Connection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_abstract_shaft_to_mountable_component_connection(self) -> '_2127.AbstractShaftToMountableComponentConnection':
        '''AbstractShaftToMountableComponentConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2127.AbstractShaftToMountableComponentConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to AbstractShaftToMountableComponentConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_belt_connection(self) -> '_2130.BeltConnection':
        '''BeltConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2130.BeltConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to BeltConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_coaxial_connection(self) -> '_2131.CoaxialConnection':
        '''CoaxialConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2131.CoaxialConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CoaxialConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_cvt_belt_connection(self) -> '_2135.CVTBeltConnection':
        '''CVTBeltConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2135.CVTBeltConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CVTBeltConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_inter_mountable_component_connection(self) -> '_2143.InterMountableComponentConnection':
        '''InterMountableComponentConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2143.InterMountableComponentConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to InterMountableComponentConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_planetary_connection(self) -> '_2149.PlanetaryConnection':
        '''PlanetaryConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2149.PlanetaryConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to PlanetaryConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_rolling_ring_connection(self) -> '_2154.RollingRingConnection':
        '''RollingRingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2154.RollingRingConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to RollingRingConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_shaft_to_mountable_component_connection(self) -> '_2157.ShaftToMountableComponentConnection':
        '''ShaftToMountableComponentConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2157.ShaftToMountableComponentConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ShaftToMountableComponentConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_agma_gleason_conical_gear_mesh(self) -> '_2161.AGMAGleasonConicalGearMesh':
        '''AGMAGleasonConicalGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2161.AGMAGleasonConicalGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to AGMAGleasonConicalGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_bevel_differential_gear_mesh(self) -> '_2163.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2163.BevelDifferentialGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to BevelDifferentialGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_bevel_gear_mesh(self) -> '_2165.BevelGearMesh':
        '''BevelGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2165.BevelGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to BevelGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_concept_gear_mesh(self) -> '_2167.ConceptGearMesh':
        '''ConceptGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2167.ConceptGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ConceptGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_conical_gear_mesh(self) -> '_2169.ConicalGearMesh':
        '''ConicalGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2169.ConicalGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ConicalGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_cylindrical_gear_mesh(self) -> '_2171.CylindricalGearMesh':
        '''CylindricalGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2171.CylindricalGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CylindricalGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_face_gear_mesh(self) -> '_2173.FaceGearMesh':
        '''FaceGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2173.FaceGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to FaceGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_gear_mesh(self) -> '_2175.GearMesh':
        '''GearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2175.GearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to GearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_hypoid_gear_mesh(self) -> '_2177.HypoidGearMesh':
        '''HypoidGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2177.HypoidGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to HypoidGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_2180.KlingelnbergCycloPalloidConicalGearMesh':
        '''KlingelnbergCycloPalloidConicalGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2180.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2181.KlingelnbergCycloPalloidHypoidGearMesh':
        '''KlingelnbergCycloPalloidHypoidGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2181.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2182.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        '''KlingelnbergCycloPalloidSpiralBevelGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2182.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_spiral_bevel_gear_mesh(self) -> '_2185.SpiralBevelGearMesh':
        '''SpiralBevelGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2185.SpiralBevelGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to SpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_straight_bevel_diff_gear_mesh(self) -> '_2187.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2187.StraightBevelDiffGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to StraightBevelDiffGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_straight_bevel_gear_mesh(self) -> '_2189.StraightBevelGearMesh':
        '''StraightBevelGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2189.StraightBevelGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to StraightBevelGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_worm_gear_mesh(self) -> '_2191.WormGearMesh':
        '''WormGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2191.WormGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to WormGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_zerol_bevel_gear_mesh(self) -> '_2193.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2193.ZerolBevelGearMesh.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ZerolBevelGearMesh. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_cycloidal_disc_central_bearing_connection(self) -> '_2197.CycloidalDiscCentralBearingConnection':
        '''CycloidalDiscCentralBearingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2197.CycloidalDiscCentralBearingConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CycloidalDiscCentralBearingConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_cycloidal_disc_planetary_bearing_connection(self) -> '_2200.CycloidalDiscPlanetaryBearingConnection':
        '''CycloidalDiscPlanetaryBearingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2200.CycloidalDiscPlanetaryBearingConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CycloidalDiscPlanetaryBearingConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_ring_pins_to_disc_connection(self) -> '_2203.RingPinsToDiscConnection':
        '''RingPinsToDiscConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2203.RingPinsToDiscConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to RingPinsToDiscConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_clutch_connection(self) -> '_2204.ClutchConnection':
        '''ClutchConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2204.ClutchConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ClutchConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_concept_coupling_connection(self) -> '_2206.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2206.ConceptCouplingConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ConceptCouplingConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_coupling_connection(self) -> '_2208.CouplingConnection':
        '''CouplingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2208.CouplingConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CouplingConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_part_to_part_shear_coupling_connection(self) -> '_2210.PartToPartShearCouplingConnection':
        '''PartToPartShearCouplingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2210.PartToPartShearCouplingConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to PartToPartShearCouplingConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_spring_damper_connection(self) -> '_2212.SpringDamperConnection':
        '''SpringDamperConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2212.SpringDamperConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to SpringDamperConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def inner_connection_of_type_torque_converter_connection(self) -> '_2214.TorqueConverterConnection':
        '''TorqueConverterConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2214.TorqueConverterConnection.TYPE not in self.wrapped.InnerConnection.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to TorqueConverterConnection. Expected: {}.'.format(self.wrapped.InnerConnection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerConnection.__class__)(self.wrapped.InnerConnection) if self.wrapped.InnerConnection is not None else None

    @property
    def is_mounted(self) -> 'bool':
        '''bool: 'IsMounted' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.IsMounted

    @property
    def inner_component(self) -> '_2298.AbstractShaft':
        '''AbstractShaft: 'InnerComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2298.AbstractShaft.TYPE not in self.wrapped.InnerComponent.__class__.__mro__:
            raise CastException('Failed to cast inner_component to AbstractShaft. Expected: {}.'.format(self.wrapped.InnerComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerComponent.__class__)(self.wrapped.InnerComponent) if self.wrapped.InnerComponent is not None else None

    @property
    def inner_component_of_type_shaft(self) -> '_2343.Shaft':
        '''Shaft: 'InnerComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2343.Shaft.TYPE not in self.wrapped.InnerComponent.__class__.__mro__:
            raise CastException('Failed to cast inner_component to Shaft. Expected: {}.'.format(self.wrapped.InnerComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerComponent.__class__)(self.wrapped.InnerComponent) if self.wrapped.InnerComponent is not None else None

    @property
    def inner_component_of_type_cycloidal_disc(self) -> '_2429.CycloidalDisc':
        '''CycloidalDisc: 'InnerComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2429.CycloidalDisc.TYPE not in self.wrapped.InnerComponent.__class__.__mro__:
            raise CastException('Failed to cast inner_component to CycloidalDisc. Expected: {}.'.format(self.wrapped.InnerComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerComponent.__class__)(self.wrapped.InnerComponent) if self.wrapped.InnerComponent is not None else None

    def try_mount_on(self, shaft: '_2298.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2307.ComponentsConnectedResult':
        ''' 'TryMountOn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        '''

        offset = float(offset)
        method_result = self.wrapped.TryMountOn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def mount_on(self, shaft: '_2298.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2131.CoaxialConnection':
        ''' 'MountOn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.connections_and_sockets.CoaxialConnection
        '''

        offset = float(offset)
        method_result = self.wrapped.MountOn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None
