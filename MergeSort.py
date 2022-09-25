#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:55:46 2022

@author: swapnilbrahmankar
"""

arr = [2, 39, 32, 23 , 21, 33, 12]

def merge (sub_arr1, sub_arr2, arr):
    
    l = 0
    m = 0
    k = 0
    
    while (l < len(sub_arr1) and m < len(sub_arr2)):
        if(sub_arr1[l] < sub_arr2[m]):
            arr[k] = sub_arr1[l]
            l += 1
            k += 1
        else:
            arr[k] = sub_arr2[m]
            m += 1
            k += 1
    
    while (l < len(sub_arr1)):
        arr[k] = sub_arr1[l]
        l += 1
        k += 1
        
    while (m < len(sub_arr2)):
        arr[k] = sub_arr2[m]
        m += 1
        k += 1
            

def mergeSort (arr, start, end):
    
    if(len(arr) == 0 or len(arr) == 1):
        return 
    
    m = (start+end)//2
    
    sub_arr1 = arr[0:m]
    sub_arr2 = arr[m:]
    # print(sub_arr1, sub_arr2, start, m, end)
    
    mergeSort(sub_arr1, 0, m)
    mergeSort(sub_arr2, m, len(arr))
    
    merge (sub_arr1, sub_arr2, arr)
    
mergeSort(arr,0, len(arr))

print(arr)