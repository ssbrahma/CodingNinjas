#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:42:39 2022

@author: swapnilbrahmankar
"""

n = 4

def Staircase (n):
    
    if (n < 0):
        return 0
    if (n == 0):
        return 1
    
    x = Staircase(n-1)
    y = Staircase(n-2)
    z = Staircase(n-3)
    
    # print(x, y, z)
    return x + y + z

print(Staircase(n))