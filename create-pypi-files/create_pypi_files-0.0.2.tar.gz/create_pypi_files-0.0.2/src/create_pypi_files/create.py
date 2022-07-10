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
    
    os.mkdir(os.getcwd()+'/'+'src')
    print(cwd)
    #os.chdir(cwd)
    cwd_1 = os.mkdir(cwd+'/'+application)
    os.chdir(cwd_1)

create()
