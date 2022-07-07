'''_1821.py

LoadedBearingDutyCycle
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_designs import (
    _1998, _1999, _2000, _2001,
    _2002
)
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_designs.rolling import (
    _2003, _2004, _2005, _2006,
    _2007, _2008, _2010, _2015,
    _2016, _2017, _2020, _2025,
    _2026, _2027, _2028, _2031,
    _2032, _2035, _2036, _2037,
    _2038, _2039, _2040
)
from mastapy.bearings.bearing_designs.fluid_film import (
    _2053, _2055, _2057, _2059,
    _2060, _2061
)
from mastapy.bearings.bearing_designs.concept import _2063, _2064, _2065
from mastapy.utility.property import _1725
from mastapy.bearings import _1753
from mastapy.bearings.bearing_results import _1822
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBearingDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBearingDutyCycle',)


class LoadedBearingDutyCycle(_0.APIBase):
    '''LoadedBearingDutyCycle

    This is a mastapy class.
    '''

    TYPE = _LOADED_BEARING_DUTY_CYCLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_name(self) -> 'str':
        '''str: 'DutyCycleName' is the original name of this property.'''

        return self.wrapped.DutyCycleName

    @duty_cycle_name.setter
    def duty_cycle_name(self, value: 'str'):
        self.wrapped.DutyCycleName = str(value) if value else ''

    @property
    def duration(self) -> 'float':
        '''float: 'Duration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Duration

    @property
    def bearing_design(self) -> '_1998.BearingDesign':
        '''BearingDesign: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1998.BearingDesign.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BearingDesign. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_detailed_bearing(self) -> '_1999.DetailedBearing':
        '''DetailedBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1999.DetailedBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DetailedBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_dummy_rolling_bearing(self) -> '_2000.DummyRollingBearing':
        '''DummyRollingBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2000.DummyRollingBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DummyRollingBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_linear_bearing(self) -> '_2001.LinearBearing':
        '''LinearBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2001.LinearBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to LinearBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_non_linear_bearing(self) -> '_2002.NonLinearBearing':
        '''NonLinearBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2002.NonLinearBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NonLinearBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_angular_contact_ball_bearing(self) -> '_2003.AngularContactBallBearing':
        '''AngularContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2003.AngularContactBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AngularContactBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_angular_contact_thrust_ball_bearing(self) -> '_2004.AngularContactThrustBallBearing':
        '''AngularContactThrustBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2004.AngularContactThrustBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AngularContactThrustBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_asymmetric_spherical_roller_bearing(self) -> '_2005.AsymmetricSphericalRollerBearing':
        '''AsymmetricSphericalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2005.AsymmetricSphericalRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AsymmetricSphericalRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_2006.AxialThrustCylindricalRollerBearing':
        '''AxialThrustCylindricalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2006.AxialThrustCylindricalRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_axial_thrust_needle_roller_bearing(self) -> '_2007.AxialThrustNeedleRollerBearing':
        '''AxialThrustNeedleRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2007.AxialThrustNeedleRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AxialThrustNeedleRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_ball_bearing(self) -> '_2008.BallBearing':
        '''BallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2008.BallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_barrel_roller_bearing(self) -> '_2010.BarrelRollerBearing':
        '''BarrelRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2010.BarrelRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BarrelRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_crossed_roller_bearing(self) -> '_2015.CrossedRollerBearing':
        '''CrossedRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2015.CrossedRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to CrossedRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_cylindrical_roller_bearing(self) -> '_2016.CylindricalRollerBearing':
        '''CylindricalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2016.CylindricalRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to CylindricalRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_deep_groove_ball_bearing(self) -> '_2017.DeepGrooveBallBearing':
        '''DeepGrooveBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2017.DeepGrooveBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DeepGrooveBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_four_point_contact_ball_bearing(self) -> '_2020.FourPointContactBallBearing':
        '''FourPointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2020.FourPointContactBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to FourPointContactBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_multi_point_contact_ball_bearing(self) -> '_2025.MultiPointContactBallBearing':
        '''MultiPointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2025.MultiPointContactBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to MultiPointContactBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_needle_roller_bearing(self) -> '_2026.NeedleRollerBearing':
        '''NeedleRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2026.NeedleRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NeedleRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_non_barrel_roller_bearing(self) -> '_2027.NonBarrelRollerBearing':
        '''NonBarrelRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2027.NonBarrelRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NonBarrelRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_roller_bearing(self) -> '_2028.RollerBearing':
        '''RollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2028.RollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to RollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_rolling_bearing(self) -> '_2031.RollingBearing':
        '''RollingBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2031.RollingBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to RollingBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_self_aligning_ball_bearing(self) -> '_2032.SelfAligningBallBearing':
        '''SelfAligningBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2032.SelfAligningBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SelfAligningBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_spherical_roller_bearing(self) -> '_2035.SphericalRollerBearing':
        '''SphericalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2035.SphericalRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SphericalRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_spherical_roller_thrust_bearing(self) -> '_2036.SphericalRollerThrustBearing':
        '''SphericalRollerThrustBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2036.SphericalRollerThrustBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SphericalRollerThrustBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_taper_roller_bearing(self) -> '_2037.TaperRollerBearing':
        '''TaperRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2037.TaperRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TaperRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_three_point_contact_ball_bearing(self) -> '_2038.ThreePointContactBallBearing':
        '''ThreePointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2038.ThreePointContactBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ThreePointContactBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_thrust_ball_bearing(self) -> '_2039.ThrustBallBearing':
        '''ThrustBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2039.ThrustBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ThrustBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_toroidal_roller_bearing(self) -> '_2040.ToroidalRollerBearing':
        '''ToroidalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2040.ToroidalRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ToroidalRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_pad_fluid_film_bearing(self) -> '_2053.PadFluidFilmBearing':
        '''PadFluidFilmBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2053.PadFluidFilmBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PadFluidFilmBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_plain_grease_filled_journal_bearing(self) -> '_2055.PlainGreaseFilledJournalBearing':
        '''PlainGreaseFilledJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2055.PlainGreaseFilledJournalBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainGreaseFilledJournalBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_plain_journal_bearing(self) -> '_2057.PlainJournalBearing':
        '''PlainJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2057.PlainJournalBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainJournalBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_plain_oil_fed_journal_bearing(self) -> '_2059.PlainOilFedJournalBearing':
        '''PlainOilFedJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2059.PlainOilFedJournalBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainOilFedJournalBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_tilting_pad_journal_bearing(self) -> '_2060.TiltingPadJournalBearing':
        '''TiltingPadJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2060.TiltingPadJournalBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TiltingPadJournalBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_tilting_pad_thrust_bearing(self) -> '_2061.TiltingPadThrustBearing':
        '''TiltingPadThrustBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2061.TiltingPadThrustBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TiltingPadThrustBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_concept_axial_clearance_bearing(self) -> '_2063.ConceptAxialClearanceBearing':
        '''ConceptAxialClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2063.ConceptAxialClearanceBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptAxialClearanceBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_concept_clearance_bearing(self) -> '_2064.ConceptClearanceBearing':
        '''ConceptClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2064.ConceptClearanceBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptClearanceBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def bearing_design_of_type_concept_radial_clearance_bearing(self) -> '_2065.ConceptRadialClearanceBearing':
        '''ConceptRadialClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2065.ConceptRadialClearanceBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptRadialClearanceBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BearingDesign.__class__)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign is not None else None

    @property
    def radial_load_summary(self) -> '_1725.DutyCyclePropertySummaryForce[_1753.BearingLoadCaseResultsLightweight]':
        '''DutyCyclePropertySummaryForce[BearingLoadCaseResultsLightweight]: 'RadialLoadSummary' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1725.DutyCyclePropertySummaryForce)[_1753.BearingLoadCaseResultsLightweight](self.wrapped.RadialLoadSummary) if self.wrapped.RadialLoadSummary is not None else None

    @property
    def z_thrust_reaction_summary(self) -> '_1725.DutyCyclePropertySummaryForce[_1753.BearingLoadCaseResultsLightweight]':
        '''DutyCyclePropertySummaryForce[BearingLoadCaseResultsLightweight]: 'ZThrustReactionSummary' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1725.DutyCyclePropertySummaryForce)[_1753.BearingLoadCaseResultsLightweight](self.wrapped.ZThrustReactionSummary) if self.wrapped.ZThrustReactionSummary is not None else None

    @property
    def bearing_load_case_results(self) -> 'List[_1822.LoadedBearingResults]':
        '''List[LoadedBearingResults]: 'BearingLoadCaseResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BearingLoadCaseResults, constructor.new(_1822.LoadedBearingResults))
        return value

    @property
    def report_names(self) -> 'List[str]':
        '''List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ReportNames, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        ''' 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        ''' 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        '''

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        ''' 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        ''' 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        ''' 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        '''

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        ''' 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        '''

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result
