'''_3395.py

CouplingSteadyStateSynchronousResponse
'''


from mastapy.system_model.part_model.couplings import (
    _2443, _2438, _2441, _2448,
    _2460, _2467
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3455
from mastapy._internal.python_net import python_net_import

_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'CouplingSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingSteadyStateSynchronousResponse',)


class CouplingSteadyStateSynchronousResponse(_3455.SpecialisedAssemblySteadyStateSynchronousResponse):
    '''CouplingSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CouplingSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2443.Coupling':
        '''Coupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2443.Coupling.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Coupling. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_clutch(self) -> '_2438.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2438.Clutch.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Clutch. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_concept_coupling(self) -> '_2441.ConceptCoupling':
        '''ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2441.ConceptCoupling.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to ConceptCoupling. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_part_to_part_shear_coupling(self) -> '_2448.PartToPartShearCoupling':
        '''PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2448.PartToPartShearCoupling.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to PartToPartShearCoupling. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_spring_damper(self) -> '_2460.SpringDamper':
        '''SpringDamper: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2460.SpringDamper.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to SpringDamper. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_torque_converter(self) -> '_2467.TorqueConverter':
        '''TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2467.TorqueConverter.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to TorqueConverter. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None
