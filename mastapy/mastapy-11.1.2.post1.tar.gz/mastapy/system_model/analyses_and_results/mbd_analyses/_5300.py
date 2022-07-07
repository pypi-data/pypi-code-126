'''_5300.py

KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
'''


from mastapy.system_model.part_model.gears import _2398
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6748
from mastapy.system_model.analyses_and_results.mbd_analyses import _5297
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis',)


class KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis(_5297.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis):
    '''KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2398.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2398.KlingelnbergCycloPalloidHypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6748.KlingelnbergCycloPalloidHypoidGearLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6748.KlingelnbergCycloPalloidHypoidGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
