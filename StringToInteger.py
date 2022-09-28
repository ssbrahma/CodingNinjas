#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:57:18 2022

@author: swapnilbrahmankar
"""

string = '12567'

def StringToInteger(string):
    if (len(string) == 0):
        return 0
    
    # num = int(string[-1]) * 10
    # print(num)
    return int(string[-1]) + StringToInteger(string[:-1]) * 10
        
    
print(StringToInteger(string))
    
    