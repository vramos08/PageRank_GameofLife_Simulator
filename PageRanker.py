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
            if A[i,j]==1 and i==0:
                newVal = 1/total1
                M[i,j] = newVal
            elif A[i,j]==1 and i==1:
                newVal = 1/total2
                M[i,j]== newVal
            elif A[i,j]==1 and i==2:
                newVal = 1/total3
                M[i,j]== newVal
            elif A[i,j]==1 and i==3:
                newVal = 1/total4
                M[i,j] = 1/newVal
            elif A[i,j]==1 and i==4:
                newVal = 1/total5
                M[i,j] = newVal
            elif A[i,j]==1 and i==5:
                newVal = 1/total6
                M[i,j] = newVal
  #Now the array M is made
  

                
    
    
    
    


