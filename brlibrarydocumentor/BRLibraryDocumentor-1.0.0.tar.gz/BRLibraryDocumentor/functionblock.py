from enum import Enum
from typing import Optional
import re
import argparse
from unicodedata import name

class BlockSection(Enum):
    Parameter = 0
    Cyclic = 1
    Command = 2
    Optional = 3
    Omit = 4

class VariableScope(Enum):
    Input = 0
    Output = 1
    Internal = 2
    Input_Output = 3

class FunctionType(Enum):
    Function = 0
    FunctionBlock = 1

class FunctionBlock():
    def __init__(self) -> None:
        self.Inputs = []
        self.Outputs = []
        self.Title = ""

class FunctionVariable():
    def __init__(self,name,type,comments,value='') -> None:
        self._name = name
        self._type = type
        self._value = value
        self._comments = comments
        if(len(self._comments) == 3):
            self._blockType = self._parseComment3(self._comments[2])
        else:
            self._blockType = BlockSection.Parameter

    # parse the 3rd comment for the flags to be used for creating the faceplate (if present)
    def _parseComment3(self,comment3) -> BlockSection:
        if(comment3.find("#PAR") > -1):
            return BlockSection.Parameter
        elif (comment3.find("#CYC") > -1):
            return BlockSection.Cyclic
        elif (comment3.find("#CMD") > -1):
            return BlockSection.Command
        elif (comment3.find("#OPT") > -1):
            return BlockSection.Optional
        elif (comment3.find("#OMIT") > -1):
            return BlockSection.Omit
        else:
            return BlockSection.Parameter

class ASLibraryEnum():
    def __init__(self,enumTypeText) -> None:
        self._comments = []
        for nm in re.finditer(r'\s*([\w\d_]+)\s*:\s*\n*\s*\(\s*\(\*(.*)\*\)\s*\n*((\s*([\w\d_]+)(\s*:=\s*(-?[\w\d_]+))?,?\s*\(\*(.*)\*\)\s*\n*)+)\);',enumTypeText):
           self._name = nm.group(1)
           self._comments.append(nm.group(2))
           self._typeMembers = self.__parseMember(nm.group(3))

    def __parseMember(self, dataTypeText):
        varList = []
        tmp = dataTypeText.splitlines()
        regex = re.compile(r'\s*([\w\d_]+)(\s*:=\s*(-?[\w\d_]+))?,?\s*\(\*(.*)\*\)\s*\n*')
        value = 0
        #print(tmp)
        for var in [regex.match(line) for line in tmp if (regex.match(line) is not None)]:
            if (var.group(3) != None):
                value = int(var.group(3))
            varList.append(FunctionVariable(var.group(1), '', var.group(4), value))
            value = value + 1
        return varList

class ASLibraryDataType():
    def __init__(self, dataTypeText) -> None:
        
        for nm in re.finditer(r'\s*(.*?)\sSTRUCT',dataTypeText):
            self._name = nm.group(1).replace(':','').replace(' ','')
        
        self._comments = []
        ##TODO: not certain the regex here is correct
        for match in re.finditer(r'STRUCT\s*\(\*(.*?)\*\)+',dataTypeText):
            self._comments.append(match.group(1))
                    
        self._typeMembers = self.__parseMember(dataTypeText)

    def __parseMember(self,dataTypeText):
        varList = []
        tmp = dataTypeText.splitlines()
        
        for line in tmp:
            Comments = []
            #Get the comments
            if re.match(r'\s*(.*)\s:\s(.*);\s(\S*?)(\s*\(\*.*?\*\))+',line) is not None:
                match = re.match(r'\s*(.*)\s:\s(.*);\s(\S*?)(\s*\(\*.*?\*\))+',line)
                for comments in re.finditer(r'\s*\(\*(.*?)\*\)',match.group()):
                    Comments.append(comments.group(1))
            #Get the variable name + type
            var = re.match(r'\s*(.*)\s:\s(.*);\s',line)
            if var is not None:
                if len(Comments) == 0:
                    Comments.append('')
                varList.append(FunctionVariable(var.group(1),var.group(2),Comments))
        return varList
        
