#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:37:35 2022

@author: swapnilbrahmankar
"""

n = 1000

def CountZeros (n):
    if (n == 0):
        return 1
    elif (n //10 == 0 and n > 0):
        return 0
    
    if (n % 10 == 0):
        return 1 + CountZeros(n //10)
    
    return CountZeros(n //10)

print(CountZeros(n))