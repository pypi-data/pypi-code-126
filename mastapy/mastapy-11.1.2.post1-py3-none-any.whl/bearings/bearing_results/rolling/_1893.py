'''_1893.py

LoadedNonBarrelRollerBearingRow
'''


from mastapy.bearings.bearing_results.rolling import (
    _1892, _1862, _1865, _1877,
    _1889, _1917, _1898
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedNonBarrelRollerBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNonBarrelRollerBearingRow',)


class LoadedNonBarrelRollerBearingRow(_1898.LoadedRollerBearingRow):
    '''LoadedNonBarrelRollerBearingRow

    This is a mastapy class.
    '''

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_ROW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedNonBarrelRollerBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_1892.LoadedNonBarrelRollerBearingResults':
        '''LoadedNonBarrelRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1892.LoadedNonBarrelRollerBearingResults.TYPE not in self.wrapped.LoadedBearing.__class__.__mro__:
            raise CastException('Failed to cast loaded_bearing to LoadedNonBarrelRollerBearingResults. Expected: {}.'.format(self.wrapped.LoadedBearing.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadedBearing.__class__)(self.wrapped.LoadedBearing) if self.wrapped.LoadedBearing is not None else None

    @property
    def loaded_bearing_of_type_loaded_axial_thrust_cylindrical_roller_bearing_results(self) -> '_1862.LoadedAxialThrustCylindricalRollerBearingResults':
        '''LoadedAxialThrustCylindricalRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1862.LoadedAxialThrustCylindricalRollerBearingResults.TYPE not in self.wrapped.LoadedBearing.__class__.__mro__:
            raise CastException('Failed to cast loaded_bearing to LoadedAxialThrustCylindricalRollerBearingResults. Expected: {}.'.format(self.wrapped.LoadedBearing.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadedBearing.__class__)(self.wrapped.LoadedBearing) if self.wrapped.LoadedBearing is not None else None

    @property
    def loaded_bearing_of_type_loaded_axial_thrust_needle_roller_bearing_results(self) -> '_1865.LoadedAxialThrustNeedleRollerBearingResults':
        '''LoadedAxialThrustNeedleRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1865.LoadedAxialThrustNeedleRollerBearingResults.TYPE not in self.wrapped.LoadedBearing.__class__.__mro__:
            raise CastException('Failed to cast loaded_bearing to LoadedAxialThrustNeedleRollerBearingResults. Expected: {}.'.format(self.wrapped.LoadedBearing.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadedBearing.__class__)(self.wrapped.LoadedBearing) if self.wrapped.LoadedBearing is not None else None

    @property
    def loaded_bearing_of_type_loaded_cylindrical_roller_bearing_results(self) -> '_1877.LoadedCylindricalRollerBearingResults':
        '''LoadedCylindricalRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1877.LoadedCylindricalRollerBearingResults.TYPE not in self.wrapped.LoadedBearing.__class__.__mro__:
            raise CastException('Failed to cast loaded_bearing to LoadedCylindricalRollerBearingResults. Expected: {}.'.format(self.wrapped.LoadedBearing.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadedBearing.__class__)(self.wrapped.LoadedBearing) if self.wrapped.LoadedBearing is not None else None

    @property
    def loaded_bearing_of_type_loaded_needle_roller_bearing_results(self) -> '_1889.LoadedNeedleRollerBearingResults':
        '''LoadedNeedleRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1889.LoadedNeedleRollerBearingResults.TYPE not in self.wrapped.LoadedBearing.__class__.__mro__:
            raise CastException('Failed to cast loaded_bearing to LoadedNeedleRollerBearingResults. Expected: {}.'.format(self.wrapped.LoadedBearing.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadedBearing.__class__)(self.wrapped.LoadedBearing) if self.wrapped.LoadedBearing is not None else None

    @property
    def loaded_bearing_of_type_loaded_taper_roller_bearing_results(self) -> '_1917.LoadedTaperRollerBearingResults':
        '''LoadedTaperRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1917.LoadedTaperRollerBearingResults.TYPE not in self.wrapped.LoadedBearing.__class__.__mro__:
            raise CastException('Failed to cast loaded_bearing to LoadedTaperRollerBearingResults. Expected: {}.'.format(self.wrapped.LoadedBearing.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LoadedBearing.__class__)(self.wrapped.LoadedBearing) if self.wrapped.LoadedBearing is not None else None
