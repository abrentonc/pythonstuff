# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Barium\.spyder2\.temp.py
"""
def smooth(arr,length):
    result = zeros(len(arr))
    pos = length//2 
    if length>2:    
        for item in arr[length//2:-length//2]:
            total = 0            
            for spot in range(length):
                total += arr[pos - length//2 + spot]
            result[pos] = total/length
            pos += 1
    else:
        result[pos] = (arr[pos-1]+arr[pos])/2
    for j in range(length//2):
        result[j] = arr[j]
    for j in range(length//2+1):
        result[-j]= arr[-j]
    return result
                

def smoothrandomwalk(length, n):    
    for j in range(n):
        walk=randint(0,2,(length,))
        
        position = zeros(length)
        
        for i in range(1,length):
            if walk[i] == 0:
                position[i] = position[i-1]-1
            else:
                position[i] = position[i-1]+1
                
       
        plot(smooth(position,4))
        

def randomwalk(length, n):    
    for j in range(n):
        walk=randint(0,2,(length,))
        
        position = zeros(length)
        
        for i in range(1,length):
            if walk[i] == 0:
                position[i] = position[i-1]-1
            else:
                position[i] = position[i-1]+1
                
       
        plot(position)