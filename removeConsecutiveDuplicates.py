#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:57:59 2022

@author: swapnilbrahmankar
"""

string = 'xxxyyyzwwzzz'

def removeConsecutiveDuplicates(string): 
    l = len(string)
    
    if(l == 0 or l == 1):
        return string

    if(string[0] == string[1]):
        return removeConsecutiveDuplicates(string[0] + string[2:])
    else:
        return string[0] + removeConsecutiveDuplicates(string[1:])
        
print(removeConsecutiveDuplicates(string))
