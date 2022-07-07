'''_6189.py

MassDiscDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2323
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6754
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6236
from mastapy._internal.python_net import python_net_import

_MASS_DISC_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'MassDiscDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscDynamicAnalysis',)


class MassDiscDynamicAnalysis(_6236.VirtualComponentDynamicAnalysis):
    '''MassDiscDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _MASS_DISC_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2323.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2323.MassDisc)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6754.MassDiscLoadCase':
        '''MassDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6754.MassDiscLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def planetaries(self) -> 'List[MassDiscDynamicAnalysis]':
        '''List[MassDiscDynamicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(MassDiscDynamicAnalysis))
        return value
