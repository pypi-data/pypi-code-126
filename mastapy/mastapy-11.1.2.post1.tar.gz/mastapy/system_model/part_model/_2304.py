'''_2304.py

Bolt
'''


from mastapy.bolts import _1381
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2305, _2306
from mastapy._internal.python_net import python_net_import

_BOLT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bolt')


__docformat__ = 'restructuredtext en'
__all__ = ('Bolt',)


class Bolt(_2306.Component):
    '''Bolt

    This is a mastapy class.
    '''

    TYPE = _BOLT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Bolt.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bolt(self) -> '_1381.LoadedBolt':
        '''LoadedBolt: 'LoadedBolt' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1381.LoadedBolt)(self.wrapped.LoadedBolt) if self.wrapped.LoadedBolt is not None else None

    @property
    def bolted_joint(self) -> '_2305.BoltedJoint':
        '''BoltedJoint: 'BoltedJoint' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2305.BoltedJoint)(self.wrapped.BoltedJoint) if self.wrapped.BoltedJoint is not None else None
