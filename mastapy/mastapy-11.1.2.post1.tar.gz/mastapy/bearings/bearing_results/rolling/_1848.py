'''_1848.py

ISO14179SettingsPerBearingType
'''


from mastapy.bearings import _1772
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.bearings.bearing_results.rolling import _1846
from mastapy.utility import _1484

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ISO14179_SETTINGS_PER_BEARING_TYPE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'ISO14179SettingsPerBearingType')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO14179SettingsPerBearingType',)


class ISO14179SettingsPerBearingType(_1484.IndependentReportablePropertiesBase['ISO14179SettingsPerBearingType']):
    '''ISO14179SettingsPerBearingType

    This is a mastapy class.
    '''

    TYPE = _ISO14179_SETTINGS_PER_BEARING_TYPE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ISO14179SettingsPerBearingType.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rolling_bearing_type(self) -> '_1772.RollingBearingType':
        '''RollingBearingType: 'RollingBearingType' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.RollingBearingType)
        return constructor.new(_1772.RollingBearingType)(value) if value is not None else None

    @property
    def iso14179_settings_database(self) -> 'str':
        '''str: 'ISO14179SettingsDatabase' is the original name of this property.'''

        return self.wrapped.ISO14179SettingsDatabase.SelectedItemName

    @iso14179_settings_database.setter
    def iso14179_settings_database(self, value: 'str'):
        self.wrapped.ISO14179SettingsDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def iso14179_settings(self) -> '_1846.ISO14179Settings':
        '''ISO14179Settings: 'ISO14179Settings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1846.ISO14179Settings)(self.wrapped.ISO14179Settings) if self.wrapped.ISO14179Settings is not None else None
