'''_4077.py

GearMeshCompoundPowerFlow
'''


from typing import List

from mastapy.gears.rating import _336
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _348
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _417
from mastapy.gears.rating.cylindrical import _435
from mastapy.gears.rating.conical import _509
from mastapy.gears.rating.concept import _514
from mastapy.system_model.analyses_and_results.power_flows import _3944
from mastapy.system_model.analyses_and_results.power_flows.compound import _4083
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'GearMeshCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundPowerFlow',)


class GearMeshCompoundPowerFlow(_4083.InterMountableComponentConnectionCompoundPowerFlow):
    '''GearMeshCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _GEAR_MESH_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh_duty_cycle_rating(self) -> '_336.MeshDutyCycleRating':
        '''MeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _336.MeshDutyCycleRating.TYPE not in self.wrapped.GearMeshDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to MeshDutyCycleRating. Expected: {}.'.format(self.wrapped.GearMeshDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMeshDutyCycleRating.__class__)(self.wrapped.GearMeshDutyCycleRating) if self.wrapped.GearMeshDutyCycleRating is not None else None

    @property
    def gear_mesh_duty_cycle_rating_of_type_worm_mesh_duty_cycle_rating(self) -> '_348.WormMeshDutyCycleRating':
        '''WormMeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _348.WormMeshDutyCycleRating.TYPE not in self.wrapped.GearMeshDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to WormMeshDutyCycleRating. Expected: {}.'.format(self.wrapped.GearMeshDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMeshDutyCycleRating.__class__)(self.wrapped.GearMeshDutyCycleRating) if self.wrapped.GearMeshDutyCycleRating is not None else None

    @property
    def gear_mesh_duty_cycle_rating_of_type_face_gear_mesh_duty_cycle_rating(self) -> '_417.FaceGearMeshDutyCycleRating':
        '''FaceGearMeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _417.FaceGearMeshDutyCycleRating.TYPE not in self.wrapped.GearMeshDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to FaceGearMeshDutyCycleRating. Expected: {}.'.format(self.wrapped.GearMeshDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMeshDutyCycleRating.__class__)(self.wrapped.GearMeshDutyCycleRating) if self.wrapped.GearMeshDutyCycleRating is not None else None

    @property
    def gear_mesh_duty_cycle_rating_of_type_cylindrical_mesh_duty_cycle_rating(self) -> '_435.CylindricalMeshDutyCycleRating':
        '''CylindricalMeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _435.CylindricalMeshDutyCycleRating.TYPE not in self.wrapped.GearMeshDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to CylindricalMeshDutyCycleRating. Expected: {}.'.format(self.wrapped.GearMeshDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMeshDutyCycleRating.__class__)(self.wrapped.GearMeshDutyCycleRating) if self.wrapped.GearMeshDutyCycleRating is not None else None

    @property
    def gear_mesh_duty_cycle_rating_of_type_conical_mesh_duty_cycle_rating(self) -> '_509.ConicalMeshDutyCycleRating':
        '''ConicalMeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _509.ConicalMeshDutyCycleRating.TYPE not in self.wrapped.GearMeshDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to ConicalMeshDutyCycleRating. Expected: {}.'.format(self.wrapped.GearMeshDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMeshDutyCycleRating.__class__)(self.wrapped.GearMeshDutyCycleRating) if self.wrapped.GearMeshDutyCycleRating is not None else None

    @property
    def gear_mesh_duty_cycle_rating_of_type_concept_gear_mesh_duty_cycle_rating(self) -> '_514.ConceptGearMeshDutyCycleRating':
        '''ConceptGearMeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _514.ConceptGearMeshDutyCycleRating.TYPE not in self.wrapped.GearMeshDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to ConceptGearMeshDutyCycleRating. Expected: {}.'.format(self.wrapped.GearMeshDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMeshDutyCycleRating.__class__)(self.wrapped.GearMeshDutyCycleRating) if self.wrapped.GearMeshDutyCycleRating is not None else None

    @property
    def connection_analysis_cases(self) -> 'List[_3944.GearMeshPowerFlow]':
        '''List[GearMeshPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_3944.GearMeshPowerFlow))
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3944.GearMeshPowerFlow]':
        '''List[GearMeshPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_3944.GearMeshPowerFlow))
        return value
