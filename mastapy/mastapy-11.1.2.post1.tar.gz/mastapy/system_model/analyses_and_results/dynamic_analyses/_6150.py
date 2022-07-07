'''_6150.py

CouplingConnectionDynamicAnalysis
'''


from mastapy.system_model.connections_and_sockets.couplings import (
    _2208, _2204, _2206, _2210,
    _2212, _2214
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6179
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'CouplingConnectionDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionDynamicAnalysis',)


class CouplingConnectionDynamicAnalysis(_6179.InterMountableComponentConnectionDynamicAnalysis):
    '''CouplingConnectionDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _COUPLING_CONNECTION_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CouplingConnectionDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2208.CouplingConnection':
        '''CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2208.CouplingConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CouplingConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectionDesign.__class__)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_design_of_type_clutch_connection(self) -> '_2204.ClutchConnection':
        '''ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2204.ClutchConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ClutchConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectionDesign.__class__)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_design_of_type_concept_coupling_connection(self) -> '_2206.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2206.ConceptCouplingConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConceptCouplingConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectionDesign.__class__)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_design_of_type_part_to_part_shear_coupling_connection(self) -> '_2210.PartToPartShearCouplingConnection':
        '''PartToPartShearCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2210.PartToPartShearCouplingConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to PartToPartShearCouplingConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectionDesign.__class__)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_design_of_type_spring_damper_connection(self) -> '_2212.SpringDamperConnection':
        '''SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2212.SpringDamperConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to SpringDamperConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectionDesign.__class__)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_design_of_type_torque_converter_connection(self) -> '_2214.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2214.TorqueConverterConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to TorqueConverterConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectionDesign.__class__)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None
