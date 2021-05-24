# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:50:23 2019

@author: 10527124 資訊三甲 邱正皓 OS作業系統 project1
"""

import threading
import time
import numpy as np
from numba import jit
#import OS_Project1_Mission3
import multiprocessing
#from multiprocessing import Pool  

filename = input("請輸入檔名:\n")
f = open( str(filename) + '.txt', 'r') #輸入數字以空格隔開
content = f.read() 
content = np.array(content.split(), np.int32) 

def chunkIt(content, k): # 切資料用
  avg = len(content) / float(k) #先算平均每筆多少資料
  out = []
  last = 0

  while last < len(content):
    out.append(content[int(last):int(last + avg)]) # 扣掉第零筆資料 剩下的等分切 存到out中再回傳
    last += avg

  return out

@jit
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

# 宣告     
tmp = []    
array = []
console = []
# ************************************************************** mission 1
            
if ( content[0] == 1 ) : 
    
    print('Mission 1 !!') 
    content = content[1:] # 去掉題目數字
    print('現在處理' + str(len(content)) + '筆資料!!\n')
    
    start = time.time()
    
    bubble_sort(content)
    console = content
    
    end = time.time()
    elapsed = end - start
    print ("Time taken: ", elapsed, " seconds.")
    
    fp = open('input_output.txt', 'w')
    for i in range(len(console)):
        fp.write( str(console[i]) + " " ) 
    fp.write( "\nTime taken: " + str(elapsed) + " seconds." ) 
    fp.close()
    
# ************************************************************** mission 2
    
elif ( content[0] == 2 ) : 

    print('Mission 2 !!') 
    
    content = content[1:] # 去掉題目數字
    print('現在處理' + str(len(content)) + '筆資料!!\n')
    k = input("請問您想切成幾筆資料?:\n")
    out = chunkIt(content, k)
    
    start = time.time()

    threads = []
    console = out[0] 
    for i in range(0,len(out)-1): #個別做 bubble
        threads.append(threading.Thread(target = bubble_sort(out[i]))) #每次多一個線程去跑
        threads[i].start()
    for i in range(0,len(out)-1):#利用迴圈join等待避免後面錯誤
        threads[i].join()
    for i in range(0,len(out)-2): 
        array = np.hstack((out[i],out[i + 1])) # 合併list到array準備做merge
        tmp = list(array)
        t = threading.Thread( target = mergeSort(tmp) ) #做merge
        t.start()
        if len(console) == 0 :
            console = np.hstack((console,tmp))
        else :
            console = np.hstack((console,array[int(len(tmp) / 2):]))
        console = list(console)
        t = threading.Thread( target = mergeSort(console) ) #做merge
        t.start()
    end = time.time()
    elapsed = end - start
    print ("Time taken: ", elapsed, " seconds.")
    
    fp = open('input_output.txt', 'w')
    for i in range(len(console)):
        fp.write( str(console[i]) + " " ) 
    fp.write( "\nTime taken: " + str(elapsed) + " seconds." ) 
    fp.close()
        
# ************************************************************** mission 3

elif ( content[0] == 3 ) :        

    print('Mission 3 !!') 
    
    content = content[1:] # 去掉題目數字
    print('現在處理' + str(len(content)) + '筆資料!!\n')
    k = input("請問您想切成幾筆資料?:\n")
    out = chunkIt(content, k)
    
    processes = []
    start = time.time()
    console = out[0]  
    #pool = Pool(len(out))
    for i in range(0,len(out)-1):
        #OS_Project1_Mission3.bubble_sort(out[i])
        processes.append(multiprocessing.Process(target = bubble_sort(out[i])))
        processes[i].start()
        #pool.map(bubble_sort(out[i]), len(out))  
    for i in range(0,len(out)-1): #利用迴圈join等待避免後面錯誤
        processes[i].join
    for i in range(0,len(out)-2): 
        array = np.hstack((out[i],out[i + 1])) # 合併list到array準備做merge
        tmp = list(array)
        #OS_Project1_Mission3.mergeSort(tmp) #做merge
        p = multiprocessing.Process(target = mergeSort(tmp))
        p.start()
        #pool.map(mergeSort(tmp), len(out)-1)  
        if len(console) == 0 :
            console = np.hstack((console,tmp))
        else :
            console = np.hstack((console,array[int(len(tmp) / 2):]))
        console = list(console)
        #OS_Project1_Mission3.mergeSort(console) #做merge
        p = multiprocessing.Process(target = mergeSort(console))
        p.start()
        #pool.map(mergeSort(console), len(console))  
    end = time.time()
    elapsed = end - start
    print ("Time taken: ", elapsed, " seconds.")
    
    fp = open('input_output.txt', 'w')
    for i in range(len(console)):
        fp.write( str(console[i]) + " " ) 
    fp.write( "\nTime taken: " + str(elapsed) + " seconds." ) 
    fp.close()

# ************************************************************** mission 4

elif ( content[0] == 4 ) : 

    print('Mission 4 !!') 
    
    content = content[1:] # 去掉題目數字
    print('現在處理' + str(len(content)) + '筆資料!!\n')
    k = input("請問您想切成幾筆資料?:\n")
    out = chunkIt(content, k)
    
    start = time.time()
    
    for i in range(0,len(out)): #個別做 bubble
        bubble_sort(out[i]) 
    for i in range(0,len(out)): # 先合併所有list到array
        array = np.hstack((array, out[i])) 
    array = np.array(array, np.int32) # 因為前一行hstack自己合併自己np會出現浮點數所以需要轉回int32
    console = list(array)
    mergeSort(console) #做merge

    end = time.time()
    elapsed = end - start
    print ("Time taken: ", elapsed, " seconds.")
    
    fp = open('input_output.txt', 'w')
    for i in range(len(console)):
        fp.write( str(console[i]) + " " ) 
    fp.write( "\nTime taken: " + str(elapsed) + " seconds." ) 
    fp.close()