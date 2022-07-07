'''_1666.py

CustomReportStatusItem
'''


from mastapy.utility.report import _1652
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_STATUS_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportStatusItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportStatusItem',)


class CustomReportStatusItem(_1652.CustomReportDefinitionItem):
    '''CustomReportStatusItem

    This is a mastapy class.
    '''

    TYPE = _CUSTOM_REPORT_STATUS_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CustomReportStatusItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
