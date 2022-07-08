'''Module to run Code Radar.'''

import sys
import os
import subprocess
import tempfile
import json

import pytest


class Gitlab():
    def __init__(self):
        archive = ''


class PylintReport():
    def __init__(self, txt=None, json=None):
        if txt is None:
            txt = 'pylint.txt'
        if json is None:
            json = 'pylint.json'
            
        self._txt = txt
        self._json = json
        self._report = self._loadJsonReport()
        
        
    def _loadJsonReport(self):
        return json.load(open(self._json))
        
        
    def getScore(self):
        with open(self._txt) as f:
            lines = f.readlines()
        
        for line in lines:
            if 'Your code has been rated' in line:
                score = line[line.find(' at ')+3:line.find('/')]
        return score
    
    
    def getMissingDocstrings(self):
        no_module_docstring   = 'C0114'
        no_class_docstring    = 'C0115'
        no_function_docstring = 'C0116'
        msg_ids = [no_module_docstring, no_class_docstring, no_function_docstring]
        
        no_docstrings = [msg for msg in self._report if msg['message-id'] in msg_ids]
        num_missing_docstrings = len(no_docstrings)
        return num_missing_docstrings
    
    
    def getTooComplex(self):
        too_complex = 'R1260'
        msg_ids = [too_complex]
        
        too_complex = [msg for msg in self._report if msg['message-id'] in msg_ids]
        num_too_complex = len(too_complex)
        if num_too_complex > 0:
            max_too_complex = max([int(msg['message'][msg['message'].rfind(' ')+1:]) for msg in too_complex])
        else:
            max_too_many_satements = 0
        return num_too_complex, max_too_complex
    
    
    def getTooManyStatements(self):
        too_many_satements = 'R0915'
        msg_ids = [too_many_satements]
        
        too_many_satements = [msg for msg in self._report if msg['message-id'] in msg_ids]
        num_too_many_satements = len(too_many_satements)
        if num_too_many_satements > 0:
            max_too_many_satements = max([int(msg['message'][msg['message'].rfind('(')+1:msg['message'].rfind('/')]) for msg in too_many_satements])
        else:
            max_too_many_satements = 0
        return num_too_many_satements, max_too_many_satements
    
    
    def getUnusedImports(self):
        unused_import = 'W0611'
        msg_ids = [unused_import]
        
        unused_import = [msg for msg in self._report if msg['message-id'] in msg_ids]
        num_unused_import = len(unused_import)
        return num_unused_import
    
    
    def getUnusedVariables(self):
        unused_variable = 'W0612'
        msg_ids = [unused_variable]
        
        unused_variables = [msg for msg in self._report if msg['message-id'] in msg_ids]
        num_unused_variables = len(unused_variables)
        return num_unused_variables
    
    
    def getUnusedArguments(self):
        unused_arguments = 'W0613'
        msg_ids = [unused_arguments]
        
        unused_arguments = [msg for msg in self._report if msg['message-id'] in msg_ids]
        num_unused_arguments = len(unused_arguments)
        return num_unused_arguments

    
    def getUnreachableCode(self):
        unreachable_code = 'W0101'
        msg_ids = [unreachable_code]
        
        unreachable_code = [msg for msg in self._report if msg['message-id'] in msg_ids]
        num_unreachable_code = len(unreachable_code)
        return num_unreachable_code

    
    def getDuplicateCode(self):
        duplicate_code = 'R0801'
        duplicate_code2 = 'RP0801'
        msg_ids = [duplicate_code, duplicate_code2]
        
        duplicate_code = [msg for msg in self._report if msg['message-id'] in msg_ids]
        num_duplicate_code = len(duplicate_code)
        return num_duplicate_code
        


class CoverageReport():
    def __init__(self, txt=None, xml=None):
        if txt is None:
            txt = 'coverage.txt'
        if xml is None:
            xml = 'coverage.xml'
            
        self._txt = txt 
        self._xml = xml 
        
        
    def getTotalCoverage(self):
        with open(self._txt) as f:
            lines = f.readlines()
            
        # find the correct line in the coverage report and extract the total coverage
        in_coverage = False
        for line in lines:
            if '-- coverage:' in line:
                in_coverage = True
            if line[:5] == 'TOTAL':
                coverage = line.split()[-1]
                break
        
        return coverage


def analyzeCoverage():
    print('Code Quality Summary')
    print('-'*50)
    
    report = CoverageReport()
    print('Pytest:')
    print('  Test coverage: %s' % report.getTotalCoverage())
    print(' ')
    print('-'*50)
    
    pylint = PylintReport()
    print('Pylint Score: %s/10' % pylint.getScore())
    print('  Missing docstrings:           %i' % pylint.getMissingDocstrings())
    print(' ')
    print('  Needs Refactoring:')
    print('    Too complex:                  %s (max=%i)' % pylint.getTooComplex())
    print('    Function too long (LoC/func): %s (max=%i)' % pylint.getTooManyStatements())
    print('    Duplicate code:               %s' % pylint.getDuplicateCode())
    print(' ')
    print('  Obsolete code:')
    print('    Unused imports:             %i' % pylint.getUnusedImports())
    print('    Unused variables:           %i' % pylint.getUnusedVariables())
    print('    Unused arguments:           %i' % pylint.getUnusedArguments())
    print('    Unreachable code:           %i' % pylint.getUnreachableCode())
    print('-'*50)
    
    
def runPytest(package_name):
    print('Running PyTest...')
    
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(['pytest', 
                                 '-p', 
                                 'no:warnings',
                                 '--cov=%s' % package_name,
                                 '--cov-report=term',
                                 '--cov-report=xml',
                                 '--cov-branch',
                                 '--cov-config=%s/tests/.coveragerc' % package_name
                                 ],
                                 stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output = str(tempf.read().decode())
        
    print(output)
    with open('coverage.txt', 'w') as f:
        f.writelines(output)
    
    
def runPylint(package_name):
    print('Running PyLint...')
    # pylint -ry --load-plugins=pylint.extensions.mccabe --output-format=json:pylint.json,text:pylint.txt --ignore tests ./testing_gitlab/
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(['pylint', 
                                 '-ry',
                                 '--load-plugins=pylint.extensions.mccabe',
                                 '--output-format=json:pylint.json,text:pylint.txt',
                                 '--ignore=tests',
                                 './%s/' % package_name
                                 ],
                                 stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output = str(tempf.read().decode())
    print(output)
        

def runFlake8(package_name):
    print('Running Flake8...')

def main():
    package_name = os.path.relpath(sys.argv[1])
    runPytest(package_name)
    runPylint(package_name)
    # runFlake8(package_name)
    analyzeCoverage()
    
if __name__ == '__main__':
    main()
    
