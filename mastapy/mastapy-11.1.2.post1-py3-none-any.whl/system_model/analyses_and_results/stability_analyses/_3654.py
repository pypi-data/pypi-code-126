'''_3654.py

ConnectorStabilityAnalysis
'''


from mastapy.system_model.part_model import _2309, _2302, _2327
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.couplings import _2458
from mastapy.system_model.analyses_and_results.stability_analyses import _3696
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ConnectorStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorStabilityAnalysis',)


class ConnectorStabilityAnalysis(_3696.MountableComponentStabilityAnalysis):
    '''ConnectorStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONNECTOR_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectorStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2309.Connector':
        '''Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2309.Connector.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Connector. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bearing(self) -> '_2302.Bearing':
        '''Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2302.Bearing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bearing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_oil_seal(self) -> '_2327.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2327.OilSeal.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to OilSeal. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_shaft_hub_connection(self) -> '_2458.ShaftHubConnection':
        '''ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2458.ShaftHubConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftHubConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None
