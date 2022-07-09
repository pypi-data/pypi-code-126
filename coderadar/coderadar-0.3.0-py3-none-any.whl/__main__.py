'''Module to run Code Radar.'''

import sys
import os

from .pylint import runPylint, PylintReport
from .pytest import runPytest, CoverageReport
from .flake8 import runFlake8
from .gitlab import Gitlab
  
def _getReportTemplateTxt():
    template = """
Code Quality Report
<package_name>
--------------------------------------------------
Pytest:
  Test coverage: <coverage>
 
--------------------------------------------------
Pylint Score:  <pylint_score>/10
  Missing docstrings:             <missing_docstrings>
 
  Needs Refactoring:
    Too complex:                  <too_complex_num> (max cyclomatic complexity=<too_complex_max>)
                                    <too_complex_file>: <too_complex_obj> (line <too_complex_line>)
    Function too long (LoC/func): <func_too_long_num> (max LoC/func=<func_too_long_max>)
                                    <func_too_long_file>: <func_too_long_obj> (line <func_too_long_line>)
    Duplicate code:               <duplicate_code> block(s)
                                    <duplicate_code_lines> lines in <duplicate_code_num> modules:
                                    <duplicate_code_files>
 
  Obsolete code:
    Unused imports:             <unused_imports>
                                  <unused_imports_file>
                                  <unused_imports_num> imports: <unused_imports_items>
    Unused variables:           <unused_variables>
                                  <unused_variables_file>
                                  <unused_variables_num> variables: <unused_variables_items>
    Unused arguments:           <unused_arguments>
                                  <unused_arguments_file>
                                  <unused_arguments_num> arguments: <unused_arguments_items>
    Unreachable code:           <unreachable_code>
                                  <unreachable_code_file>
                                  <unreachable_code_num> block(s): <unreachable_code_items>
--------------------------------------------------
"""
    return template


def _getReportTemplateHtml():
    template = """<html><body>
<head>
<style>
    td {vertical-align: top;}
    td:first-child {white-space: nowrap;}
    div.details {font-size: 90%; color: #666; margin-left:10px;}
    em.code {font-style:normal; font-family: monospace, monospace;}
    .logo {font-size:small; color:#BBB; font-style:italic;font-family:sans-serif; text-decoration: none;}
    a.logo {font-variant: small-caps;}
    a.logo:hover {color: #B33; text-decoration: underline;}
</style>
</head>
<div style='margin: 0 auto; width: 900px;'>
<div style='display: table; margin: 0 auto;'>
<h1>Code Quality Report</h1>
<package_name>
<hr>
<h2>Pytest <span style='font-weight: normal; font-size: medium;'>(<a href='<pytest_report_url>'>Report</a>)</span></h2>
<table>
<tr><td>Test coverage:</td><td><coverage></td></tr>
</table>

<hr>
<h2>Pylint <span style='font-weight: normal; font-size: medium;'>(Score: <pylint_score>/10; <a href='<pylint_report_url>'>Report</a>)</span></h2>

<table>
<tr><td>Missing docstrings:</td><td><missing_docstrings></td></tr>

<tr><td span=2>&nbsp;</td></tr>
<tr><td span=2><b>Needs Refactoring:</b></td></tr>
<tr><td style='padding: 0 10px;'>Too complex:</td><td><too_complex_num> (max cyclomatic complexity=<too_complex_max>)<br/>
  <div class='details'><em class='code'><too_complex_file></em>: <em class='code'><too_complex_obj></em> (line <too_complex_line>)</div></td></tr>
<tr><td style='padding: 0 10px;'>Function too long (LoC/func):</td><td><func_too_long_num> (max LoC/func=<func_too_long_max>)<br/>
  <div class='details'><em class='code'><func_too_long_file></em>: <em class='code'><func_too_long_obj></em> (line <func_too_long_line>)</div></td></tr>
<tr><td style='padding: 0 10px;'>Duplicate code:</td><td><duplicate_code> block(s)<br/>
  <div class='details'><duplicate_code_lines> lines in <duplicate_code_num> modules:<br/><em class='code'><duplicate_code_files></em></div></td></tr>

<tr><td span=2>&nbsp;</td></tr>
<tr><td span=2><b>Obsolete code:</b></td></tr>
<tr><td style='padding: 0 10px;'>Unused imports:</td><td><unused_imports><br/>
  <div class='details'><em class='code'><unused_imports_file></em><br/><unused_imports_num> import(s): <em style='code'><unused_imports_items></em></div></td></tr>
<tr><td style='padding: 0 10px;'>Unused variables:</td><td><unused_variables><br/>
  <div class='details'><em class='code'><unused_variables_file></em><br/><unused_variables_num> variable(s): <em style='code'><unused_variables_items></em></div></td></tr>
<tr><td style='padding: 0 10px;'>Unused arguments:</td><td><unused_arguments><br/>
  <div class='details'><em class='code'><unused_arguments_file></em><br/><unused_arguments_num> arguments(s): <em style='code'><unused_arguments_items></em></div></td></tr>
<tr><td style='padding: 0 10px;'>Unreachable code:</td><td><unreachable_code>
  <div class='details'><em class='code'><unreachable_code_file></em><br/><unreachable_code_num> block(s): <em style='code'><unreachable_code_items></em></div></td></tr>
</table>         
<hr>
<span style='float:right;' class='logo'>generated with <a href='https://gitlab.com/ck2go/coderadar' class='logo'>CodeRadar</a></span>
</div>
</body></html>"""
    return template
  
  
