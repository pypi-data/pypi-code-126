'''_6458.py

OilSealCriticalSpeedAnalysis
'''


from mastapy.system_model.part_model import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6759
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6414
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'OilSealCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealCriticalSpeedAnalysis',)


class OilSealCriticalSpeedAnalysis(_6414.ConnectorCriticalSpeedAnalysis):
    '''OilSealCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _OIL_SEAL_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OilSealCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2327.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2327.OilSeal)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6759.OilSealLoadCase':
        '''OilSealLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6759.OilSealLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
