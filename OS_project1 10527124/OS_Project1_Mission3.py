# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:54:07 2019

@author: User
"""

def bubble_sort(content):
    for i in range(0,len(content)-1): #有n-1回合(n為數字個數)
        for j in range(0,len(content)-1-i): #每回合進行比較的範圍
            if content[j] > content[j+1]: #是否需交換
                tmp = content[j]
                content[j] = content[j+1]
                content[j+1] = tmp

def mergeSort(content): 
    if len(content) > 1: 
        mid = len(content) // 2 #Finding the mid of the array 
        L = content[:mid] # Dividing the array elements  
        R = content[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                content[k] = L[i] 
                i=i+1
            else: 
                content[k] = R[j] 
                j=j+1
            k=k+1
          
        # Checking if any element was left 
        while i < len(L): 
            content[k] = L[i] 
            i=i+1
            k=k+1
          
        while j < len(R): 
            content[k] = R[j] 
            j=j+1
            k=k+1
