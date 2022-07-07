'''_1195.py

CADElectricMachineDetail
'''


from mastapy.nodal_analysis.geometry_modeller_link import _146
from mastapy._internal import constructor
from mastapy.electric_machines import _1206
from mastapy._internal.python_net import python_net_import

_CAD_ELECTRIC_MACHINE_DETAIL = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADElectricMachineDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('CADElectricMachineDetail',)


class CADElectricMachineDetail(_1206.ElectricMachineDetail):
    '''CADElectricMachineDetail

    This is a mastapy class.
    '''

    TYPE = _CAD_ELECTRIC_MACHINE_DETAIL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CADElectricMachineDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_modeller_dimensions(self) -> '_146.GeometryModellerDimensions':
        '''GeometryModellerDimensions: 'GeometryModellerDimensions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_146.GeometryModellerDimensions)(self.wrapped.GeometryModellerDimensions) if self.wrapped.GeometryModellerDimensions is not None else None

    def reread_geometry_from_geometry_modeller(self):
        ''' 'RereadGeometryFromGeometryModeller' is the original name of this method.'''

        self.wrapped.RereadGeometryFromGeometryModeller()
