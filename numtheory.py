# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:53:55 2014

@author: Barium
"""
def gcd(a,b):
    t = 1
    while b!= 0:
        t = b
        b = a%b
        a = t
    return a
        
        
def lcm(a,b):
    return abs(a*b)/gcd(a,b)       
    
def lcmm(lst):
    lst.sort()
    result = lcm(lst[1],lst[0])    
    for i in range(2,len(lst)):
        result = lcm(result,lst[i])
    return result