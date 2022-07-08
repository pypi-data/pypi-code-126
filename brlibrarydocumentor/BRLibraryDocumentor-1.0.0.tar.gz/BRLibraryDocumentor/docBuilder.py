import argparse
import os
from pathlib import Path
from os import makedirs, path, listdir

from functionblock import ASLibraryDataType, ASLibraryFunction, ASLibrary, BlockSection
from jinja2 import Environment, FileSystemLoader

def BuildFunctionBlockPage(funct : ASLibraryFunction) -> None:
    if os.path.exists('./Output/') == False:
        os.mkdir('./Output/')
    if(os.path.exists('./Output/{0}.html'.format(funct._name))):
        os.remove('./Output/{0}.html'.format(funct._name))

    with open('./Output/{0}.html'.format(funct._name),"w") as f:
        file_loader = FileSystemLoader("./src/Templates/")
        env = Environment(loader = file_loader)

        template = env.get_template("functionBlockPage.html")
        output = template.render(functionBlock = funct)
        f.write(output)

# Output all of the datatype files from the library's typ file(s)
def BuildTypePage(typ : ASLibraryDataType) -> None:
    if os.path.exists('./Output/DataTypes') == False:
        os.mkdir('./Output/DataTypes')
    
    if(os.path.exists('./Output/DataTypes/{0}.html'.format(typ._name))):
        os.remove('./Output/DataTypes/{0}.html'.format(typ._name))
    
    with open('./Output/DataTypes/{0}.html'.format(typ._name),"w") as f:
        file_loader = FileSystemLoader("./src/Templates/")
        env = Environment(loader = file_loader)

        template = env.get_template("libDatatypePage.html")
        output = template.render(datatype = typ)
        f.write(output)


# Output all of the datatype files from the library's typ file(s)
def BuildEnumPage(typ : ASLibraryDataType) -> None:
    if os.path.exists('./Output/DataTypes') == False:
        os.mkdir('./Output/DataTypes')
    
    if(os.path.exists('./Output/DataTypes/{0}.html'.format(typ._name))):
        os.remove('./Output/DataTypes/{0}.html'.format(typ._name))
    
    with open('./Output/DataTypes/{0}.html'.format(typ._name),"w") as f:
        file_loader = FileSystemLoader("./src/Templates/")
        env = Environment(loader = file_loader)

        template = env.get_template("libEnumPage.html")
        output = template.render(datatype = typ)
        f.write(output)


#Main classes if you're trying to call the script standalone
def main() -> None:
    parser = argparse.ArgumentParser()
    # parser.add_argument('-f', '--fun', help='Function File Path', dest='funFilePath', required=True)
    # parser.add_argument('-t', '--type', help='Type File Path', dest='typFilePath', required=True)
    parser.add_argument('-p', '--path', help='Library File Path', dest='libraryFilePath', required=True)
    args = parser.parse_args()
    itm = []
    for f in os.listdir(os.path.join(args.libraryFilePath)):
        suf = Path(f).suffix
        if suf == '.typ' or suf == '.var' or suf == '.fun':
            itm.append(os.path.join(args.libraryFilePath,f))
    
    #Currently only supports 1 type,fun and var file!!
    funFileContents = ''
    typFileContents = ''
    for i in itm:
        if i.endswith('.typ'):
            with open(i) as file:
                typFileContents = file.read()
        if i.endswith('.fun'):
            with open(i) as file:
                funFileContents = file.read()
    lib = ASLibrary(funFileContents,typFileContents)
    for funct in lib._functions:
        BuildFunctionBlockPage(funct)
    for typ in lib._datatypes:
        BuildTypePage(typ)
    for enum in lib._enums:
        BuildEnumPage(enum)  
                

if __name__ == '__main__':
    main()
