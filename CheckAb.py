#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 20:32:12 2022

@author: swapnilbrahmankar
"""

string  = 'abababa'

def CheckAb (string):
    if(len(string) == 0):
        return True
    
    if(string[0] =='a' and len(string) ==1):
        return True
    elif(string[0] =='a' and string[1] =='a' and len(string)>=2):
        return CheckAb(string[1:])
    elif(string[0] =='a' and string[1:3] =='bb' and len(string)>=3):
        return CheckAb(string[3:])
    
    return False

if(CheckAb(string)):
    print('true')
else:
    print('false')    