'''_1501.py

MeasurementSettings
'''


from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.utility.units_and_measurements import _1500
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility.units_and_measurements.measurements import (
    _1507, _1508, _1509, _1510,
    _1511, _1512, _1513, _1514,
    _1515, _1516, _1517, _1518,
    _1519, _1520, _1521, _1522,
    _1523, _1524, _1525, _1526,
    _1527, _1528, _1529, _1530,
    _1531, _1532, _1533, _1534,
    _1535, _1536, _1537, _1538,
    _1539, _1540, _1541, _1542,
    _1543, _1544, _1545, _1546,
    _1547, _1548, _1549, _1550,
    _1551, _1552, _1553, _1554,
    _1555, _1556, _1557, _1558,
    _1559, _1560, _1561, _1562,
    _1563, _1564, _1565, _1566,
    _1567, _1568, _1569, _1570,
    _1571, _1572, _1573, _1574,
    _1575, _1576, _1577, _1578,
    _1579, _1580, _1581, _1582,
    _1583, _1584, _1585, _1586,
    _1587, _1588, _1589, _1590,
    _1591, _1592, _1593, _1594,
    _1595, _1596, _1597, _1598,
    _1599, _1600, _1601, _1602,
    _1603, _1604, _1605, _1606,
    _1607, _1608, _1609, _1610,
    _1611, _1612, _1613, _1614,
    _1615, _1616, _1617, _1618,
    _1619, _1620, _1621, _1622,
    _1623, _1624, _1625, _1626,
    _1627, _1628, _1629, _1630,
    _1631
)
from mastapy._internal.cast_exception import CastException
from mastapy.utility import _1489
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_SETTINGS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'MeasurementSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementSettings',)


