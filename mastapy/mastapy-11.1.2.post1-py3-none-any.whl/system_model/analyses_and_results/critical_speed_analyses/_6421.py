'''_6421.py

CVTCriticalSpeedAnalysis
'''


from mastapy.system_model.part_model.couplings import _2446
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6388
from mastapy._internal.python_net import python_net_import

_CVT_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'CVTCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTCriticalSpeedAnalysis',)


class CVTCriticalSpeedAnalysis(_6388.BeltDriveCriticalSpeedAnalysis):
    '''CVTCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _CVT_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CVTCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2446.CVT':
        '''CVT: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2446.CVT)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None
