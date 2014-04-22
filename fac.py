# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 14:18:01 2014

@author: Barium
"""
def fac(n):
    product = 1    
    for i in range(1,n+1):
        product = product*i
    return product
    
def binomial(m,n):
    return fac(m)/fac(n)/fac(m-n)

i = 0
n = 7    
while n<=1000:
    for m in range(1,n+1):
        if binomial(n,m)%7 == 0:
            i += 1
    n+=1
print i           