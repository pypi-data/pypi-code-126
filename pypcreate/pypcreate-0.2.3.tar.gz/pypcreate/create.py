import os
import argparse
from pypcreate.__init__ import __version__
from pypcreate.create_func import mkdir
from pypcreate.create_func import mkdir_from_yaml
from pypcreate.create_func import setpyp
from pypcreate.create_func import pyptemp
from pypcreate.create_func import inittemp

def test_parser():
    parser = argparse.ArgumentParser(description="opencood command")

    parser.add_argument("-V","--version",action='store_true',
                        help="Display version.",
                    )
    parser.add_argument('--mkdir', type=str,
                        default='None',
                        help="To create a directory with empty`__init__.py` and `README.md` ")

    parser.add_argument('--yamlmkdir', type=str,
                        default='None',
                        help="To create a directory from a yaml file ")

    parser.add_argument('--setpyp', action='store_true',
                        help="To create all empty setup files: 'setup.py', 'MANIFEST.in', environment.yml ")
    
    parser.add_argument('--pyptemp', action='store_true',
                        help="To download all setup files to current directory: 'setup.py', 'MANIFEST.in', environment.yml ")

    parser.add_argument('--inittemp', action='store_true',
                        help="To download '__init__.py' template ")
  
    opt = parser.parse_args()
    return opt

def main():
    opt = test_parser()

    if opt.version:
        print("pypcreate version:",__version__)

    if opt.mkdir != 'None':
        mkdir(opt.mkdir)
    
    if opt.yamlmkdir != 'None':
        mkdir_from_yaml(opt.yamlmkdir)
    
    if opt.setpyp:
        setpyp()
    
    if opt.pyptemp:
        pyptemp()

    if opt.inittemp:
        inittemp()
    
if __name__ == '__main__':
    main()
