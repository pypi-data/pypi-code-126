'''_1370.py

BoltMaterialDatabase
'''


from mastapy.bolts import _1366, _1369
from mastapy._internal.python_net import python_net_import

_BOLT_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Bolts', 'BoltMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltMaterialDatabase',)


class BoltMaterialDatabase(_1366.BoltedJointMaterialDatabase['_1369.BoltMaterial']):
    '''BoltMaterialDatabase

    This is a mastapy class.
    '''

    TYPE = _BOLT_MATERIAL_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
