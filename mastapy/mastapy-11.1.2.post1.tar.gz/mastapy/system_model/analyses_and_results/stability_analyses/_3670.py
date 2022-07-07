'''_3670.py

DatumStabilityAnalysis
'''


from mastapy.system_model.part_model import _2310
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6703
from mastapy.system_model.analyses_and_results.stability_analyses import _3643
from mastapy._internal.python_net import python_net_import

_DATUM_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'DatumStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumStabilityAnalysis',)


class DatumStabilityAnalysis(_3643.ComponentStabilityAnalysis):
    '''DatumStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _DATUM_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2310.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2310.Datum)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6703.DatumLoadCase':
        '''DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6703.DatumLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
