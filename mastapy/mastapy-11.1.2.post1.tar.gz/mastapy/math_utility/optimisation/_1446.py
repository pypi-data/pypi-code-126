'''_1446.py

OptimizationVariable
'''


from typing import List

from mastapy.utility.units_and_measurements import _1500
from mastapy._internal import constructor, conversion
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
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_VARIABLE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'OptimizationVariable')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationVariable',)


class OptimizationVariable(_0.APIBase):
    '''OptimizationVariable

    This is a mastapy class.
    '''

    TYPE = _OPTIMIZATION_VARIABLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OptimizationVariable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measurement(self) -> '_1500.MeasurementBase':
        '''MeasurementBase: 'Measurement' is the original name of this property.'''

        if _1500.MeasurementBase.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MeasurementBase. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement.setter
    def measurement(self, value: '_1500.MeasurementBase'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_acceleration(self) -> '_1507.Acceleration':
        '''Acceleration: 'Measurement' is the original name of this property.'''

        if _1507.Acceleration.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Acceleration. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_acceleration.setter
    def measurement_of_type_acceleration(self, value: '_1507.Acceleration'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle(self) -> '_1508.Angle':
        '''Angle: 'Measurement' is the original name of this property.'''

        if _1508.Angle.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Angle. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angle.setter
    def measurement_of_type_angle(self, value: '_1508.Angle'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle_per_unit_temperature(self) -> '_1509.AnglePerUnitTemperature':
        '''AnglePerUnitTemperature: 'Measurement' is the original name of this property.'''

        if _1509.AnglePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AnglePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angle_per_unit_temperature.setter
    def measurement_of_type_angle_per_unit_temperature(self, value: '_1509.AnglePerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle_small(self) -> '_1510.AngleSmall':
        '''AngleSmall: 'Measurement' is the original name of this property.'''

        if _1510.AngleSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngleSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angle_small.setter
    def measurement_of_type_angle_small(self, value: '_1510.AngleSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle_very_small(self) -> '_1511.AngleVerySmall':
        '''AngleVerySmall: 'Measurement' is the original name of this property.'''

        if _1511.AngleVerySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngleVerySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angle_very_small.setter
    def measurement_of_type_angle_very_small(self, value: '_1511.AngleVerySmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_acceleration(self) -> '_1512.AngularAcceleration':
        '''AngularAcceleration: 'Measurement' is the original name of this property.'''

        if _1512.AngularAcceleration.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularAcceleration. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angular_acceleration.setter
    def measurement_of_type_angular_acceleration(self, value: '_1512.AngularAcceleration'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_compliance(self) -> '_1513.AngularCompliance':
        '''AngularCompliance: 'Measurement' is the original name of this property.'''

        if _1513.AngularCompliance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularCompliance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angular_compliance.setter
    def measurement_of_type_angular_compliance(self, value: '_1513.AngularCompliance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_jerk(self) -> '_1514.AngularJerk':
        '''AngularJerk: 'Measurement' is the original name of this property.'''

        if _1514.AngularJerk.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularJerk. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angular_jerk.setter
    def measurement_of_type_angular_jerk(self, value: '_1514.AngularJerk'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_stiffness(self) -> '_1515.AngularStiffness':
        '''AngularStiffness: 'Measurement' is the original name of this property.'''

        if _1515.AngularStiffness.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularStiffness. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angular_stiffness.setter
    def measurement_of_type_angular_stiffness(self, value: '_1515.AngularStiffness'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_velocity(self) -> '_1516.AngularVelocity':
        '''AngularVelocity: 'Measurement' is the original name of this property.'''

        if _1516.AngularVelocity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularVelocity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angular_velocity.setter
    def measurement_of_type_angular_velocity(self, value: '_1516.AngularVelocity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_area(self) -> '_1517.Area':
        '''Area: 'Measurement' is the original name of this property.'''

        if _1517.Area.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Area. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_area.setter
    def measurement_of_type_area(self, value: '_1517.Area'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_area_small(self) -> '_1518.AreaSmall':
        '''AreaSmall: 'Measurement' is the original name of this property.'''

        if _1518.AreaSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AreaSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_area_small.setter
    def measurement_of_type_area_small(self, value: '_1518.AreaSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_current_density(self) -> '_1519.CurrentDensity':
        '''CurrentDensity: 'Measurement' is the original name of this property.'''

        if _1519.CurrentDensity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to CurrentDensity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_current_density.setter
    def measurement_of_type_current_density(self, value: '_1519.CurrentDensity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_current_per_length(self) -> '_1520.CurrentPerLength':
        '''CurrentPerLength: 'Measurement' is the original name of this property.'''

        if _1520.CurrentPerLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to CurrentPerLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_current_per_length.setter
    def measurement_of_type_current_per_length(self, value: '_1520.CurrentPerLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_cycles(self) -> '_1521.Cycles':
        '''Cycles: 'Measurement' is the original name of this property.'''

        if _1521.Cycles.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Cycles. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_cycles.setter
    def measurement_of_type_cycles(self, value: '_1521.Cycles'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_damage(self) -> '_1522.Damage':
        '''Damage: 'Measurement' is the original name of this property.'''

        if _1522.Damage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Damage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_damage.setter
    def measurement_of_type_damage(self, value: '_1522.Damage'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_damage_rate(self) -> '_1523.DamageRate':
        '''DamageRate: 'Measurement' is the original name of this property.'''

        if _1523.DamageRate.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to DamageRate. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_damage_rate.setter
    def measurement_of_type_damage_rate(self, value: '_1523.DamageRate'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_data_size(self) -> '_1524.DataSize':
        '''DataSize: 'Measurement' is the original name of this property.'''

        if _1524.DataSize.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to DataSize. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_data_size.setter
    def measurement_of_type_data_size(self, value: '_1524.DataSize'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_decibel(self) -> '_1525.Decibel':
        '''Decibel: 'Measurement' is the original name of this property.'''

        if _1525.Decibel.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Decibel. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_decibel.setter
    def measurement_of_type_decibel(self, value: '_1525.Decibel'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_density(self) -> '_1526.Density':
        '''Density: 'Measurement' is the original name of this property.'''

        if _1526.Density.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Density. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_density.setter
    def measurement_of_type_density(self, value: '_1526.Density'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_electrical_resistance(self) -> '_1527.ElectricalResistance':
        '''ElectricalResistance: 'Measurement' is the original name of this property.'''

        if _1527.ElectricalResistance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ElectricalResistance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_electrical_resistance.setter
    def measurement_of_type_electrical_resistance(self, value: '_1527.ElectricalResistance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_electrical_resistivity(self) -> '_1528.ElectricalResistivity':
        '''ElectricalResistivity: 'Measurement' is the original name of this property.'''

        if _1528.ElectricalResistivity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ElectricalResistivity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_electrical_resistivity.setter
    def measurement_of_type_electrical_resistivity(self, value: '_1528.ElectricalResistivity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_electric_current(self) -> '_1529.ElectricCurrent':
        '''ElectricCurrent: 'Measurement' is the original name of this property.'''

        if _1529.ElectricCurrent.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ElectricCurrent. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_electric_current.setter
    def measurement_of_type_electric_current(self, value: '_1529.ElectricCurrent'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy(self) -> '_1530.Energy':
        '''Energy: 'Measurement' is the original name of this property.'''

        if _1530.Energy.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Energy. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_energy.setter
    def measurement_of_type_energy(self, value: '_1530.Energy'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy_per_unit_area(self) -> '_1531.EnergyPerUnitArea':
        '''EnergyPerUnitArea: 'Measurement' is the original name of this property.'''

        if _1531.EnergyPerUnitArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergyPerUnitArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_energy_per_unit_area.setter
    def measurement_of_type_energy_per_unit_area(self, value: '_1531.EnergyPerUnitArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy_per_unit_area_small(self) -> '_1532.EnergyPerUnitAreaSmall':
        '''EnergyPerUnitAreaSmall: 'Measurement' is the original name of this property.'''

        if _1532.EnergyPerUnitAreaSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergyPerUnitAreaSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_energy_per_unit_area_small.setter
    def measurement_of_type_energy_per_unit_area_small(self, value: '_1532.EnergyPerUnitAreaSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy_small(self) -> '_1533.EnergySmall':
        '''EnergySmall: 'Measurement' is the original name of this property.'''

        if _1533.EnergySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_energy_small.setter
    def measurement_of_type_energy_small(self, value: '_1533.EnergySmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_enum(self) -> '_1534.Enum':
        '''Enum: 'Measurement' is the original name of this property.'''

        if _1534.Enum.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Enum. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_enum.setter
    def measurement_of_type_enum(self, value: '_1534.Enum'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_flow_rate(self) -> '_1535.FlowRate':
        '''FlowRate: 'Measurement' is the original name of this property.'''

        if _1535.FlowRate.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FlowRate. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_flow_rate.setter
    def measurement_of_type_flow_rate(self, value: '_1535.FlowRate'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force(self) -> '_1536.Force':
        '''Force: 'Measurement' is the original name of this property.'''

        if _1536.Force.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Force. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_force.setter
    def measurement_of_type_force(self, value: '_1536.Force'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force_per_unit_length(self) -> '_1537.ForcePerUnitLength':
        '''ForcePerUnitLength: 'Measurement' is the original name of this property.'''

        if _1537.ForcePerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_force_per_unit_length.setter
    def measurement_of_type_force_per_unit_length(self, value: '_1537.ForcePerUnitLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force_per_unit_pressure(self) -> '_1538.ForcePerUnitPressure':
        '''ForcePerUnitPressure: 'Measurement' is the original name of this property.'''

        if _1538.ForcePerUnitPressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitPressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_force_per_unit_pressure.setter
    def measurement_of_type_force_per_unit_pressure(self, value: '_1538.ForcePerUnitPressure'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force_per_unit_temperature(self) -> '_1539.ForcePerUnitTemperature':
        '''ForcePerUnitTemperature: 'Measurement' is the original name of this property.'''

        if _1539.ForcePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_force_per_unit_temperature.setter
    def measurement_of_type_force_per_unit_temperature(self, value: '_1539.ForcePerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fraction_measurement_base(self) -> '_1540.FractionMeasurementBase':
        '''FractionMeasurementBase: 'Measurement' is the original name of this property.'''

        if _1540.FractionMeasurementBase.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FractionMeasurementBase. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_fraction_measurement_base.setter
    def measurement_of_type_fraction_measurement_base(self, value: '_1540.FractionMeasurementBase'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fraction_per_temperature(self) -> '_1541.FractionPerTemperature':
        '''FractionPerTemperature: 'Measurement' is the original name of this property.'''

        if _1541.FractionPerTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FractionPerTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_fraction_per_temperature.setter
    def measurement_of_type_fraction_per_temperature(self, value: '_1541.FractionPerTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_frequency(self) -> '_1542.Frequency':
        '''Frequency: 'Measurement' is the original name of this property.'''

        if _1542.Frequency.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Frequency. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_frequency.setter
    def measurement_of_type_frequency(self, value: '_1542.Frequency'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fuel_consumption_engine(self) -> '_1543.FuelConsumptionEngine':
        '''FuelConsumptionEngine: 'Measurement' is the original name of this property.'''

        if _1543.FuelConsumptionEngine.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FuelConsumptionEngine. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_fuel_consumption_engine.setter
    def measurement_of_type_fuel_consumption_engine(self, value: '_1543.FuelConsumptionEngine'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fuel_efficiency_vehicle(self) -> '_1544.FuelEfficiencyVehicle':
        '''FuelEfficiencyVehicle: 'Measurement' is the original name of this property.'''

        if _1544.FuelEfficiencyVehicle.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FuelEfficiencyVehicle. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_fuel_efficiency_vehicle.setter
    def measurement_of_type_fuel_efficiency_vehicle(self, value: '_1544.FuelEfficiencyVehicle'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_gradient(self) -> '_1545.Gradient':
        '''Gradient: 'Measurement' is the original name of this property.'''

        if _1545.Gradient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Gradient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_gradient.setter
    def measurement_of_type_gradient(self, value: '_1545.Gradient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_conductivity(self) -> '_1546.HeatConductivity':
        '''HeatConductivity: 'Measurement' is the original name of this property.'''

        if _1546.HeatConductivity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatConductivity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_heat_conductivity.setter
    def measurement_of_type_heat_conductivity(self, value: '_1546.HeatConductivity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_transfer(self) -> '_1547.HeatTransfer':
        '''HeatTransfer: 'Measurement' is the original name of this property.'''

        if _1547.HeatTransfer.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransfer. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_heat_transfer.setter
    def measurement_of_type_heat_transfer(self, value: '_1547.HeatTransfer'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1548.HeatTransferCoefficientForPlasticGearTooth':
        '''HeatTransferCoefficientForPlasticGearTooth: 'Measurement' is the original name of this property.'''

        if _1548.HeatTransferCoefficientForPlasticGearTooth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth.setter
    def measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self, value: '_1548.HeatTransferCoefficientForPlasticGearTooth'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_transfer_resistance(self) -> '_1549.HeatTransferResistance':
        '''HeatTransferResistance: 'Measurement' is the original name of this property.'''

        if _1549.HeatTransferResistance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransferResistance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_heat_transfer_resistance.setter
    def measurement_of_type_heat_transfer_resistance(self, value: '_1549.HeatTransferResistance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_impulse(self) -> '_1550.Impulse':
        '''Impulse: 'Measurement' is the original name of this property.'''

        if _1550.Impulse.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Impulse. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_impulse.setter
    def measurement_of_type_impulse(self, value: '_1550.Impulse'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_index(self) -> '_1551.Index':
        '''Index: 'Measurement' is the original name of this property.'''

        if _1551.Index.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Index. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_index.setter
    def measurement_of_type_index(self, value: '_1551.Index'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_inductance(self) -> '_1552.Inductance':
        '''Inductance: 'Measurement' is the original name of this property.'''

        if _1552.Inductance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Inductance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_inductance.setter
    def measurement_of_type_inductance(self, value: '_1552.Inductance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_integer(self) -> '_1553.Integer':
        '''Integer: 'Measurement' is the original name of this property.'''

        if _1553.Integer.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Integer. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_integer.setter
    def measurement_of_type_integer(self, value: '_1553.Integer'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_inverse_short_length(self) -> '_1554.InverseShortLength':
        '''InverseShortLength: 'Measurement' is the original name of this property.'''

        if _1554.InverseShortLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to InverseShortLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_inverse_short_length.setter
    def measurement_of_type_inverse_short_length(self, value: '_1554.InverseShortLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_inverse_short_time(self) -> '_1555.InverseShortTime':
        '''InverseShortTime: 'Measurement' is the original name of this property.'''

        if _1555.InverseShortTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to InverseShortTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_inverse_short_time.setter
    def measurement_of_type_inverse_short_time(self, value: '_1555.InverseShortTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_jerk(self) -> '_1556.Jerk':
        '''Jerk: 'Measurement' is the original name of this property.'''

        if _1556.Jerk.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Jerk. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_jerk.setter
    def measurement_of_type_jerk(self, value: '_1556.Jerk'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_kinematic_viscosity(self) -> '_1557.KinematicViscosity':
        '''KinematicViscosity: 'Measurement' is the original name of this property.'''

        if _1557.KinematicViscosity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to KinematicViscosity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_kinematic_viscosity.setter
    def measurement_of_type_kinematic_viscosity(self, value: '_1557.KinematicViscosity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_long(self) -> '_1558.LengthLong':
        '''LengthLong: 'Measurement' is the original name of this property.'''

        if _1558.LengthLong.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthLong. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_long.setter
    def measurement_of_type_length_long(self, value: '_1558.LengthLong'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_medium(self) -> '_1559.LengthMedium':
        '''LengthMedium: 'Measurement' is the original name of this property.'''

        if _1559.LengthMedium.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthMedium. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_medium.setter
    def measurement_of_type_length_medium(self, value: '_1559.LengthMedium'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_per_unit_temperature(self) -> '_1560.LengthPerUnitTemperature':
        '''LengthPerUnitTemperature: 'Measurement' is the original name of this property.'''

        if _1560.LengthPerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthPerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_per_unit_temperature.setter
    def measurement_of_type_length_per_unit_temperature(self, value: '_1560.LengthPerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_short(self) -> '_1561.LengthShort':
        '''LengthShort: 'Measurement' is the original name of this property.'''

        if _1561.LengthShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_short.setter
    def measurement_of_type_length_short(self, value: '_1561.LengthShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_to_the_fourth(self) -> '_1562.LengthToTheFourth':
        '''LengthToTheFourth: 'Measurement' is the original name of this property.'''

        if _1562.LengthToTheFourth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthToTheFourth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_to_the_fourth.setter
    def measurement_of_type_length_to_the_fourth(self, value: '_1562.LengthToTheFourth'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_very_long(self) -> '_1563.LengthVeryLong':
        '''LengthVeryLong: 'Measurement' is the original name of this property.'''

        if _1563.LengthVeryLong.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryLong. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_very_long.setter
    def measurement_of_type_length_very_long(self, value: '_1563.LengthVeryLong'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_very_short(self) -> '_1564.LengthVeryShort':
        '''LengthVeryShort: 'Measurement' is the original name of this property.'''

        if _1564.LengthVeryShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_very_short.setter
    def measurement_of_type_length_very_short(self, value: '_1564.LengthVeryShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_very_short_per_length_short(self) -> '_1565.LengthVeryShortPerLengthShort':
        '''LengthVeryShortPerLengthShort: 'Measurement' is the original name of this property.'''

        if _1565.LengthVeryShortPerLengthShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryShortPerLengthShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_very_short_per_length_short.setter
    def measurement_of_type_length_very_short_per_length_short(self, value: '_1565.LengthVeryShortPerLengthShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_angular_damping(self) -> '_1566.LinearAngularDamping':
        '''LinearAngularDamping: 'Measurement' is the original name of this property.'''

        if _1566.LinearAngularDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearAngularDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_linear_angular_damping.setter
    def measurement_of_type_linear_angular_damping(self, value: '_1566.LinearAngularDamping'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_angular_stiffness_cross_term(self) -> '_1567.LinearAngularStiffnessCrossTerm':
        '''LinearAngularStiffnessCrossTerm: 'Measurement' is the original name of this property.'''

        if _1567.LinearAngularStiffnessCrossTerm.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_linear_angular_stiffness_cross_term.setter
    def measurement_of_type_linear_angular_stiffness_cross_term(self, value: '_1567.LinearAngularStiffnessCrossTerm'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_damping(self) -> '_1568.LinearDamping':
        '''LinearDamping: 'Measurement' is the original name of this property.'''

        if _1568.LinearDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_linear_damping.setter
    def measurement_of_type_linear_damping(self, value: '_1568.LinearDamping'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_flexibility(self) -> '_1569.LinearFlexibility':
        '''LinearFlexibility: 'Measurement' is the original name of this property.'''

        if _1569.LinearFlexibility.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearFlexibility. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_linear_flexibility.setter
    def measurement_of_type_linear_flexibility(self, value: '_1569.LinearFlexibility'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_stiffness(self) -> '_1570.LinearStiffness':
        '''LinearStiffness: 'Measurement' is the original name of this property.'''

        if _1570.LinearStiffness.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearStiffness. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_linear_stiffness.setter
    def measurement_of_type_linear_stiffness(self, value: '_1570.LinearStiffness'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_magnetic_field_strength(self) -> '_1571.MagneticFieldStrength':
        '''MagneticFieldStrength: 'Measurement' is the original name of this property.'''

        if _1571.MagneticFieldStrength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MagneticFieldStrength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_magnetic_field_strength.setter
    def measurement_of_type_magnetic_field_strength(self, value: '_1571.MagneticFieldStrength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_magnetic_flux(self) -> '_1572.MagneticFlux':
        '''MagneticFlux: 'Measurement' is the original name of this property.'''

        if _1572.MagneticFlux.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MagneticFlux. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_magnetic_flux.setter
    def measurement_of_type_magnetic_flux(self, value: '_1572.MagneticFlux'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_magnetic_flux_density(self) -> '_1573.MagneticFluxDensity':
        '''MagneticFluxDensity: 'Measurement' is the original name of this property.'''

        if _1573.MagneticFluxDensity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MagneticFluxDensity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_magnetic_flux_density.setter
    def measurement_of_type_magnetic_flux_density(self, value: '_1573.MagneticFluxDensity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_magnetic_vector_potential(self) -> '_1574.MagneticVectorPotential':
        '''MagneticVectorPotential: 'Measurement' is the original name of this property.'''

        if _1574.MagneticVectorPotential.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MagneticVectorPotential. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_magnetic_vector_potential.setter
    def measurement_of_type_magnetic_vector_potential(self, value: '_1574.MagneticVectorPotential'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_mass(self) -> '_1575.Mass':
        '''Mass: 'Measurement' is the original name of this property.'''

        if _1575.Mass.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Mass. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_mass.setter
    def measurement_of_type_mass(self, value: '_1575.Mass'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_mass_per_unit_length(self) -> '_1576.MassPerUnitLength':
        '''MassPerUnitLength: 'Measurement' is the original name of this property.'''

        if _1576.MassPerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MassPerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_mass_per_unit_length.setter
    def measurement_of_type_mass_per_unit_length(self, value: '_1576.MassPerUnitLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_mass_per_unit_time(self) -> '_1577.MassPerUnitTime':
        '''MassPerUnitTime: 'Measurement' is the original name of this property.'''

        if _1577.MassPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MassPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_mass_per_unit_time.setter
    def measurement_of_type_mass_per_unit_time(self, value: '_1577.MassPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_moment_of_inertia(self) -> '_1578.MomentOfInertia':
        '''MomentOfInertia: 'Measurement' is the original name of this property.'''

        if _1578.MomentOfInertia.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentOfInertia. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_moment_of_inertia.setter
    def measurement_of_type_moment_of_inertia(self, value: '_1578.MomentOfInertia'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_moment_of_inertia_per_unit_length(self) -> '_1579.MomentOfInertiaPerUnitLength':
        '''MomentOfInertiaPerUnitLength: 'Measurement' is the original name of this property.'''

        if _1579.MomentOfInertiaPerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentOfInertiaPerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_moment_of_inertia_per_unit_length.setter
    def measurement_of_type_moment_of_inertia_per_unit_length(self, value: '_1579.MomentOfInertiaPerUnitLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_moment_per_unit_pressure(self) -> '_1580.MomentPerUnitPressure':
        '''MomentPerUnitPressure: 'Measurement' is the original name of this property.'''

        if _1580.MomentPerUnitPressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentPerUnitPressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_moment_per_unit_pressure.setter
    def measurement_of_type_moment_per_unit_pressure(self, value: '_1580.MomentPerUnitPressure'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_number(self) -> '_1581.Number':
        '''Number: 'Measurement' is the original name of this property.'''

        if _1581.Number.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Number. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_number.setter
    def measurement_of_type_number(self, value: '_1581.Number'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_percentage(self) -> '_1582.Percentage':
        '''Percentage: 'Measurement' is the original name of this property.'''

        if _1582.Percentage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Percentage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_percentage.setter
    def measurement_of_type_percentage(self, value: '_1582.Percentage'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power(self) -> '_1583.Power':
        '''Power: 'Measurement' is the original name of this property.'''

        if _1583.Power.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Power. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power.setter
    def measurement_of_type_power(self, value: '_1583.Power'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_per_small_area(self) -> '_1584.PowerPerSmallArea':
        '''PowerPerSmallArea: 'Measurement' is the original name of this property.'''

        if _1584.PowerPerSmallArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerPerSmallArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_per_small_area.setter
    def measurement_of_type_power_per_small_area(self, value: '_1584.PowerPerSmallArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_per_unit_time(self) -> '_1585.PowerPerUnitTime':
        '''PowerPerUnitTime: 'Measurement' is the original name of this property.'''

        if _1585.PowerPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_per_unit_time.setter
    def measurement_of_type_power_per_unit_time(self, value: '_1585.PowerPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small(self) -> '_1586.PowerSmall':
        '''PowerSmall: 'Measurement' is the original name of this property.'''

        if _1586.PowerSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_small.setter
    def measurement_of_type_power_small(self, value: '_1586.PowerSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_area(self) -> '_1587.PowerSmallPerArea':
        '''PowerSmallPerArea: 'Measurement' is the original name of this property.'''

        if _1587.PowerSmallPerArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_small_per_area.setter
    def measurement_of_type_power_small_per_area(self, value: '_1587.PowerSmallPerArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_mass(self) -> '_1588.PowerSmallPerMass':
        '''PowerSmallPerMass: 'Measurement' is the original name of this property.'''

        if _1588.PowerSmallPerMass.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerMass. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_small_per_mass.setter
    def measurement_of_type_power_small_per_mass(self, value: '_1588.PowerSmallPerMass'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1589.PowerSmallPerUnitAreaPerUnitTime':
        '''PowerSmallPerUnitAreaPerUnitTime: 'Measurement' is the original name of this property.'''

        if _1589.PowerSmallPerUnitAreaPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_small_per_unit_area_per_unit_time.setter
    def measurement_of_type_power_small_per_unit_area_per_unit_time(self, value: '_1589.PowerSmallPerUnitAreaPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_unit_time(self) -> '_1590.PowerSmallPerUnitTime':
        '''PowerSmallPerUnitTime: 'Measurement' is the original name of this property.'''

        if _1590.PowerSmallPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_small_per_unit_time.setter
    def measurement_of_type_power_small_per_unit_time(self, value: '_1590.PowerSmallPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_volume(self) -> '_1591.PowerSmallPerVolume':
        '''PowerSmallPerVolume: 'Measurement' is the original name of this property.'''

        if _1591.PowerSmallPerVolume.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerVolume. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_small_per_volume.setter
    def measurement_of_type_power_small_per_volume(self, value: '_1591.PowerSmallPerVolume'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure(self) -> '_1592.Pressure':
        '''Pressure: 'Measurement' is the original name of this property.'''

        if _1592.Pressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Pressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_pressure.setter
    def measurement_of_type_pressure(self, value: '_1592.Pressure'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure_per_unit_time(self) -> '_1593.PressurePerUnitTime':
        '''PressurePerUnitTime: 'Measurement' is the original name of this property.'''

        if _1593.PressurePerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressurePerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_pressure_per_unit_time.setter
    def measurement_of_type_pressure_per_unit_time(self, value: '_1593.PressurePerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure_velocity_product(self) -> '_1594.PressureVelocityProduct':
        '''PressureVelocityProduct: 'Measurement' is the original name of this property.'''

        if _1594.PressureVelocityProduct.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressureVelocityProduct. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_pressure_velocity_product.setter
    def measurement_of_type_pressure_velocity_product(self, value: '_1594.PressureVelocityProduct'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure_viscosity_coefficient(self) -> '_1595.PressureViscosityCoefficient':
        '''PressureViscosityCoefficient: 'Measurement' is the original name of this property.'''

        if _1595.PressureViscosityCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressureViscosityCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_pressure_viscosity_coefficient.setter
    def measurement_of_type_pressure_viscosity_coefficient(self, value: '_1595.PressureViscosityCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_price(self) -> '_1596.Price':
        '''Price: 'Measurement' is the original name of this property.'''

        if _1596.Price.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Price. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_price.setter
    def measurement_of_type_price(self, value: '_1596.Price'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_price_per_unit_mass(self) -> '_1597.PricePerUnitMass':
        '''PricePerUnitMass: 'Measurement' is the original name of this property.'''

        if _1597.PricePerUnitMass.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PricePerUnitMass. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_price_per_unit_mass.setter
    def measurement_of_type_price_per_unit_mass(self, value: '_1597.PricePerUnitMass'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_quadratic_angular_damping(self) -> '_1598.QuadraticAngularDamping':
        '''QuadraticAngularDamping: 'Measurement' is the original name of this property.'''

        if _1598.QuadraticAngularDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to QuadraticAngularDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_quadratic_angular_damping.setter
    def measurement_of_type_quadratic_angular_damping(self, value: '_1598.QuadraticAngularDamping'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_quadratic_drag(self) -> '_1599.QuadraticDrag':
        '''QuadraticDrag: 'Measurement' is the original name of this property.'''

        if _1599.QuadraticDrag.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to QuadraticDrag. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_quadratic_drag.setter
    def measurement_of_type_quadratic_drag(self, value: '_1599.QuadraticDrag'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_rescaled_measurement(self) -> '_1600.RescaledMeasurement':
        '''RescaledMeasurement: 'Measurement' is the original name of this property.'''

        if _1600.RescaledMeasurement.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to RescaledMeasurement. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_rescaled_measurement.setter
    def measurement_of_type_rescaled_measurement(self, value: '_1600.RescaledMeasurement'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_rotatum(self) -> '_1601.Rotatum':
        '''Rotatum: 'Measurement' is the original name of this property.'''

        if _1601.Rotatum.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Rotatum. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_rotatum.setter
    def measurement_of_type_rotatum(self, value: '_1601.Rotatum'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_safety_factor(self) -> '_1602.SafetyFactor':
        '''SafetyFactor: 'Measurement' is the original name of this property.'''

        if _1602.SafetyFactor.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SafetyFactor. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_safety_factor.setter
    def measurement_of_type_safety_factor(self, value: '_1602.SafetyFactor'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_specific_acoustic_impedance(self) -> '_1603.SpecificAcousticImpedance':
        '''SpecificAcousticImpedance: 'Measurement' is the original name of this property.'''

        if _1603.SpecificAcousticImpedance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SpecificAcousticImpedance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_specific_acoustic_impedance.setter
    def measurement_of_type_specific_acoustic_impedance(self, value: '_1603.SpecificAcousticImpedance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_specific_heat(self) -> '_1604.SpecificHeat':
        '''SpecificHeat: 'Measurement' is the original name of this property.'''

        if _1604.SpecificHeat.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SpecificHeat. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_specific_heat.setter
    def measurement_of_type_specific_heat(self, value: '_1604.SpecificHeat'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1605.SquareRootOfUnitForcePerUnitArea':
        '''SquareRootOfUnitForcePerUnitArea: 'Measurement' is the original name of this property.'''

        if _1605.SquareRootOfUnitForcePerUnitArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_square_root_of_unit_force_per_unit_area.setter
    def measurement_of_type_square_root_of_unit_force_per_unit_area(self, value: '_1605.SquareRootOfUnitForcePerUnitArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_stiffness_per_unit_face_width(self) -> '_1606.StiffnessPerUnitFaceWidth':
        '''StiffnessPerUnitFaceWidth: 'Measurement' is the original name of this property.'''

        if _1606.StiffnessPerUnitFaceWidth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to StiffnessPerUnitFaceWidth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_stiffness_per_unit_face_width.setter
    def measurement_of_type_stiffness_per_unit_face_width(self, value: '_1606.StiffnessPerUnitFaceWidth'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_stress(self) -> '_1607.Stress':
        '''Stress: 'Measurement' is the original name of this property.'''

        if _1607.Stress.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Stress. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_stress.setter
    def measurement_of_type_stress(self, value: '_1607.Stress'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_temperature(self) -> '_1608.Temperature':
        '''Temperature: 'Measurement' is the original name of this property.'''

        if _1608.Temperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Temperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_temperature.setter
    def measurement_of_type_temperature(self, value: '_1608.Temperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_temperature_difference(self) -> '_1609.TemperatureDifference':
        '''TemperatureDifference: 'Measurement' is the original name of this property.'''

        if _1609.TemperatureDifference.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TemperatureDifference. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_temperature_difference.setter
    def measurement_of_type_temperature_difference(self, value: '_1609.TemperatureDifference'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_temperature_per_unit_time(self) -> '_1610.TemperaturePerUnitTime':
        '''TemperaturePerUnitTime: 'Measurement' is the original name of this property.'''

        if _1610.TemperaturePerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TemperaturePerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_temperature_per_unit_time.setter
    def measurement_of_type_temperature_per_unit_time(self, value: '_1610.TemperaturePerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_text(self) -> '_1611.Text':
        '''Text: 'Measurement' is the original name of this property.'''

        if _1611.Text.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Text. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_text.setter
    def measurement_of_type_text(self, value: '_1611.Text'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_thermal_contact_coefficient(self) -> '_1612.ThermalContactCoefficient':
        '''ThermalContactCoefficient: 'Measurement' is the original name of this property.'''

        if _1612.ThermalContactCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermalContactCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_thermal_contact_coefficient.setter
    def measurement_of_type_thermal_contact_coefficient(self, value: '_1612.ThermalContactCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_thermal_expansion_coefficient(self) -> '_1613.ThermalExpansionCoefficient':
        '''ThermalExpansionCoefficient: 'Measurement' is the original name of this property.'''

        if _1613.ThermalExpansionCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermalExpansionCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_thermal_expansion_coefficient.setter
    def measurement_of_type_thermal_expansion_coefficient(self, value: '_1613.ThermalExpansionCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_thermo_elastic_factor(self) -> '_1614.ThermoElasticFactor':
        '''ThermoElasticFactor: 'Measurement' is the original name of this property.'''

        if _1614.ThermoElasticFactor.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermoElasticFactor. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_thermo_elastic_factor.setter
    def measurement_of_type_thermo_elastic_factor(self, value: '_1614.ThermoElasticFactor'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_time(self) -> '_1615.Time':
        '''Time: 'Measurement' is the original name of this property.'''

        if _1615.Time.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Time. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_time.setter
    def measurement_of_type_time(self, value: '_1615.Time'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_time_short(self) -> '_1616.TimeShort':
        '''TimeShort: 'Measurement' is the original name of this property.'''

        if _1616.TimeShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TimeShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_time_short.setter
    def measurement_of_type_time_short(self, value: '_1616.TimeShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_time_very_short(self) -> '_1617.TimeVeryShort':
        '''TimeVeryShort: 'Measurement' is the original name of this property.'''

        if _1617.TimeVeryShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TimeVeryShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_time_very_short.setter
    def measurement_of_type_time_very_short(self, value: '_1617.TimeVeryShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque(self) -> '_1618.Torque':
        '''Torque: 'Measurement' is the original name of this property.'''

        if _1618.Torque.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Torque. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_torque.setter
    def measurement_of_type_torque(self, value: '_1618.Torque'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_converter_inverse_k(self) -> '_1619.TorqueConverterInverseK':
        '''TorqueConverterInverseK: 'Measurement' is the original name of this property.'''

        if _1619.TorqueConverterInverseK.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorqueConverterInverseK. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_torque_converter_inverse_k.setter
    def measurement_of_type_torque_converter_inverse_k(self, value: '_1619.TorqueConverterInverseK'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_converter_k(self) -> '_1620.TorqueConverterK':
        '''TorqueConverterK: 'Measurement' is the original name of this property.'''

        if _1620.TorqueConverterK.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorqueConverterK. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_torque_converter_k.setter
    def measurement_of_type_torque_converter_k(self, value: '_1620.TorqueConverterK'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_per_current(self) -> '_1621.TorquePerCurrent':
        '''TorquePerCurrent: 'Measurement' is the original name of this property.'''

        if _1621.TorquePerCurrent.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorquePerCurrent. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_torque_per_current.setter
    def measurement_of_type_torque_per_current(self, value: '_1621.TorquePerCurrent'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_per_square_root_of_power(self) -> '_1622.TorquePerSquareRootOfPower':
        '''TorquePerSquareRootOfPower: 'Measurement' is the original name of this property.'''

        if _1622.TorquePerSquareRootOfPower.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorquePerSquareRootOfPower. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_torque_per_square_root_of_power.setter
    def measurement_of_type_torque_per_square_root_of_power(self, value: '_1622.TorquePerSquareRootOfPower'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_per_unit_temperature(self) -> '_1623.TorquePerUnitTemperature':
        '''TorquePerUnitTemperature: 'Measurement' is the original name of this property.'''

        if _1623.TorquePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorquePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_torque_per_unit_temperature.setter
    def measurement_of_type_torque_per_unit_temperature(self, value: '_1623.TorquePerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_velocity(self) -> '_1624.Velocity':
        '''Velocity: 'Measurement' is the original name of this property.'''

        if _1624.Velocity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Velocity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_velocity.setter
    def measurement_of_type_velocity(self, value: '_1624.Velocity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_velocity_small(self) -> '_1625.VelocitySmall':
        '''VelocitySmall: 'Measurement' is the original name of this property.'''

        if _1625.VelocitySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to VelocitySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_velocity_small.setter
    def measurement_of_type_velocity_small(self, value: '_1625.VelocitySmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_viscosity(self) -> '_1626.Viscosity':
        '''Viscosity: 'Measurement' is the original name of this property.'''

        if _1626.Viscosity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Viscosity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_viscosity.setter
    def measurement_of_type_viscosity(self, value: '_1626.Viscosity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_voltage(self) -> '_1627.Voltage':
        '''Voltage: 'Measurement' is the original name of this property.'''

        if _1627.Voltage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Voltage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_voltage.setter
    def measurement_of_type_voltage(self, value: '_1627.Voltage'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_voltage_per_angular_velocity(self) -> '_1628.VoltagePerAngularVelocity':
        '''VoltagePerAngularVelocity: 'Measurement' is the original name of this property.'''

        if _1628.VoltagePerAngularVelocity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to VoltagePerAngularVelocity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_voltage_per_angular_velocity.setter
    def measurement_of_type_voltage_per_angular_velocity(self, value: '_1628.VoltagePerAngularVelocity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_volume(self) -> '_1629.Volume':
        '''Volume: 'Measurement' is the original name of this property.'''

        if _1629.Volume.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Volume. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_volume.setter
    def measurement_of_type_volume(self, value: '_1629.Volume'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_wear_coefficient(self) -> '_1630.WearCoefficient':
        '''WearCoefficient: 'Measurement' is the original name of this property.'''

        if _1630.WearCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to WearCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_wear_coefficient.setter
    def measurement_of_type_wear_coefficient(self, value: '_1630.WearCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_yank(self) -> '_1631.Yank':
        '''Yank: 'Measurement' is the original name of this property.'''

        if _1631.Yank.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Yank. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_yank.setter
    def measurement_of_type_yank(self, value: '_1631.Yank'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def results(self) -> 'List[float]':
        '''List[float]: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Results, float)
        return value
