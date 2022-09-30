#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:48:57 2022

@author: swapnilbrahmankar
"""

n = 2

def towerofhanoi(n, source, aux, dest):
    if (n == 0):
        return
    if (n == 1):
        print (source + ' ' + dest)
        return
    towerofhanoi(n - 1, source, dest, aux)
    print (source + ' ' + dest)
    towerofhanoi(n - 1, aux, source, dest)
    
towerofhanoi(n, 'a', 'b', 'c')
    