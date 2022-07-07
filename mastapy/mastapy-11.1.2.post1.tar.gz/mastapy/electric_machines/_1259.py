'''_1259.py

VShapedMagnetLayerSpecification
'''


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines import _1222, _1246
from mastapy._internal.python_net import python_net_import

_V_SHAPED_MAGNET_LAYER_SPECIFICATION = python_net_import('SMT.MastaAPI.ElectricMachines', 'VShapedMagnetLayerSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('VShapedMagnetLayerSpecification',)


class VShapedMagnetLayerSpecification(_1246.RotorInternalLayerSpecification):
    '''VShapedMagnetLayerSpecification

    This is a mastapy class.
    '''

    TYPE = _V_SHAPED_MAGNET_LAYER_SPECIFICATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'VShapedMagnetLayerSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def v_shaped_angle(self) -> 'float':
        '''float: 'VShapedAngle' is the original name of this property.'''

        return self.wrapped.VShapedAngle

    @v_shaped_angle.setter
    def v_shaped_angle(self, value: 'float'):
        self.wrapped.VShapedAngle = float(value) if value else 0.0

    @property
    def distance_to_v_shape(self) -> 'float':
        '''float: 'DistanceToVShape' is the original name of this property.'''

        return self.wrapped.DistanceToVShape

    @distance_to_v_shape.setter
    def distance_to_v_shape(self, value: 'float'):
        self.wrapped.DistanceToVShape = float(value) if value else 0.0

    @property
    def flux_barrier_length(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'FluxBarrierLength' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.FluxBarrierLength) if self.wrapped.FluxBarrierLength is not None else None

    @flux_barrier_length.setter
    def flux_barrier_length(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FluxBarrierLength = value

    @property
    def has_flux_barriers(self) -> 'bool':
        '''bool: 'HasFluxBarriers' is the original name of this property.'''

        return self.wrapped.HasFluxBarriers

    @has_flux_barriers.setter
    def has_flux_barriers(self, value: 'bool'):
        self.wrapped.HasFluxBarriers = bool(value) if value else False

    @property
    def distance_between_magnets(self) -> 'float':
        '''float: 'DistanceBetweenMagnets' is the original name of this property.'''

        return self.wrapped.DistanceBetweenMagnets

    @distance_between_magnets.setter
    def distance_between_magnets(self, value: 'float'):
        self.wrapped.DistanceBetweenMagnets = float(value) if value else 0.0

    @property
    def upper_flux_barrier_web_specification(self) -> '_1222.FluxBarrierOrWeb':
        '''FluxBarrierOrWeb: 'UpperFluxBarrierWebSpecification' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.UpperFluxBarrierWebSpecification)
        return constructor.new(_1222.FluxBarrierOrWeb)(value) if value is not None else None

    @upper_flux_barrier_web_specification.setter
    def upper_flux_barrier_web_specification(self, value: '_1222.FluxBarrierOrWeb'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.UpperFluxBarrierWebSpecification = value

    @property
    def web_thickness(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'WebThickness' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.WebThickness) if self.wrapped.WebThickness is not None else None

    @web_thickness.setter
    def web_thickness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.WebThickness = value

    @property
    def web_length(self) -> 'float':
        '''float: 'WebLength' is the original name of this property.'''

        return self.wrapped.WebLength

    @web_length.setter
    def web_length(self, value: 'float'):
        self.wrapped.WebLength = float(value) if value else 0.0

    @property
    def upper_round_height(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'UpperRoundHeight' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.UpperRoundHeight) if self.wrapped.UpperRoundHeight is not None else None

    @upper_round_height.setter
    def upper_round_height(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.UpperRoundHeight = value

    @property
    def lower_round_height(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'LowerRoundHeight' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.LowerRoundHeight) if self.wrapped.LowerRoundHeight is not None else None

    @lower_round_height.setter
    def lower_round_height(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.LowerRoundHeight = value