def getReportTemplate(type='txt'):
    if type.lower() == 'txt':
        template = _getReportTemplateTxt()
    elif type.lower() == 'html':
        template = _getReportTemplateHtml()
    return template

def _fillTemplate(report, package_name, coverage, pylint):
    report = report.replace('<package_name>', str(package_name))
    report = report.replace('<pytest_report_url>', str(coverage.getTxtUrl()))
    report = report.replace('<coverage>', str(coverage.getTotalCoverage()))
    report = report.replace('<pylint_score>', str(pylint.getScore()))
    report = report.replace('<pylint_report_url>', str(pylint.getTxtUrl()))
    report = report.replace('<missing_docstrings>', str(pylint.getMissingDocstrings()))
    report = report.replace('<too_complex_num>', str(pylint.getTooComplex()[0]))
    report = report.replace('<too_complex_max>', str(pylint.getTooComplex()[1]))
    report = report.replace('<too_complex_file>', str(pylint.getTooComplex()[2]))
    report = report.replace('<too_complex_obj>', str(pylint.getTooComplex()[3]))
    report = report.replace('<too_complex_line>', str(pylint.getTooComplex()[4]))
    report = report.replace('<func_too_long_num>', str(pylint.getTooManyStatements()[0]))
    report = report.replace('<func_too_long_max>', str(pylint.getTooManyStatements()[1]))
    report = report.replace('<func_too_long_file>', str(pylint.getTooManyStatements()[2]))
    report = report.replace('<func_too_long_obj>', str(pylint.getTooManyStatements()[3]))
    report = report.replace('<func_too_long_line>', str(pylint.getTooManyStatements()[4]))
    report = report.replace('<duplicate_code>', str(pylint.getDuplicateCode()[0]))
    report = report.replace('<duplicate_code_num>', str(pylint.getDuplicateCode()[1]))
    report = report.replace('<duplicate_code_files>', ', '.join(pylint.getDuplicateCode()[2]))
    report = report.replace('<duplicate_code_lines>', str(pylint.getDuplicateCode()[3]))
    report = report.replace('<unused_imports>', str(pylint.getUnusedImports()[0]))
    report = report.replace('<unused_imports_file>', str(pylint.getUnusedImports()[1]))
    report = report.replace('<unused_imports_num>', str(pylint.getUnusedImports()[2]))
    report = report.replace('<unused_imports_items>', ', '.join(pylint.getUnusedImports()[3]))
    report = report.replace('<unused_variables>', str(pylint.getUnusedVariables()[0]))
    report = report.replace('<unused_variables_file>', str(pylint.getUnusedVariables()[1]))
    report = report.replace('<unused_variables_num>', str(pylint.getUnusedVariables()[2]))
    report = report.replace('<unused_variables_items>', ', '.join(pylint.getUnusedVariables()[3]))
    report = report.replace('<unused_arguments>', str(pylint.getUnusedArguments()[0]))
    report = report.replace('<unused_arguments_file>', str(pylint.getUnusedArguments()[1]))
    report = report.replace('<unused_arguments_num>', str(pylint.getUnusedArguments()[2]))
    report = report.replace('<unused_arguments_items>', ', '.join(pylint.getUnusedArguments()[3]))
    report = report.replace('<unreachable_code>', str(pylint.getUnreachableCode()[0]))
    report = report.replace('<unreachable_code_file>', str(pylint.getUnreachableCode()[1]))
    report = report.replace('<unreachable_code_num>', str(pylint.getUnreachableCode()[2]))
    report = report.replace('<unreachable_code_items>', ', '.join(pylint.getUnreachableCode()[3]))
    return report


def summarizeCodeQuality(package_name):
    coverage = CoverageReport()
    pylint = PylintReport()
    report_txt = getReportTemplate(type='txt')
    report_txt = _fillTemplate(report_txt, package_name, coverage, pylint)
    print(report_txt)
    with open('code_quality_report.txt', 'w') as f:
        f.write(report_txt)
    
    report_html = getReportTemplate(type='html')
    report_html = _fillTemplate(report_html, package_name, coverage, pylint)
    with open('code_quality_report.html', 'w') as f:
        f.write(report_html)


def main():
    package_name = os.path.relpath(sys.argv[1])
    runPytest(package_name)
    runPylint(package_name)
    # runFlake8(package_name)
    summarizeCodeQuality(package_name)
    
if __name__ == '__main__':
    main()
    