class MeasurementSettings(_1489.PerMachineSettings):
    '''MeasurementSettings

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_SETTINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_measurement(self) -> 'list_with_selected_item.ListWithSelectedItem_MeasurementBase':
        '''list_with_selected_item.ListWithSelectedItem_MeasurementBase: 'SelectedMeasurement' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_MeasurementBase)(self.wrapped.SelectedMeasurement) if self.wrapped.SelectedMeasurement is not None else None

    @selected_measurement.setter
    def selected_measurement(self, value: 'list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectedMeasurement = value

    @property
    def sample_input(self) -> 'str':
        '''str: 'SampleInput' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SampleInput

    @property
    def sample_output(self) -> 'str':
        '''str: 'SampleOutput' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SampleOutput

    @property
    def number_decimal_separator(self) -> 'str':
        '''str: 'NumberDecimalSeparator' is the original name of this property.'''

        return self.wrapped.NumberDecimalSeparator

    @number_decimal_separator.setter
    def number_decimal_separator(self, value: 'str'):
        self.wrapped.NumberDecimalSeparator = str(value) if value else ''

    @property
    def number_group_separator(self) -> 'str':
        '''str: 'NumberGroupSeparator' is the original name of this property.'''

        return self.wrapped.NumberGroupSeparator

    @number_group_separator.setter
    def number_group_separator(self, value: 'str'):
        self.wrapped.NumberGroupSeparator = str(value) if value else ''

    @property
    def small_number_cutoff(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'SmallNumberCutoff' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.SmallNumberCutoff) if self.wrapped.SmallNumberCutoff is not None else None

    @small_number_cutoff.setter
    def small_number_cutoff(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SmallNumberCutoff = value

    @property
    def large_number_cutoff(self) -> 'float':
        '''float: 'LargeNumberCutoff' is the original name of this property.'''

        return self.wrapped.LargeNumberCutoff

    @large_number_cutoff.setter
    def large_number_cutoff(self, value: 'float'):
        self.wrapped.LargeNumberCutoff = float(value) if value else 0.0

    @property
    def show_trailing_zeros(self) -> 'bool':
        '''bool: 'ShowTrailingZeros' is the original name of this property.'''

        return self.wrapped.ShowTrailingZeros

    @show_trailing_zeros.setter
    def show_trailing_zeros(self, value: 'bool'):
        self.wrapped.ShowTrailingZeros = bool(value) if value else False

    @property
    def current_selected_measurement(self) -> '_1500.MeasurementBase':
        '''MeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1500.MeasurementBase.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MeasurementBase. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_acceleration(self) -> '_1507.Acceleration':
        '''Acceleration: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1507.Acceleration.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Acceleration. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_angle(self) -> '_1508.Angle':
        '''Angle: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1508.Angle.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Angle. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_angle_per_unit_temperature(self) -> '_1509.AnglePerUnitTemperature':
        '''AnglePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1509.AnglePerUnitTemperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AnglePerUnitTemperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_angle_small(self) -> '_1510.AngleSmall':
        '''AngleSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1510.AngleSmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngleSmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_angle_very_small(self) -> '_1511.AngleVerySmall':
        '''AngleVerySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1511.AngleVerySmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngleVerySmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_angular_acceleration(self) -> '_1512.AngularAcceleration':
        '''AngularAcceleration: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1512.AngularAcceleration.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularAcceleration. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_angular_compliance(self) -> '_1513.AngularCompliance':
        '''AngularCompliance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1513.AngularCompliance.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularCompliance. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_angular_jerk(self) -> '_1514.AngularJerk':
        '''AngularJerk: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1514.AngularJerk.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularJerk. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_angular_stiffness(self) -> '_1515.AngularStiffness':
        '''AngularStiffness: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1515.AngularStiffness.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularStiffness. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_angular_velocity(self) -> '_1516.AngularVelocity':
        '''AngularVelocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1516.AngularVelocity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularVelocity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_area(self) -> '_1517.Area':
        '''Area: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1517.Area.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Area. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_area_small(self) -> '_1518.AreaSmall':
        '''AreaSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1518.AreaSmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AreaSmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_current_density(self) -> '_1519.CurrentDensity':
        '''CurrentDensity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1519.CurrentDensity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to CurrentDensity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_current_per_length(self) -> '_1520.CurrentPerLength':
        '''CurrentPerLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1520.CurrentPerLength.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to CurrentPerLength. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_cycles(self) -> '_1521.Cycles':
        '''Cycles: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1521.Cycles.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Cycles. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_damage(self) -> '_1522.Damage':
        '''Damage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1522.Damage.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Damage. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_damage_rate(self) -> '_1523.DamageRate':
        '''DamageRate: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1523.DamageRate.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to DamageRate. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_data_size(self) -> '_1524.DataSize':
        '''DataSize: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1524.DataSize.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to DataSize. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_decibel(self) -> '_1525.Decibel':
        '''Decibel: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1525.Decibel.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Decibel. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_density(self) -> '_1526.Density':
        '''Density: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1526.Density.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Density. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_electrical_resistance(self) -> '_1527.ElectricalResistance':
        '''ElectricalResistance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1527.ElectricalResistance.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricalResistance. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_electrical_resistivity(self) -> '_1528.ElectricalResistivity':
        '''ElectricalResistivity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1528.ElectricalResistivity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricalResistivity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_electric_current(self) -> '_1529.ElectricCurrent':
        '''ElectricCurrent: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1529.ElectricCurrent.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricCurrent. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_energy(self) -> '_1530.Energy':
        '''Energy: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1530.Energy.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Energy. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_energy_per_unit_area(self) -> '_1531.EnergyPerUnitArea':
        '''EnergyPerUnitArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1531.EnergyPerUnitArea.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergyPerUnitArea. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_energy_per_unit_area_small(self) -> '_1532.EnergyPerUnitAreaSmall':
        '''EnergyPerUnitAreaSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1532.EnergyPerUnitAreaSmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergyPerUnitAreaSmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_energy_small(self) -> '_1533.EnergySmall':
        '''EnergySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1533.EnergySmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergySmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_enum(self) -> '_1534.Enum':
        '''Enum: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1534.Enum.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Enum. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_flow_rate(self) -> '_1535.FlowRate':
        '''FlowRate: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1535.FlowRate.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FlowRate. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_force(self) -> '_1536.Force':
        '''Force: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1536.Force.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Force. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_length(self) -> '_1537.ForcePerUnitLength':
        '''ForcePerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1537.ForcePerUnitLength.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitLength. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_pressure(self) -> '_1538.ForcePerUnitPressure':
        '''ForcePerUnitPressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1538.ForcePerUnitPressure.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitPressure. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_temperature(self) -> '_1539.ForcePerUnitTemperature':
        '''ForcePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1539.ForcePerUnitTemperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitTemperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_fraction_measurement_base(self) -> '_1540.FractionMeasurementBase':
        '''FractionMeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1540.FractionMeasurementBase.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FractionMeasurementBase. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_fraction_per_temperature(self) -> '_1541.FractionPerTemperature':
        '''FractionPerTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1541.FractionPerTemperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FractionPerTemperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_frequency(self) -> '_1542.Frequency':
        '''Frequency: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1542.Frequency.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Frequency. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_fuel_consumption_engine(self) -> '_1543.FuelConsumptionEngine':
        '''FuelConsumptionEngine: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1543.FuelConsumptionEngine.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FuelConsumptionEngine. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_fuel_efficiency_vehicle(self) -> '_1544.FuelEfficiencyVehicle':
        '''FuelEfficiencyVehicle: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1544.FuelEfficiencyVehicle.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FuelEfficiencyVehicle. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_gradient(self) -> '_1545.Gradient':
        '''Gradient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1545.Gradient.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Gradient. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_heat_conductivity(self) -> '_1546.HeatConductivity':
        '''HeatConductivity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1546.HeatConductivity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatConductivity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer(self) -> '_1547.HeatTransfer':
        '''HeatTransfer: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1547.HeatTransfer.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransfer. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1548.HeatTransferCoefficientForPlasticGearTooth':
        '''HeatTransferCoefficientForPlasticGearTooth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1548.HeatTransferCoefficientForPlasticGearTooth.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer_resistance(self) -> '_1549.HeatTransferResistance':
        '''HeatTransferResistance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1549.HeatTransferResistance.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransferResistance. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_impulse(self) -> '_1550.Impulse':
        '''Impulse: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1550.Impulse.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Impulse. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_index(self) -> '_1551.Index':
        '''Index: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1551.Index.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Index. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_inductance(self) -> '_1552.Inductance':
        '''Inductance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1552.Inductance.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Inductance. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_integer(self) -> '_1553.Integer':
        '''Integer: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1553.Integer.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Integer. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_inverse_short_length(self) -> '_1554.InverseShortLength':
        '''InverseShortLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1554.InverseShortLength.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to InverseShortLength. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_inverse_short_time(self) -> '_1555.InverseShortTime':
        '''InverseShortTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1555.InverseShortTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to InverseShortTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_jerk(self) -> '_1556.Jerk':
        '''Jerk: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1556.Jerk.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Jerk. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_kinematic_viscosity(self) -> '_1557.KinematicViscosity':
        '''KinematicViscosity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1557.KinematicViscosity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to KinematicViscosity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_length_long(self) -> '_1558.LengthLong':
        '''LengthLong: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1558.LengthLong.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthLong. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_length_medium(self) -> '_1559.LengthMedium':
        '''LengthMedium: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1559.LengthMedium.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthMedium. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_length_per_unit_temperature(self) -> '_1560.LengthPerUnitTemperature':
        '''LengthPerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1560.LengthPerUnitTemperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthPerUnitTemperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_length_short(self) -> '_1561.LengthShort':
        '''LengthShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1561.LengthShort.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthShort. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_length_to_the_fourth(self) -> '_1562.LengthToTheFourth':
        '''LengthToTheFourth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1562.LengthToTheFourth.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthToTheFourth. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_length_very_long(self) -> '_1563.LengthVeryLong':
        '''LengthVeryLong: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1563.LengthVeryLong.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryLong. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_length_very_short(self) -> '_1564.LengthVeryShort':
        '''LengthVeryShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1564.LengthVeryShort.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryShort. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_length_very_short_per_length_short(self) -> '_1565.LengthVeryShortPerLengthShort':
        '''LengthVeryShortPerLengthShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1565.LengthVeryShortPerLengthShort.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryShortPerLengthShort. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_linear_angular_damping(self) -> '_1566.LinearAngularDamping':
        '''LinearAngularDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1566.LinearAngularDamping.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearAngularDamping. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_linear_angular_stiffness_cross_term(self) -> '_1567.LinearAngularStiffnessCrossTerm':
        '''LinearAngularStiffnessCrossTerm: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1567.LinearAngularStiffnessCrossTerm.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_linear_damping(self) -> '_1568.LinearDamping':
        '''LinearDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1568.LinearDamping.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearDamping. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_linear_flexibility(self) -> '_1569.LinearFlexibility':
        '''LinearFlexibility: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1569.LinearFlexibility.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearFlexibility. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_linear_stiffness(self) -> '_1570.LinearStiffness':
        '''LinearStiffness: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1570.LinearStiffness.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearStiffness. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_field_strength(self) -> '_1571.MagneticFieldStrength':
        '''MagneticFieldStrength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1571.MagneticFieldStrength.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFieldStrength. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_flux(self) -> '_1572.MagneticFlux':
        '''MagneticFlux: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1572.MagneticFlux.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFlux. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_flux_density(self) -> '_1573.MagneticFluxDensity':
        '''MagneticFluxDensity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1573.MagneticFluxDensity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFluxDensity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_vector_potential(self) -> '_1574.MagneticVectorPotential':
        '''MagneticVectorPotential: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1574.MagneticVectorPotential.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticVectorPotential. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_mass(self) -> '_1575.Mass':
        '''Mass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1575.Mass.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Mass. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_mass_per_unit_length(self) -> '_1576.MassPerUnitLength':
        '''MassPerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1576.MassPerUnitLength.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MassPerUnitLength. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_mass_per_unit_time(self) -> '_1577.MassPerUnitTime':
        '''MassPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1577.MassPerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MassPerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_moment_of_inertia(self) -> '_1578.MomentOfInertia':
        '''MomentOfInertia: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1578.MomentOfInertia.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentOfInertia. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_moment_of_inertia_per_unit_length(self) -> '_1579.MomentOfInertiaPerUnitLength':
        '''MomentOfInertiaPerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1579.MomentOfInertiaPerUnitLength.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentOfInertiaPerUnitLength. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_moment_per_unit_pressure(self) -> '_1580.MomentPerUnitPressure':
        '''MomentPerUnitPressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1580.MomentPerUnitPressure.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentPerUnitPressure. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_number(self) -> '_1581.Number':
        '''Number: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1581.Number.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Number. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_percentage(self) -> '_1582.Percentage':
        '''Percentage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1582.Percentage.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Percentage. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_power(self) -> '_1583.Power':
        '''Power: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1583.Power.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Power. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_power_per_small_area(self) -> '_1584.PowerPerSmallArea':
        '''PowerPerSmallArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1584.PowerPerSmallArea.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerPerSmallArea. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_power_per_unit_time(self) -> '_1585.PowerPerUnitTime':
        '''PowerPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1585.PowerPerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerPerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_power_small(self) -> '_1586.PowerSmall':
        '''PowerSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1586.PowerSmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_area(self) -> '_1587.PowerSmallPerArea':
        '''PowerSmallPerArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1587.PowerSmallPerArea.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerArea. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_mass(self) -> '_1588.PowerSmallPerMass':
        '''PowerSmallPerMass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1588.PowerSmallPerMass.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerMass. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1589.PowerSmallPerUnitAreaPerUnitTime':
        '''PowerSmallPerUnitAreaPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1589.PowerSmallPerUnitAreaPerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_unit_time(self) -> '_1590.PowerSmallPerUnitTime':
        '''PowerSmallPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1590.PowerSmallPerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_volume(self) -> '_1591.PowerSmallPerVolume':
        '''PowerSmallPerVolume: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1591.PowerSmallPerVolume.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerVolume. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_pressure(self) -> '_1592.Pressure':
        '''Pressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1592.Pressure.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Pressure. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_pressure_per_unit_time(self) -> '_1593.PressurePerUnitTime':
        '''PressurePerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1593.PressurePerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressurePerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_pressure_velocity_product(self) -> '_1594.PressureVelocityProduct':
        '''PressureVelocityProduct: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1594.PressureVelocityProduct.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressureVelocityProduct. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_pressure_viscosity_coefficient(self) -> '_1595.PressureViscosityCoefficient':
        '''PressureViscosityCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1595.PressureViscosityCoefficient.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressureViscosityCoefficient. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_price(self) -> '_1596.Price':
        '''Price: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1596.Price.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Price. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_price_per_unit_mass(self) -> '_1597.PricePerUnitMass':
        '''PricePerUnitMass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1597.PricePerUnitMass.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PricePerUnitMass. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_quadratic_angular_damping(self) -> '_1598.QuadraticAngularDamping':
        '''QuadraticAngularDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1598.QuadraticAngularDamping.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to QuadraticAngularDamping. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_quadratic_drag(self) -> '_1599.QuadraticDrag':
        '''QuadraticDrag: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1599.QuadraticDrag.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to QuadraticDrag. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_rescaled_measurement(self) -> '_1600.RescaledMeasurement':
        '''RescaledMeasurement: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1600.RescaledMeasurement.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to RescaledMeasurement. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_rotatum(self) -> '_1601.Rotatum':
        '''Rotatum: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1601.Rotatum.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Rotatum. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_safety_factor(self) -> '_1602.SafetyFactor':
        '''SafetyFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1602.SafetyFactor.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SafetyFactor. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_specific_acoustic_impedance(self) -> '_1603.SpecificAcousticImpedance':
        '''SpecificAcousticImpedance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1603.SpecificAcousticImpedance.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SpecificAcousticImpedance. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_specific_heat(self) -> '_1604.SpecificHeat':
        '''SpecificHeat: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1604.SpecificHeat.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SpecificHeat. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1605.SquareRootOfUnitForcePerUnitArea':
        '''SquareRootOfUnitForcePerUnitArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1605.SquareRootOfUnitForcePerUnitArea.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_stiffness_per_unit_face_width(self) -> '_1606.StiffnessPerUnitFaceWidth':
        '''StiffnessPerUnitFaceWidth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1606.StiffnessPerUnitFaceWidth.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to StiffnessPerUnitFaceWidth. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_stress(self) -> '_1607.Stress':
        '''Stress: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1607.Stress.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Stress. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_temperature(self) -> '_1608.Temperature':
        '''Temperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1608.Temperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Temperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_temperature_difference(self) -> '_1609.TemperatureDifference':
        '''TemperatureDifference: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1609.TemperatureDifference.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TemperatureDifference. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_temperature_per_unit_time(self) -> '_1610.TemperaturePerUnitTime':
        '''TemperaturePerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1610.TemperaturePerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TemperaturePerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_text(self) -> '_1611.Text':
        '''Text: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1611.Text.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Text. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_thermal_contact_coefficient(self) -> '_1612.ThermalContactCoefficient':
        '''ThermalContactCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1612.ThermalContactCoefficient.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermalContactCoefficient. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_thermal_expansion_coefficient(self) -> '_1613.ThermalExpansionCoefficient':
        '''ThermalExpansionCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1613.ThermalExpansionCoefficient.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermalExpansionCoefficient. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_thermo_elastic_factor(self) -> '_1614.ThermoElasticFactor':
        '''ThermoElasticFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1614.ThermoElasticFactor.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermoElasticFactor. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_time(self) -> '_1615.Time':
        '''Time: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1615.Time.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Time. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_time_short(self) -> '_1616.TimeShort':
        '''TimeShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1616.TimeShort.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TimeShort. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_time_very_short(self) -> '_1617.TimeVeryShort':
        '''TimeVeryShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1617.TimeVeryShort.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TimeVeryShort. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_torque(self) -> '_1618.Torque':
        '''Torque: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1618.Torque.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Torque. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_torque_converter_inverse_k(self) -> '_1619.TorqueConverterInverseK':
        '''TorqueConverterInverseK: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1619.TorqueConverterInverseK.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorqueConverterInverseK. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_torque_converter_k(self) -> '_1620.TorqueConverterK':
        '''TorqueConverterK: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1620.TorqueConverterK.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorqueConverterK. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_current(self) -> '_1621.TorquePerCurrent':
        '''TorquePerCurrent: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1621.TorquePerCurrent.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerCurrent. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_square_root_of_power(self) -> '_1622.TorquePerSquareRootOfPower':
        '''TorquePerSquareRootOfPower: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1622.TorquePerSquareRootOfPower.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerSquareRootOfPower. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_unit_temperature(self) -> '_1623.TorquePerUnitTemperature':
        '''TorquePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1623.TorquePerUnitTemperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerUnitTemperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_velocity(self) -> '_1624.Velocity':
        '''Velocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1624.Velocity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Velocity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_velocity_small(self) -> '_1625.VelocitySmall':
        '''VelocitySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1625.VelocitySmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to VelocitySmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_viscosity(self) -> '_1626.Viscosity':
        '''Viscosity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1626.Viscosity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Viscosity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_voltage(self) -> '_1627.Voltage':
        '''Voltage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1627.Voltage.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Voltage. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_voltage_per_angular_velocity(self) -> '_1628.VoltagePerAngularVelocity':
        '''VoltagePerAngularVelocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1628.VoltagePerAngularVelocity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to VoltagePerAngularVelocity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_volume(self) -> '_1629.Volume':
        '''Volume: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1629.Volume.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Volume. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_wear_coefficient(self) -> '_1630.WearCoefficient':
        '''WearCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1630.WearCoefficient.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to WearCoefficient. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    @property
    def current_selected_measurement_of_type_yank(self) -> '_1631.Yank':
        '''Yank: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1631.Yank.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Yank. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement is not None else None

    def default_to_metric(self):
        ''' 'DefaultToMetric' is the original name of this method.'''

        self.wrapped.DefaultToMetric()

    def default_to_imperial(self):
        ''' 'DefaultToImperial' is the original name of this method.'''

        self.wrapped.DefaultToImperial()
