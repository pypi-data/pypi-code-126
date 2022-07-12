# -*- coding: utf-8 -*-
import sys

from xltmpl import worksheet as _worksheet

from openpyxl.workbook import workbook as _workbook
sys.modules['openpyxl.worksheet.worksheet'] = _worksheet
sys.modules['openpyxl.workbook.workbook'] = _workbook
_workbook.Worksheet = _worksheet.Worksheet

from .xltmpl import XlTemplate, XlsTemplate, XlsxTemplate
