#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:36:49 2022

@author: swapnilbrahmankar
"""

n = 4

def GeometricSum (n):
    if n == 0:
        return 1
    
    return 1/(2**n) + GeometricSum(n-1)

print(format(GeometricSum(n), '.5f'))