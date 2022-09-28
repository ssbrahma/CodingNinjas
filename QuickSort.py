#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 09:43:28 2022

@author: swapnilbrahmankar
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:55:46 2022

@author: swapnilbrahmankar
"""

arr = [2, 39, 32, 23 , 21, 33, 12]

def partition (arr):
    
    i = 1
    ele = arr[0]
    replace = 0
   
    while (i < len(arr)-1):
        if (ele > arr[i]):
            replace += 1
        i += 1
    
    arr[replace], arr[0] = arr[0], arr[replace]
    
    print(arr)

            

def quickSort (arr, start, end):
    
    if(len(arr) == 0 or len(arr) == 1):
        return 
    
    m = (start+end)//2
    
    sub_arr1 = arr[0:m]
    sub_arr2 = arr[m:]
    # print(sub_arr1, sub_arr2, start, m, end)
    
    partition (sub_arr1, sub_arr2, arr)
    
    quickSort(sub_arr1, 0, m)
    quickSort(sub_arr2, m, len(arr))
   
quickSort(arr,0, len(arr))

print(arr)