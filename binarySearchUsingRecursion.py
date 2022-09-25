#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:37:01 2022

@author: swapnilbrahmankar
"""

arr = [1, 4, 7, 8, 9, 11, 32, 55]

def binarySearchUsingRecursion (arr, x, s, e):
    if (s > e):
        return -1
    
    m = (s+e)//2
    # print(m, s, e, arr[m])
    if (arr[m] == x):
        return m
    elif (arr[m] > x):
        # print('upper')
        return binarySearchUsingRecursion (arr, x, s, m-1)
    else:
        return binarySearchUsingRecursion (arr, x, m+1, e)

print(binarySearchUsingRecursion(arr, 32, 0, len(arr)))