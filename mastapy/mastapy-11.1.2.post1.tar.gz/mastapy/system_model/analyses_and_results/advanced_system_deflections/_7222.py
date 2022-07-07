'''_7222.py

SynchroniserPartAdvancedSystemDeflection
'''


from mastapy.system_model.part_model.couplings import _2465, _2464, _2466
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7144
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'SynchroniserPartAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartAdvancedSystemDeflection',)


class SynchroniserPartAdvancedSystemDeflection(_7144.CouplingHalfAdvancedSystemDeflection):
    '''SynchroniserPartAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_PART_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserPartAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2465.SynchroniserPart':
        '''SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2465.SynchroniserPart.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserPart. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_synchroniser_half(self) -> '_2464.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2464.SynchroniserHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_synchroniser_sleeve(self) -> '_2466.SynchroniserSleeve':
        '''SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2466.SynchroniserSleeve.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None
