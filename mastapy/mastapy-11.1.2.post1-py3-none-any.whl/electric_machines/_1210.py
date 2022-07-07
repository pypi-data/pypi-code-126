'''_1210.py

ElectricMachineMeshingOptions
'''


from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.nodal_analysis import _57
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_MESHING_OPTIONS = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineMeshingOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineMeshingOptions',)


class ElectricMachineMeshingOptions(_57.FEMeshingOptions):
    '''ElectricMachineMeshingOptions

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_MESHING_OPTIONS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineMeshingOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def utilise_periodicity_when_meshing_geometry(self) -> 'bool':
        '''bool: 'UtilisePeriodicityWhenMeshingGeometry' is the original name of this property.'''

        return self.wrapped.UtilisePeriodicityWhenMeshingGeometry

    @utilise_periodicity_when_meshing_geometry.setter
    def utilise_periodicity_when_meshing_geometry(self, value: 'bool'):
        self.wrapped.UtilisePeriodicityWhenMeshingGeometry = bool(value) if value else False

    @property
    def magnet_element_size(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'MagnetElementSize' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.MagnetElementSize) if self.wrapped.MagnetElementSize is not None else None

    @magnet_element_size.setter
    def magnet_element_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MagnetElementSize = value

    @property
    def use_p_elements(self) -> 'bool':
        '''bool: 'UsePElements' is the original name of this property.'''

        return self.wrapped.UsePElements

    @use_p_elements.setter
    def use_p_elements(self, value: 'bool'):
        self.wrapped.UsePElements = bool(value) if value else False

    @property
    def p_element_order(self) -> 'int':
        '''int: 'PElementOrder' is the original name of this property.'''

        return self.wrapped.PElementOrder

    @p_element_order.setter
    def p_element_order(self, value: 'int'):
        self.wrapped.PElementOrder = int(value) if value else 0

    @property
    def air_gap_element_size(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'AirGapElementSize' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.AirGapElementSize) if self.wrapped.AirGapElementSize is not None else None

    @air_gap_element_size.setter
    def air_gap_element_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AirGapElementSize = value

    @property
    def minimum_number_of_element_layers_in_air_gap(self) -> 'int':
        '''int: 'MinimumNumberOfElementLayersInAirGap' is the original name of this property.'''

        return self.wrapped.MinimumNumberOfElementLayersInAirGap

    @minimum_number_of_element_layers_in_air_gap.setter
    def minimum_number_of_element_layers_in_air_gap(self, value: 'int'):
        self.wrapped.MinimumNumberOfElementLayersInAirGap = int(value) if value else 0

    @property
    def slot_element_size(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'SlotElementSize' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.SlotElementSize) if self.wrapped.SlotElementSize is not None else None

    @slot_element_size.setter
    def slot_element_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SlotElementSize = value
