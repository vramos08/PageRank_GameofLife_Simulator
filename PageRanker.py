# -*- coding: utf-8 -*-
"""
PageRank Algorithm
    -first I need to make the matrix given to become
    a new matrix that adds up to 1. 
    - Assume that the array A is already numpy array
    
"""
import numpy as np

def PageRanker(A):
    #normalize the array so that it becomes the sum of 1
    #To do this I wil be adding each column and diving it by the total
    total1 = 0 
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    
    #looping through the array and adding each column 
    for i in range (0, 5):
        for j in range (0,5):
            if i==0:
                total1 = total1+ A[i,j]
            elif i==1:
                total2 = total2 + A[i,j]
            elif i==2:
                total3 = total3 + A[i,j]
            elif i==3:
                total4 = total4 + A[i,j]
            elif i==4:
                total5 = total5 + A[i,j]
            else:
                    total6 = total6 + A[i,j]
    #now i know the total for each column, I will be changing it so that
    #it will become 1/total for each 1
    
    M = np.zeros((6,6), dtype = np.float64)
    
    #I will be looping through the matrix A to find 1s and replace them
    for i in range (0,5):
        for j in range (0,5):
            if A[i,j]==1:
                if i==0:
                    newVal = 1/total1
                    M[i,j] = newVal
                elif i==1:
                    newVal = 1/total2
                    M[i,j]== newVal
                elif i==2:
                    newVal = 1/total3
                    M[i,j]== newVal
                elif i==3:
                    newVal = 1/total4
                    M[i,j] = 1/newVal
                elif i==4:
                    newVal = 1/total5
                    M[i,j] = newVal
                elif i==5:
                    newVal = 1/total6
                    M[i,j] = newVal
    #initialize a vector named r with size 6 and each value is 1/6
    #s = vector size 6 with all entries equal to 1/6
    #threshold of 1e -6
    a = 0.85
    r = np.array([1/6,1/6,1/6,1/6,1/6,1/6], dtype = np.float64)
    s = np.array([1/6,1/6,1/6,1/6,1/6,1/6], dtype = np.float64)
    threshold = 1e-6
    
    #updating r until the difference between consecultive r values is
    #below threshold
    converges = True
    while not converges:
        updated_r = a * np.dot(M,r) + (1-a)*s
        difference1 = abs(r[0]-updated_r[0])
        difference2 = abs(r[1]-updated_r[1])
        difference3 = abs(r[2]-updated_r[2])
        difference4 = abs(r[3]-updated_r[3])
        difference5 = abs(r[4]-updated_r[4])
        difference6 = abs(r[5]-updated_r[5])
        if difference1<threshold and difference2<threshold and difference3<threshold and difference4 <threshold and difference5< threshold and difference6< threshold:
             converges = False
        else:
            r = updated_r
    return r
        
    
  
  

                
    
    
    
    


