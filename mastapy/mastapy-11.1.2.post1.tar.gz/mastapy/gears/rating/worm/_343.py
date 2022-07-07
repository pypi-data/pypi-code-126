'''_343.py

WormGearDutyCycleRating
'''


from typing import List

from mastapy.gears.rating import _330, _329
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical import _424, _425
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.worm import _346, _345
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Worm', 'WormGearDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearDutyCycleRating',)


class WormGearDutyCycleRating(_329.GearDutyCycleRating):
    '''WormGearDutyCycleRating

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_DUTY_CYCLE_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_rating(self) -> '_330.GearFlankRating':
        '''GearFlankRating: 'LeftFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _330.GearFlankRating.TYPE not in self.wrapped.LeftFlankRating.__class__.__mro__:
            raise CastException('Failed to cast left_flank_rating to GearFlankRating. Expected: {}.'.format(self.wrapped.LeftFlankRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LeftFlankRating.__class__)(self.wrapped.LeftFlankRating) if self.wrapped.LeftFlankRating is not None else None

    @property
    def right_flank_rating(self) -> '_330.GearFlankRating':
        '''GearFlankRating: 'RightFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _330.GearFlankRating.TYPE not in self.wrapped.RightFlankRating.__class__.__mro__:
            raise CastException('Failed to cast right_flank_rating to GearFlankRating. Expected: {}.'.format(self.wrapped.RightFlankRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.RightFlankRating.__class__)(self.wrapped.RightFlankRating) if self.wrapped.RightFlankRating is not None else None

    @property
    def gear_set_design_duty_cycle(self) -> '_346.WormGearSetDutyCycleRating':
        '''WormGearSetDutyCycleRating: 'GearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_346.WormGearSetDutyCycleRating)(self.wrapped.GearSetDesignDutyCycle) if self.wrapped.GearSetDesignDutyCycle is not None else None

    @property
    def worm_gear_set_design_duty_cycle(self) -> '_346.WormGearSetDutyCycleRating':
        '''WormGearSetDutyCycleRating: 'WormGearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_346.WormGearSetDutyCycleRating)(self.wrapped.WormGearSetDesignDutyCycle) if self.wrapped.WormGearSetDesignDutyCycle is not None else None

    @property
    def gear_ratings(self) -> 'List[_345.WormGearRating]':
        '''List[WormGearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearRatings, constructor.new(_345.WormGearRating))
        return value

    @property
    def worm_gear_ratings(self) -> 'List[_345.WormGearRating]':
        '''List[WormGearRating]: 'WormGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearRatings, constructor.new(_345.WormGearRating))
        return value
