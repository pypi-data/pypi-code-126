'''Module to run Code Radar.'''

import sys
import os

from .pylint import runPylint, PylintReport
from .pytest import runPytest, CoverageReport
from .flake8 import runFlake8
from .gitlab import Gitlab
        

def summarizeCodeQuality():
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
        

def main():
    package_name = os.path.relpath(sys.argv[1])
    runPytest(package_name)
    runPylint(package_name)
    # runFlake8(package_name)
    summarizeCodeQuality()
    
if __name__ == '__main__':
    main()
    
