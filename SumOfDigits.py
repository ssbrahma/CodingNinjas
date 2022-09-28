#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:04:26 2022

@author: swapnilbrahmankar
"""
n = 12345

def SumOfDigits (n):
    
    if n // 10 == 0:
        return n % 10
    
    return n%10 + SumOfDigits (n//10)

print(SumOfDigits(n))