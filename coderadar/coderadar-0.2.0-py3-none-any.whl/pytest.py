'''Module for PyTest functionality.'''

import subprocess
import tempfile

    
def runPytest(package_name):
    print('Running PyTest...')
    
    cmd = ['python',
           '-m',
           'pytest',
           '--cov=%s' % package_name,
           '--cov-report=term',
           '--cov-report=xml',
           '--cov-branch',
           '--cov-config=%s/tests/.coveragerc' % package_name,
           '%s/tests/' % package_name
           ]
    print(' '.join(cmd))
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(cmd,
                                stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output = str(tempf.read().decode())
        
    print(output)
    with open('coverage.txt', 'w') as f:
        f.writelines(output)
        

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