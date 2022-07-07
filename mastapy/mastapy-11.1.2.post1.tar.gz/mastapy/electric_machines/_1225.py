'''_1225.py

InteriorPermanentMagnetAndSynchronousReluctanceRotor
'''


from typing import List

from mastapy.electric_machines import (
    _1247, _1223, _1259, _1258,
    _1201, _1240, _1244
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.python_net import python_net_import

_INTERIOR_PERMANENT_MAGNET_AND_SYNCHRONOUS_RELUCTANCE_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'InteriorPermanentMagnetAndSynchronousReluctanceRotor')


__docformat__ = 'restructuredtext en'
__all__ = ('InteriorPermanentMagnetAndSynchronousReluctanceRotor',)


class InteriorPermanentMagnetAndSynchronousReluctanceRotor(_1244.PermanentMagnetRotor):
    '''InteriorPermanentMagnetAndSynchronousReluctanceRotor

    This is a mastapy class.
    '''

    TYPE = _INTERIOR_PERMANENT_MAGNET_AND_SYNCHRONOUS_RELUCTANCE_ROTOR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'InteriorPermanentMagnetAndSynchronousReluctanceRotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor_type(self) -> '_1247.RotorType':
        '''RotorType: 'RotorType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.RotorType)
        return constructor.new(_1247.RotorType)(value) if value is not None else None

    @rotor_type.setter
    def rotor_type(self, value: '_1247.RotorType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.RotorType = value

    @property
    def flux_barrier_style(self) -> '_1223.FluxBarrierStyle':
        '''FluxBarrierStyle: 'FluxBarrierStyle' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.FluxBarrierStyle)
        return constructor.new(_1223.FluxBarrierStyle)(value) if value is not None else None

    @flux_barrier_style.setter
    def flux_barrier_style(self, value: '_1223.FluxBarrierStyle'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FluxBarrierStyle = value

    @property
    def number_of_magnet_flux_barrier_layers(self) -> 'int':
        '''int: 'NumberOfMagnetFluxBarrierLayers' is the original name of this property.'''

        return self.wrapped.NumberOfMagnetFluxBarrierLayers

    @number_of_magnet_flux_barrier_layers.setter
    def number_of_magnet_flux_barrier_layers(self, value: 'int'):
        self.wrapped.NumberOfMagnetFluxBarrierLayers = int(value) if value else 0

    @property
    def number_of_cooling_duct_layers(self) -> 'int':
        '''int: 'NumberOfCoolingDuctLayers' is the original name of this property.'''

        return self.wrapped.NumberOfCoolingDuctLayers

    @number_of_cooling_duct_layers.setter
    def number_of_cooling_duct_layers(self, value: 'int'):
        self.wrapped.NumberOfCoolingDuctLayers = int(value) if value else 0

    @property
    def number_of_notch_specifications(self) -> 'int':
        '''int: 'NumberOfNotchSpecifications' is the original name of this property.'''

        return self.wrapped.NumberOfNotchSpecifications

    @number_of_notch_specifications.setter
    def number_of_notch_specifications(self, value: 'int'):
        self.wrapped.NumberOfNotchSpecifications = int(value) if value else 0

    @property
    def v_shape_magnet_layers(self) -> 'List[_1259.VShapedMagnetLayerSpecification]':
        '''List[VShapedMagnetLayerSpecification]: 'VShapeMagnetLayers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.VShapeMagnetLayers, constructor.new(_1259.VShapedMagnetLayerSpecification))
        return value

    @property
    def u_shape_layers(self) -> 'List[_1258.UShapedLayerSpecification]':
        '''List[UShapedLayerSpecification]: 'UShapeLayers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UShapeLayers, constructor.new(_1258.UShapedLayerSpecification))
        return value

    @property
    def cooling_duct_layers(self) -> 'List[_1201.CoolingDuctLayerSpecification]':
        '''List[CoolingDuctLayerSpecification]: 'CoolingDuctLayers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CoolingDuctLayers, constructor.new(_1201.CoolingDuctLayerSpecification))
        return value

    @property
    def notch_specifications(self) -> 'List[_1240.NotchSpecification]':
        '''List[NotchSpecification]: 'NotchSpecifications' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.NotchSpecifications, constructor.new(_1240.NotchSpecification))
        return value
