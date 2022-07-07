'''_2126.py

Databases
'''


from mastapy.bearings import _1769
from mastapy._internal import constructor
from mastapy.bolts import _1368, _1370, _1375
from mastapy.gears.gear_set_pareto_optimiser import (
    _885, _886, _889, _890,
    _895, _896, _898, _899,
    _900, _901
)
from mastapy.gears.manufacturing.bevel import _765
from mastapy.gears.manufacturing.cylindrical.cutters import (
    _688, _694, _699, _700
)
from mastapy.gears.manufacturing.cylindrical import _580, _591
from mastapy.gears.materials import (
    _551, _553, _554, _555,
    _558, _565, _572
)
from mastapy.system_model.optimization import _2093, _2102
from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2424
from mastapy.materials import _221, _222, _241
from mastapy.shafts import _25
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_DATABASES = python_net_import('SMT.MastaAPI.SystemModel.DatabaseAccess', 'Databases')


__docformat__ = 'restructuredtext en'
__all__ = ('Databases',)


class Databases(_0.APIBase):
    '''Databases

    This is a mastapy class.
    '''

    TYPE = _DATABASES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Databases.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rolling_bearing_database(self) -> '_1769.RollingBearingDatabase':
        '''RollingBearingDatabase: 'RollingBearingDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1769.RollingBearingDatabase)(self.wrapped.RollingBearingDatabase) if self.wrapped.RollingBearingDatabase is not None else None

    @property
    def bolt_geometry_database(self) -> '_1368.BoltGeometryDatabase':
        '''BoltGeometryDatabase: 'BoltGeometryDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1368.BoltGeometryDatabase)(self.wrapped.BoltGeometryDatabase) if self.wrapped.BoltGeometryDatabase is not None else None

    @property
    def bolt_material_database(self) -> '_1370.BoltMaterialDatabase':
        '''BoltMaterialDatabase: 'BoltMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1370.BoltMaterialDatabase)(self.wrapped.BoltMaterialDatabase) if self.wrapped.BoltMaterialDatabase is not None else None

    @property
    def clamped_section_material_database(self) -> '_1375.ClampedSectionMaterialDatabase':
        '''ClampedSectionMaterialDatabase: 'ClampedSectionMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1375.ClampedSectionMaterialDatabase)(self.wrapped.ClampedSectionMaterialDatabase) if self.wrapped.ClampedSectionMaterialDatabase is not None else None

    @property
    def micro_geometry_gear_set_design_space_search_strategy_database(self) -> '_885.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase':
        '''MicroGeometryGearSetDesignSpaceSearchStrategyDatabase: 'MicroGeometryGearSetDesignSpaceSearchStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_885.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase)(self.wrapped.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase) if self.wrapped.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase is not None else None

    @property
    def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(self) -> '_886.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase':
        '''MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase: 'MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_886.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase)(self.wrapped.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase) if self.wrapped.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase is not None else None

    @property
    def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_889.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase':
        '''ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_889.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase)(self.wrapped.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase) if self.wrapped.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase is not None else None

    @property
    def pareto_cylindrical_gear_set_optimisation_strategy_database(self) -> '_890.ParetoCylindricalGearSetOptimisationStrategyDatabase':
        '''ParetoCylindricalGearSetOptimisationStrategyDatabase: 'ParetoCylindricalGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_890.ParetoCylindricalGearSetOptimisationStrategyDatabase)(self.wrapped.ParetoCylindricalGearSetOptimisationStrategyDatabase) if self.wrapped.ParetoCylindricalGearSetOptimisationStrategyDatabase is not None else None

    @property
    def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_895.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase':
        '''ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_895.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase)(self.wrapped.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase) if self.wrapped.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase is not None else None

    @property
    def pareto_hypoid_gear_set_optimisation_strategy_database(self) -> '_896.ParetoHypoidGearSetOptimisationStrategyDatabase':
        '''ParetoHypoidGearSetOptimisationStrategyDatabase: 'ParetoHypoidGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_896.ParetoHypoidGearSetOptimisationStrategyDatabase)(self.wrapped.ParetoHypoidGearSetOptimisationStrategyDatabase) if self.wrapped.ParetoHypoidGearSetOptimisationStrategyDatabase is not None else None

    @property
    def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_898.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase':
        '''ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_898.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase)(self.wrapped.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase) if self.wrapped.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase is not None else None

    @property
    def pareto_spiral_bevel_gear_set_optimisation_strategy_database(self) -> '_899.ParetoSpiralBevelGearSetOptimisationStrategyDatabase':
        '''ParetoSpiralBevelGearSetOptimisationStrategyDatabase: 'ParetoSpiralBevelGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_899.ParetoSpiralBevelGearSetOptimisationStrategyDatabase)(self.wrapped.ParetoSpiralBevelGearSetOptimisationStrategyDatabase) if self.wrapped.ParetoSpiralBevelGearSetOptimisationStrategyDatabase is not None else None

    @property
    def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_900.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase':
        '''ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_900.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase)(self.wrapped.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase) if self.wrapped.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase is not None else None

    @property
    def pareto_straight_bevel_gear_set_optimisation_strategy_database(self) -> '_901.ParetoStraightBevelGearSetOptimisationStrategyDatabase':
        '''ParetoStraightBevelGearSetOptimisationStrategyDatabase: 'ParetoStraightBevelGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_901.ParetoStraightBevelGearSetOptimisationStrategyDatabase)(self.wrapped.ParetoStraightBevelGearSetOptimisationStrategyDatabase) if self.wrapped.ParetoStraightBevelGearSetOptimisationStrategyDatabase is not None else None

    @property
    def manufacturing_machine_database(self) -> '_765.ManufacturingMachineDatabase':
        '''ManufacturingMachineDatabase: 'ManufacturingMachineDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_765.ManufacturingMachineDatabase)(self.wrapped.ManufacturingMachineDatabase) if self.wrapped.ManufacturingMachineDatabase is not None else None

    @property
    def cylindrical_formed_wheel_grinder_database(self) -> '_688.CylindricalFormedWheelGrinderDatabase':
        '''CylindricalFormedWheelGrinderDatabase: 'CylindricalFormedWheelGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_688.CylindricalFormedWheelGrinderDatabase)(self.wrapped.CylindricalFormedWheelGrinderDatabase) if self.wrapped.CylindricalFormedWheelGrinderDatabase is not None else None

    @property
    def cylindrical_gear_plunge_shaver_database(self) -> '_694.CylindricalGearPlungeShaverDatabase':
        '''CylindricalGearPlungeShaverDatabase: 'CylindricalGearPlungeShaverDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_694.CylindricalGearPlungeShaverDatabase)(self.wrapped.CylindricalGearPlungeShaverDatabase) if self.wrapped.CylindricalGearPlungeShaverDatabase is not None else None

    @property
    def cylindrical_gear_shaver_database(self) -> '_699.CylindricalGearShaverDatabase':
        '''CylindricalGearShaverDatabase: 'CylindricalGearShaverDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_699.CylindricalGearShaverDatabase)(self.wrapped.CylindricalGearShaverDatabase) if self.wrapped.CylindricalGearShaverDatabase is not None else None

    @property
    def cylindrical_worm_grinder_database(self) -> '_700.CylindricalWormGrinderDatabase':
        '''CylindricalWormGrinderDatabase: 'CylindricalWormGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_700.CylindricalWormGrinderDatabase)(self.wrapped.CylindricalWormGrinderDatabase) if self.wrapped.CylindricalWormGrinderDatabase is not None else None

    @property
    def cylindrical_hob_database(self) -> '_580.CylindricalHobDatabase':
        '''CylindricalHobDatabase: 'CylindricalHobDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_580.CylindricalHobDatabase)(self.wrapped.CylindricalHobDatabase) if self.wrapped.CylindricalHobDatabase is not None else None

    @property
    def cylindrical_shaper_database(self) -> '_591.CylindricalShaperDatabase':
        '''CylindricalShaperDatabase: 'CylindricalShaperDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_591.CylindricalShaperDatabase)(self.wrapped.CylindricalShaperDatabase) if self.wrapped.CylindricalShaperDatabase is not None else None

    @property
    def bevel_gear_iso_material_database(self) -> '_551.BevelGearIsoMaterialDatabase':
        '''BevelGearIsoMaterialDatabase: 'BevelGearIsoMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_551.BevelGearIsoMaterialDatabase)(self.wrapped.BevelGearIsoMaterialDatabase) if self.wrapped.BevelGearIsoMaterialDatabase is not None else None

    @property
    def bevel_gear_material_database(self) -> '_553.BevelGearMaterialDatabase':
        '''BevelGearMaterialDatabase: 'BevelGearMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_553.BevelGearMaterialDatabase)(self.wrapped.BevelGearMaterialDatabase) if self.wrapped.BevelGearMaterialDatabase is not None else None

    @property
    def cylindrical_gear_agma_material_database(self) -> '_554.CylindricalGearAGMAMaterialDatabase':
        '''CylindricalGearAGMAMaterialDatabase: 'CylindricalGearAGMAMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_554.CylindricalGearAGMAMaterialDatabase)(self.wrapped.CylindricalGearAGMAMaterialDatabase) if self.wrapped.CylindricalGearAGMAMaterialDatabase is not None else None

    @property
    def cylindrical_gear_iso_material_database(self) -> '_555.CylindricalGearISOMaterialDatabase':
        '''CylindricalGearISOMaterialDatabase: 'CylindricalGearISOMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_555.CylindricalGearISOMaterialDatabase)(self.wrapped.CylindricalGearISOMaterialDatabase) if self.wrapped.CylindricalGearISOMaterialDatabase is not None else None

    @property
    def cylindrical_gear_plastic_material_database(self) -> '_558.CylindricalGearPlasticMaterialDatabase':
        '''CylindricalGearPlasticMaterialDatabase: 'CylindricalGearPlasticMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_558.CylindricalGearPlasticMaterialDatabase)(self.wrapped.CylindricalGearPlasticMaterialDatabase) if self.wrapped.CylindricalGearPlasticMaterialDatabase is not None else None

    @property
    def klingelnberg_conical_gear_material_database(self) -> '_565.KlingelnbergConicalGearMaterialDatabase':
        '''KlingelnbergConicalGearMaterialDatabase: 'KlingelnbergConicalGearMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_565.KlingelnbergConicalGearMaterialDatabase)(self.wrapped.KlingelnbergConicalGearMaterialDatabase) if self.wrapped.KlingelnbergConicalGearMaterialDatabase is not None else None

    @property
    def raw_material_database(self) -> '_572.RawMaterialDatabase':
        '''RawMaterialDatabase: 'RawMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_572.RawMaterialDatabase)(self.wrapped.RawMaterialDatabase) if self.wrapped.RawMaterialDatabase is not None else None

    @property
    def conical_gear_optimization_strategy_database(self) -> '_2093.ConicalGearOptimizationStrategyDatabase':
        '''ConicalGearOptimizationStrategyDatabase: 'ConicalGearOptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2093.ConicalGearOptimizationStrategyDatabase)(self.wrapped.ConicalGearOptimizationStrategyDatabase) if self.wrapped.ConicalGearOptimizationStrategyDatabase is not None else None

    @property
    def optimization_strategy_database(self) -> '_2102.OptimizationStrategyDatabase':
        '''OptimizationStrategyDatabase: 'OptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2102.OptimizationStrategyDatabase)(self.wrapped.OptimizationStrategyDatabase) if self.wrapped.OptimizationStrategyDatabase is not None else None

    @property
    def supercharger_rotor_set_database(self) -> '_2424.SuperchargerRotorSetDatabase':
        '''SuperchargerRotorSetDatabase: 'SuperchargerRotorSetDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2424.SuperchargerRotorSetDatabase)(self.wrapped.SuperchargerRotorSetDatabase) if self.wrapped.SuperchargerRotorSetDatabase is not None else None

    @property
    def bearing_material_database(self) -> '_221.BearingMaterialDatabase':
        '''BearingMaterialDatabase: 'BearingMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_221.BearingMaterialDatabase)(self.wrapped.BearingMaterialDatabase) if self.wrapped.BearingMaterialDatabase is not None else None

    @property
    def component_material_database(self) -> '_222.ComponentMaterialDatabase':
        '''ComponentMaterialDatabase: 'ComponentMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_222.ComponentMaterialDatabase)(self.wrapped.ComponentMaterialDatabase) if self.wrapped.ComponentMaterialDatabase is not None else None

    @property
    def lubrication_detail_database(self) -> '_241.LubricationDetailDatabase':
        '''LubricationDetailDatabase: 'LubricationDetailDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_241.LubricationDetailDatabase)(self.wrapped.LubricationDetailDatabase) if self.wrapped.LubricationDetailDatabase is not None else None

    @property
    def shaft_material_database(self) -> '_25.ShaftMaterialDatabase':
        '''ShaftMaterialDatabase: 'ShaftMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_25.ShaftMaterialDatabase)(self.wrapped.ShaftMaterialDatabase) if self.wrapped.ShaftMaterialDatabase is not None else None
