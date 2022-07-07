'''_4229.py

MassDiscParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model import _2323
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6754
from mastapy.system_model.analyses_and_results.system_deflections import _2634
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4287
from mastapy._internal.python_net import python_net_import

_MASS_DISC_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'MassDiscParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscParametricStudyTool',)


class MassDiscParametricStudyTool(_4287.VirtualComponentParametricStudyTool):
    '''MassDiscParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _MASS_DISC_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscParametricStudyTool.TYPE'):
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
    def planetaries(self) -> 'List[MassDiscParametricStudyTool]':
        '''List[MassDiscParametricStudyTool]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(MassDiscParametricStudyTool))
        return value

    @property
    def component_system_deflection_results(self) -> 'List[_2634.MassDiscSystemDeflection]':
        '''List[MassDiscSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2634.MassDiscSystemDeflection))
        return value
