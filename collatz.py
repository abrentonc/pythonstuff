# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 08:36:08 2014

@author: Barium
"""

#this builds a collatz sequence

def collatz(n):
    seq = []
    nxt = n
    while nxt!=1:
        seq.append(nxt)
        if nxt%2==0:
            nxt = nxt/2
        else:
            nxt = 3*nxt + 1
    return len(seq)+1
n = 2
d = {}    
while n<10**6:    
    nxt = n
    i = 0
    while nxt!=1:
        if nxt in d:
            d[n]=i+d[nxt]
            break
        elif nxt%2==0:
            nxt = nxt/2
        else:
            nxt = 3*nxt + 1
        i += 1
        d[n]= i + 1
    n += 1
m = max(d.itervalues())    
for item in d.iteritems():
    if item[1] == m:
        print item[0]
        break