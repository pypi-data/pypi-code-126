'''_5355.py

TorqueConverterMultibodyDynamicsAnalysis
'''


from mastapy.system_model.part_model.couplings import _2467
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6806
from mastapy.system_model.analyses_and_results.mbd_analyses import _5264
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'TorqueConverterMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterMultibodyDynamicsAnalysis',)


class TorqueConverterMultibodyDynamicsAnalysis(_5264.CouplingMultibodyDynamicsAnalysis):
    '''TorqueConverterMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2467.TorqueConverter':
        '''TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2467.TorqueConverter)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6806.TorqueConverterLoadCase':
        '''TorqueConverterLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6806.TorqueConverterLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None
