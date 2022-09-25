#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:57:59 2022

@author: swapnilbrahmankar
"""

string = 'xaxb'

def removeX(string): 
    l = len(string)
    
    if(l == 0):
        return string
    print(string)
    if(string[0] == 'x'):
        return removeX(string[1:])
    else:
        return string[0] + removeX(string[1:])
        
print(removeX(string))