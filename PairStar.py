#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:22:00 2022

@author: swapnilbrahmankar
"""

string = 'helllo'

def PairStar (string):
    if(len(string) == 0 or len(string) == 1):
        return string
    
    if (string[0] == string[1]):
        return string[0] + '*' + PairStar(string[1:])
    else:
        return string[0] + PairStar(string[1:])
    

print(PairStar(string))