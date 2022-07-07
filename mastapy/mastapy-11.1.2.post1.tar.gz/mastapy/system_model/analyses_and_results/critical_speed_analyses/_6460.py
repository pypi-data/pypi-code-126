'''_6460.py

PartToPartShearCouplingConnectionCriticalSpeedAnalysis
'''


from mastapy.system_model.connections_and_sockets.couplings import _2210
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6762
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6415
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'PartToPartShearCouplingConnectionCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingConnectionCriticalSpeedAnalysis',)


class PartToPartShearCouplingConnectionCriticalSpeedAnalysis(_6415.CouplingConnectionCriticalSpeedAnalysis):
    '''PartToPartShearCouplingConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingConnectionCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2210.PartToPartShearCouplingConnection':
        '''PartToPartShearCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2210.PartToPartShearCouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6762.PartToPartShearCouplingConnectionLoadCase':
        '''PartToPartShearCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6762.PartToPartShearCouplingConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
