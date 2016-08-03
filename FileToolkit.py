# -*- coding: utf-8 -*-
"""
A small tool for operating file and dir. 
Created on Wed Aug  3 11:24:02 2016
@author: chen bin 
"""

import os 
import time
import re

def Get_Unique_Filename_Without_Extend(path):
    '''
    input: dir path which contain the file you want to operate
    output:a set of file name with out extend 
    '''

    file_list=os.listdir(path)
    fileset=set()
    for file in file_list:
        filepath=os.path.join(path,file)
        if os.path.isfile(filepath):
            dir_file=os.path.split(filepath)
            file_ext=os.path.splitext(dir_file[1])
            fileset.add(file_ext[0])
    return fileset

def Get_Unique_Filename_With_Extend(path):
    '''
    input: dir path which contain the file you want to operate
    output:a set of file name with out extend 
    '''

    file_list=os.listdir(path)
    fileset=set()
    for file in file_list:
        filepath=os.path.join(path,file)
        if os.path.isfile(filepath):
            dir_file=os.path.split(filepath)
            fileset.add(dir_file[1])
    return fileset