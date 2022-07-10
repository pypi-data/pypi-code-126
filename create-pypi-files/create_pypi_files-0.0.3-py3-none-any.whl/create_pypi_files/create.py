#!/usr/bin/python

import os
'''
    *os* and *os.path* modules include many functions to interact with the file system.
'''
import shutil

def create():

    application = input("The name of application: ")
    cwd = os.getcwd()+'/'+application
    print(cwd)
    os.mkdir(cwd)
    os.chdir(cwd)

    os.system("touch LICENSE")
    os.system("touch README.md")
    os.system("touch pyproject.toml")
    
    cwd_1 = os.getcwd()+'/'+'src'
    print(cwd_1)
    os.mkdir(cwd_1)
    
    os.chdir(cwd_1)
    cwd_2 = os.getcwd()+'/'+application
    os.mkdir(cwd_2)
    
    os.chdir(cwd_2)
    os.system("touch __init__.py")
    os.system("touch main.py")

#create()