class ASLibraryFunction():
    def __init__(self, functionText) -> None:
        self.Comments = []
        self.Inputs = []
        self.Outputs = []
        self.Internals = []

        for fcn in re.finditer(r'(?:FUNCTION)(.|\n)*?END_FUNCTION',functionText):
            #Determine if a function or a function block
            if re.match(r'FUNCTION_BLOCK',fcn.group()):
                self._type = FunctionType.FunctionBlock
            else:
                self._type = FunctionType.Function
            #Check to see if there are comments
            if re.match(r'FUNCTION_BLOCK\s*(\S*?)(\s*\(\*.*?\*\))+',fcn.group()) is not None:
                match = re.match(r'FUNCTION_BLOCK\s*(\S*?)(\s*\(\*.*?\*\))+',fcn.group())
                for comments in re.finditer(r'\s*\(\*(.*?)\*\)',match.group()):
                    self.Comments.append(comments.group(1))
            if len(self.Comments) == 0:
                self.Comments.append("")
            #get the name of the Function or function block
            if self._type is FunctionType.FunctionBlock:
                for tst in re.finditer(r'FUNCTION_BLOCK\s*(.*?)\s',fcn.group()):
                    self._name = tst.group(1)
            else:
                for tst in re.finditer(r'FUNCTION\s*(.*?)\s',fcn.group()):
                    self._name = tst.group(1)
                
            for fcnInputs in re.finditer(r'(?:VAR_INPUT)(.|\n)*?(END_VAR)',fcn.group()):
                self.Inputs = self.Inputs + self._parseVar(fcnInputs.group())
            for fcnOutputs in re.finditer(r'(?:VAR_OUTPUT)(.|\n)*?(END_VAR)',fcn.group()):
                self.Outputs = self.Outputs + self._parseVar(fcnOutputs.group())
            for fcnInternals in re.finditer(r'(?:VAR)(.|\n)*?(END_VAR)',fcn.group()):
                self.Internals = self.Internals + self._parseVar(fcnInternals.group())


    def _parseVar(self,varBlock):
        varList = []
        tmp = varBlock.splitlines()
        
        for line in tmp:
            Comments = []
            #Get the comments
            if re.match(r'\s*(.*)\s:\s(.*);\s(\S*?)(\s*\(\*.*?\*\))+',line) is not None:
                match = re.match(r'\s*(.*)\s:\s(.*);\s(\S*?)(\s*\(\*.*?\*\))+',line)
                for comments in re.finditer(r'\s*\(\*(.*?)\*\)',match.group()):
                    Comments.append(comments.group(1))
            #Get the variable name + type
            var = re.match(r'\s*(.*)\s:\s(.*);\s',line)
            if var is not None:
                if len(Comments) == 0:
                    Comments.append('')
                varList.append(FunctionVariable(var.group(1),var.group(2),Comments))
        return varList

class ASLibrary():
    def __init__(self,name,functionFileContents,typeFileContents) -> None:
        self.Name = name
        self._functions = {}
        self._datatypes = []
        self._enums = []
        #Get all the types from the File
        for fcn in re.finditer(r'(?:FUNCTION)(.|\n)*?END_FUNCTION',functionFileContents):
            tmp = ASLibraryFunction(fcn.group())
            self._functions[tmp._name] = tmp
        
        for typ in re.finditer(r'\s*(.*?)\s(?:STRUCT)(.|\n)*?END_STRUCT',typeFileContents):
            self._datatypes.append(ASLibraryDataType(typ.group()))

        for enum in re.finditer(r'\s*([\w\d_]+)\s*:\s*\n*\s*\(\s*\(\*(.*)\*\)\s*\n*(\s*([\w\d_]+)(\s*:=\s*(-?[\w\d_]+))?,?\s*\(\*(.*)\*\)\s*\n*)+\);',typeFileContents):
            self._enums.append(ASLibraryEnum(enum.group()))

    # Should pass in the path to the Library root directory
        # The important files will be 
        #   any .type files - defines the library types
        #   any .var files - defines the library constants
        #   any .fun files (i'm not sure if you can actually have more than 1 .fun file in a project)

    # How should one mix automatically generated and manually built content??

#Main classes if you're trying to call the script standalone
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fun', help='Function File Path', dest='funFilePath', required=True)
    parser.add_argument('-t', '--type', help='Type File Path', dest='typFilePath', required=True)
    args = parser.parse_args()
    funFileContents = ''
    typFileContents = ''
    with open(args.funFilePath) as file:
        funFileContents = file.read()
    with open(args.typFilePath) as file:
        typFileContents = file.read()
    
    lib = ASLibrary(funFileContents, typFileContents)

if __name__ == '__main__':
    main()
