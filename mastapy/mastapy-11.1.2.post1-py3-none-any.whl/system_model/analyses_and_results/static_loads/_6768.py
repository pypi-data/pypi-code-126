'''_6768.py

PlanetCarrierLoadCase
'''


from typing import List

from mastapy.system_model.part_model import _2330
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6767, _6757
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PlanetCarrierLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierLoadCase',)


class PlanetCarrierLoadCase(_6757.MountableComponentLoadCase):
    '''PlanetCarrierLoadCase

    This is a mastapy class.
    '''

    TYPE = _PLANET_CARRIER_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetCarrierLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2330.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2330.PlanetCarrier)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def planet_manufacture_errors(self) -> 'List[_6767.PlanetarySocketManufactureError]':
        '''List[PlanetarySocketManufactureError]: 'PlanetManufactureErrors' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetManufactureErrors, constructor.new(_6767.PlanetarySocketManufactureError))
        return value
