'''Module to run Code Radar.'''

import sys
import os

from .pylint import runPylint, PylintReport
from .pytest import runPytest, CoverageReport
from .flake8 import runFlake8
from .gitlab import Gitlab
  
def _getReportTemplateTxt():
    template = """
Code Quality Summary
--------------------------------------------------
Pytest:
  Test coverage: <coverage>
 
--------------------------------------------------
Pylint Score:  <pylint_score>
  Missing docstrings:             <missing_docstrings>
 
  Needs Refactoring:
    Too complex:                  <too_complex_num> (max=<too_complex_max>)
    Function too long (LoC/func): <func_too_long_num> (max=<func_too_long_max>)
    Duplicate code:               <duplicate_code>
 
  Obsolete code:
    Unused imports:             <unused_imports>
    Unused variables:           <unused_variables>
    Unused arguments:           <unused_arguments>
    Unreachable code:           <unreachable_code>
--------------------------------------------------
"""
    return template


def _getReportTemplateHtml():
    template = """<html><body>
<div style='margin: 0 auto;'>
<div style='display: table; margin: 0 auto;'>
<h1>Code Quality Summary</h1>

<hr>
<h2>Pytest:</h2>
<table>
<tr><td>Test coverage:</td><td><coverage></td></tr>
</table>

<hr>
<h2>Pylint <span style='font-weight: normal; font-size: medium;'>(Score: <pylint_score>)</span></h2>

<table>
<tr><td>Missing docstrings:</td><td><missing_docstrings></td></tr>

<tr><td span=2>&nbsp;</td></tr>
<tr><td span=2><b>Needs Refactoring:</b></td></tr>
<tr><td style='padding: 0 10px;'>Too complex:</td><td><too_complex_num> (max=<too_complex_max>)</td></tr>
<tr><td style='padding: 0 10px;'>Function too long (LoC/func):</td><td><func_too_long_num> (max=<func_too_long_max>)</td></tr>
<tr><td style='padding: 0 10px;'>Duplicate code:</td><td><duplicate_code></td></tr>

<tr><td span=2>&nbsp;</td></tr>
<tr><td span=2><b>Obsolete code:</b></td></tr>
<tr><td style='padding: 0 10px;'>Unused imports:</td><td><unused_imports></td></tr>
<tr><td style='padding: 0 10px;'>Unused variables:</td><td><unused_variables></td></tr>
<tr><td style='padding: 0 10px;'>Unused arguments:</td><td><unused_arguments></td></tr>
<tr><td style='padding: 0 10px;'>Unreachable code:</td><td><unreachable_code></td></tr>
</table>         
<hr>
</div>
</body></html>"""
    return template
  
  
def getReportTemplate(type='txt'):
    if type.lower() == 'txt':
        template = _getReportTemplateTxt()
    elif type.lower() == 'html':
        template = _getReportTemplateHtml()
    return template


def summarizeCodeQuality():
    coverage = CoverageReport()
    pylint = PylintReport()
    report_txt = getReportTemplate(type='txt')
    report_txt = report_txt.replace('<coverage>', str(coverage.getTotalCoverage()))
    report_txt = report_txt.replace('<pylint_score>', str(pylint.getScore()))
    report_txt = report_txt.replace('<missing_docstrings>', str(pylint.getMissingDocstrings()))
    report_txt = report_txt.replace('<too_complex_num>', str(pylint.getTooComplex()[0]))
    report_txt = report_txt.replace('<too_complex_max>', str(pylint.getTooComplex()[1]))
    report_txt = report_txt.replace('<func_too_long_num>', str(pylint.getTooManyStatements()[0]))
    report_txt = report_txt.replace('<func_too_long_max>', str(pylint.getTooManyStatements()[1]))
    report_txt = report_txt.replace('<duplicate_code>', str(pylint.getDuplicateCode()))
    report_txt = report_txt.replace('<unused_imports>', str(pylint.getUnusedImports()))
    report_txt = report_txt.replace('<unused_variables>', str(pylint.getUnusedVariables()))
    report_txt = report_txt.replace('<unused_arguments>', str(pylint.getUnusedArguments()))
    report_txt = report_txt.replace('<unreachable_code>', str(pylint.getUnreachableCode()))
    print(report_txt)
    with open('code_quality_report.txt', 'w') as f:
        f.write(report_txt)
    
    report_html = getReportTemplate(type='html')
    report_html = report_html.replace('<coverage>', str(coverage.getTotalCoverage()))
    report_html = report_html.replace('<pylint_score>', str(pylint.getScore()))
    report_html = report_html.replace('<missing_docstrings>', str(pylint.getMissingDocstrings()))
    report_html = report_html.replace('<too_complex_num>', str(pylint.getTooComplex()[0]))
    report_html = report_html.replace('<too_complex_max>', str(pylint.getTooComplex()[1]))
    report_html = report_html.replace('<func_too_long_num>', str(pylint.getTooManyStatements()[0]))
    report_html = report_html.replace('<func_too_long_max>', str(pylint.getTooManyStatements()[1]))
    report_html = report_html.replace('<duplicate_code>', str(pylint.getDuplicateCode()))
    report_html = report_html.replace('<unused_imports>', str(pylint.getUnusedImports()))
    report_html = report_html.replace('<unused_variables>', str(pylint.getUnusedVariables()))
    report_html = report_html.replace('<unused_arguments>', str(pylint.getUnusedArguments()))
    report_html = report_html.replace('<unreachable_code>', str(pylint.getUnreachableCode()))
    with open('code_quality_report.html', 'w') as f:
        f.write(report_html)


def main():
    package_name = os.path.relpath(sys.argv[1])
    runPytest(package_name)
    runPylint(package_name)
    # runFlake8(package_name)
    summarizeCodeQuality()
    
if __name__ == '__main__':
    main()
    
