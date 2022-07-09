'''Module containing PyLint functionality.'''

import sys
import subprocess
import tempfile
import json

    
def _runPylintPy2(package_name):
    # pylint -ry --load-plugins=pylint.extensions.mccabe --output-format=json:pylint.json,text:pylint.txt --ignore tests ./testing_gitlab/
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(['pylint', 
                                 '-ry',
                                 '--load-plugins=pylint.extensions.mccabe',
                                 '--output-format=json',
                                 '--ignore=tests',
                                 '--persistent=n',
                                 './%s/' % package_name
                                 ],
                                 stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output = str(tempf.read().decode())
        with open('pylint.json', 'w') as f:
            f.write(output)
    
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(['pylint', 
                                 '-ry',
                                 '--load-plugins=pylint.extensions.mccabe',
                                 '--output-format=text',
                                 '--ignore=tests',
                                 '--persistent=n',
                                 './%s/' % package_name
                                 ],
                                 stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output = str(tempf.read().decode())
        with open('pylint.txt', 'w') as f:
            f.write(output)
        print(output)
    
    
def _runPylintPy3(package_name):
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
    
    
def runPylint(package_name):
    print('Running PyLint...')
    if sys.version_info.major == 2:
        _runPylintPy2(package_name)
    else:
        _runPylintPy3(package_name)
    
    
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
        if sys.version_info.major == 2:
            no_docstring   = 'C0111'
            msg_ids = [no_docstring]
        else:
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
    
