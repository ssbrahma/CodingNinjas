#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:11:30 2022

@author: swapnilbrahmankar
"""

m = 3
n = -5

def Multiplication(m, n):
    if (m == 0 or n == 0):
        return 0
    
    if (n < 0):
        return -(m - Multiplication(m, n+1))
    else:
        return m + Multiplication(m, n-1)
    
print(Multiplication(m, n))