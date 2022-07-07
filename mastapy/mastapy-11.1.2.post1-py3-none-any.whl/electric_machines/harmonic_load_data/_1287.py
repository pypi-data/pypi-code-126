'''_1287.py

SpeedDependentHarmonicLoadData
'''


from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines.harmonic_load_data import _1284
from mastapy._internal.python_net import python_net_import

_SPEED_DEPENDENT_HARMONIC_LOAD_DATA = python_net_import('SMT.MastaAPI.ElectricMachines.HarmonicLoadData', 'SpeedDependentHarmonicLoadData')


__docformat__ = 'restructuredtext en'
__all__ = ('SpeedDependentHarmonicLoadData',)


class SpeedDependentHarmonicLoadData(_1284.HarmonicLoadDataBase):
    '''SpeedDependentHarmonicLoadData

    This is a mastapy class.
    '''

    TYPE = _SPEED_DEPENDENT_HARMONIC_LOAD_DATA

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpeedDependentHarmonicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_all_speeds(self) -> 'bool':
        '''bool: 'ShowAllSpeeds' is the original name of this property.'''

        return self.wrapped.ShowAllSpeeds

    @show_all_speeds.setter
    def show_all_speeds(self, value: 'bool'):
        self.wrapped.ShowAllSpeeds = bool(value) if value else False

    @property
    def selected_speed(self) -> 'list_with_selected_item.ListWithSelectedItem_float':
        '''list_with_selected_item.ListWithSelectedItem_float: 'SelectedSpeed' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_float)(self.wrapped.SelectedSpeed) if self.wrapped.SelectedSpeed is not None else None

    @selected_speed.setter
    def selected_speed(self, value: 'list_with_selected_item.ListWithSelectedItem_float.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_float.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0)
        self.wrapped.SelectedSpeed = value
