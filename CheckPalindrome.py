#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:48:53 2022

@author: swapnilbrahmankar
"""
string = 'ninin'

def CheckPalindrome(string):
    # print(string, len(string))
    if len(string) == 0 or len(string) == 1:
        return True
    
    if (string[0] != string[-1]):
        # print(string)
        return False
    
    return CheckPalindrome(string[1:-1]) 
    
if (CheckPalindrome(string)):
    print ('true')
else:
    print('false')    