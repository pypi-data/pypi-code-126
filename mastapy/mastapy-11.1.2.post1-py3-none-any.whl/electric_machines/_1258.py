'''_1258.py

UShapedLayerSpecification
'''


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines import _1231, _1230, _1246
from mastapy._internal.python_net import python_net_import

_U_SHAPED_LAYER_SPECIFICATION = python_net_import('SMT.MastaAPI.ElectricMachines', 'UShapedLayerSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('UShapedLayerSpecification',)


class UShapedLayerSpecification(_1246.RotorInternalLayerSpecification):
    '''UShapedLayerSpecification

    This is a mastapy class.
    '''

    TYPE = _U_SHAPED_LAYER_SPECIFICATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UShapedLayerSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_to_layer(self) -> 'float':
        '''float: 'DistanceToLayer' is the original name of this property.'''

        return self.wrapped.DistanceToLayer

    @distance_to_layer.setter
    def distance_to_layer(self, value: 'float'):
        self.wrapped.DistanceToLayer = float(value) if value else 0.0

    @property
    def web_thickness(self) -> 'float':
        '''float: 'WebThickness' is the original name of this property.'''

        return self.wrapped.WebThickness

    @web_thickness.setter
    def web_thickness(self, value: 'float'):
        self.wrapped.WebThickness = float(value) if value else 0.0

    @property
    def angle_between_inner_and_outer_sections(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'AngleBetweenInnerAndOuterSections' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.AngleBetweenInnerAndOuterSections) if self.wrapped.AngleBetweenInnerAndOuterSections is not None else None

    @angle_between_inner_and_outer_sections.setter
    def angle_between_inner_and_outer_sections(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AngleBetweenInnerAndOuterSections = value

    @property
    def bridge_thickness_at_layer_bend(self) -> 'float':
        '''float: 'BridgeThicknessAtLayerBend' is the original name of this property.'''

        return self.wrapped.BridgeThicknessAtLayerBend

    @bridge_thickness_at_layer_bend.setter
    def bridge_thickness_at_layer_bend(self, value: 'float'):
        self.wrapped.BridgeThicknessAtLayerBend = float(value) if value else 0.0

    @property
    def bridge_offset_at_layer_bend(self) -> 'float':
        '''float: 'BridgeOffsetAtLayerBend' is the original name of this property.'''

        return self.wrapped.BridgeOffsetAtLayerBend

    @bridge_offset_at_layer_bend.setter
    def bridge_offset_at_layer_bend(self, value: 'float'):
        self.wrapped.BridgeOffsetAtLayerBend = float(value) if value else 0.0

    @property
    def thickness_of_inner_flux_barriers(self) -> 'float':
        '''float: 'ThicknessOfInnerFluxBarriers' is the original name of this property.'''

        return self.wrapped.ThicknessOfInnerFluxBarriers

    @thickness_of_inner_flux_barriers.setter
    def thickness_of_inner_flux_barriers(self, value: 'float'):
        self.wrapped.ThicknessOfInnerFluxBarriers = float(value) if value else 0.0

    @property
    def thickness_of_outer_flux_barriers(self) -> 'float':
        '''float: 'ThicknessOfOuterFluxBarriers' is the original name of this property.'''

        return self.wrapped.ThicknessOfOuterFluxBarriers

    @thickness_of_outer_flux_barriers.setter
    def thickness_of_outer_flux_barriers(self, value: 'float'):
        self.wrapped.ThicknessOfOuterFluxBarriers = float(value) if value else 0.0

    @property
    def magnet_configuration(self) -> '_1231.MagnetConfiguration':
        '''MagnetConfiguration: 'MagnetConfiguration' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.MagnetConfiguration)
        return constructor.new(_1231.MagnetConfiguration)(value) if value is not None else None

    @magnet_configuration.setter
    def magnet_configuration(self, value: '_1231.MagnetConfiguration'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MagnetConfiguration = value

    @property
    def outer_magnet(self) -> '_1230.Magnet':
        '''Magnet: 'OuterMagnet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1230.Magnet)(self.wrapped.OuterMagnet) if self.wrapped.OuterMagnet is not None else None
