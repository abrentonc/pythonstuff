# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 09:50:43 2014

@author: Barium
"""                   
    
    
 
# This is a basic matrix multiplication function
                   
def mmatrix(Array1,Array2):
    d11 = len(Array1)
    d12 = len(Array1[0])
    d21 = len(Array2)
    d22 = len(Array2[0])
    if d12 == d21:  #insures proper dimensions
        result = zeros([d11,d22])
        for i in range(d11):
            for j in range(d12):
                for k in range(d12):
                    result[i,j] += Array1[i,k]*Array2[k,j]
        return result
    else:
        print 'wrong dims'
        return None   
            
# This takes a permutation and builds a matrix.
            
def p_matrix(perm):
   d = len(perm)
   result = zeros([d,d])
   for i in range(d):
       result[i,perm[i]-1] = 1
   return result
   

# This is an attempt to do an LU decomposition on given (square??) array


def lu_decomp(Array):
    a = Array
    N = len(a)    
    perm = range(N)
    p = 0
    n = 0
    s = 0
    h = 0
    d = 1
    for j in range(N):
        for i in range(j):
            s = 0            
            for k in range(1,i):
                s += a[i,k]*a[k,j]
            a[i,j] += -s
        p = abs(a[j,j])
        n = j
        for i in range(j+1,N):
            s = 0            
            for k in range(j):
                s += a[i,k]*a[k,j]
            a[i,j] += -s
            if abs(a[i,j])>p:
                p = abs(a[i,j])
                n = i
        if p == 0:
            return "singular"
        if n!=j:
            temp = range(N)
            h = temp[n]
            temp[n] = temp[j]
            temp[j] = h
            h = perm[n]
            perm[n] = perm[j]
            perm[j] = h
            a = mmatrix(p_matrix(temp),a)
            d = -d
        for i in range(j+1,N):
            a[i,j] = a[i,j]/a[j,j]
    return [a,p_matrix(perm)]



# This does a basic transpose of a matrix
   
def transpose(m):
    d1 = len(m)
    d2 = len(m[0])
    result = zeros([d2,d1])
    for i in range(d1):
        for j in range(d2):
            result[i,j] = m[j,i]
    return result
    
#This does a forward substitution to solve Ly = b system

def forward_solve(L,b):
    d = len(b)
    y = array([0]*d)
    for i in range(d):
        s = 0
        for j in range(i):
            s += L[i,j]*y[j]
        y[i] = (b[i]-s)/L[i,i]
    return y
    
#This does a backward substitution to solve Ux = y system    

def backward_solve(U,y):
    d = len(y)
    x = array([0]*d)
    a = range(d)
    a.reverse()
    for i in a:
        s = 0
        for j in range(d-i-1):
            s += U[i,d-j-1]*x[d-j-1]
        x[i] = (y[i]-s)/U[i,i]
    return x

#This solves Ax = b system via LU decomposition 

def lu_solve(A,b):
    LU = lu_decomp(A)
    return backward_solve(LU[1],forward_solve(LU[0],b))  
    

    