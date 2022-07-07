'''_1250.py

StatorRotorMaterial
'''


from mastapy.math_utility import _1435
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility_gui.charts import (
    _1745, _1736, _1741, _1742
)
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines import _1194, _1227
from mastapy.materials import _242
from mastapy._internal.python_net import python_net_import

_STATOR_ROTOR_MATERIAL = python_net_import('SMT.MastaAPI.ElectricMachines', 'StatorRotorMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('StatorRotorMaterial',)


class StatorRotorMaterial(_242.Material):
    '''StatorRotorMaterial

    This is a mastapy class.
    '''

    TYPE = _STATOR_ROTOR_MATERIAL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StatorRotorMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bh_curve(self) -> '_1435.Vector2DListAccessor':
        '''Vector2DListAccessor: 'BHCurve' is the original name of this property.'''

        return constructor.new(_1435.Vector2DListAccessor)(self.wrapped.BHCurve) if self.wrapped.BHCurve is not None else None

    @bh_curve.setter
    def bh_curve(self, value: '_1435.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.BHCurve = value

    @property
    def bh_curve_plot(self) -> '_1745.TwoDChartDefinition':
        '''TwoDChartDefinition: 'BHCurvePlot' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1745.TwoDChartDefinition.TYPE not in self.wrapped.BHCurvePlot.__class__.__mro__:
            raise CastException('Failed to cast bh_curve_plot to TwoDChartDefinition. Expected: {}.'.format(self.wrapped.BHCurvePlot.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BHCurvePlot.__class__)(self.wrapped.BHCurvePlot) if self.wrapped.BHCurvePlot is not None else None

    @property
    def bh_curve_extrapolation_method(self) -> '_1194.BHCurveExtrapolationMethod':
        '''BHCurveExtrapolationMethod: 'BHCurveExtrapolationMethod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.BHCurveExtrapolationMethod)
        return constructor.new(_1194.BHCurveExtrapolationMethod)(value) if value is not None else None

    @bh_curve_extrapolation_method.setter
    def bh_curve_extrapolation_method(self, value: '_1194.BHCurveExtrapolationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.BHCurveExtrapolationMethod = value

    @property
    def number_of_points_for_bh_curve_extrapolation(self) -> 'int':
        '''int: 'NumberOfPointsForBHCurveExtrapolation' is the original name of this property.'''

        return self.wrapped.NumberOfPointsForBHCurveExtrapolation

    @number_of_points_for_bh_curve_extrapolation.setter
    def number_of_points_for_bh_curve_extrapolation(self, value: 'int'):
        self.wrapped.NumberOfPointsForBHCurveExtrapolation = int(value) if value else 0

    @property
    def maximum_h_for_bh_curve_extrapolation(self) -> 'float':
        '''float: 'MaximumHForBHCurveExtrapolation' is the original name of this property.'''

        return self.wrapped.MaximumHForBHCurveExtrapolation

    @maximum_h_for_bh_curve_extrapolation.setter
    def maximum_h_for_bh_curve_extrapolation(self, value: 'float'):
        self.wrapped.MaximumHForBHCurveExtrapolation = float(value) if value else 0.0

    @property
    def iron_loss_coefficients(self) -> '_1227.IronLossCoefficients':
        '''IronLossCoefficients: 'IronLossCoefficients' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1227.IronLossCoefficients)(self.wrapped.IronLossCoefficients) if self.wrapped.IronLossCoefficients is not None else None
