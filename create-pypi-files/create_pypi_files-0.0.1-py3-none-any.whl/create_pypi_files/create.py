#!/usr/bin/python

import os
'''
    *os* and *os.path* modules include many functions to interact with the file system.
'''
import shutil

def create():

    application = input("The name of application: ")
    cwd = os.getcwd()
    os.mkdir(cwd+'/'+application)

create()
