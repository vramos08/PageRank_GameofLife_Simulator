# -*- coding: utf-8 -*-
"""
PageRank Algorithm
    This algorithm will create a matrix where the array will have a fixed
    size of 6 by 6 with zeros and ones. If there is a one, that means that there
    is a connection between the pages and a zero shows no connection.
    I will normalize this array by finding the total of each
    column and dividing each one by the sum. I will then create a vector r
    and apply the formula r′ = αMr + (1−α)s and iterate until r converges.
"""
import numpy as np

def PageRanker(A):
    #normalize the array so that it becomes the sum of 1
    #To do this I will be adding each column and diving it by the total
    total1 = 0 
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    
    #looping through the array and adding each column 
    for i in range (0, 6):
        for j in range (0,6):
            if j==0:
                total1 = total1+ A[i,j]
            elif j==1:
                total2 = total2 + A[i,j]
            elif j==2:
                total3 = total3 + A[i,j]
            elif j==3:
                total4 = total4 + A[i,j]
            elif j==4:
                total5 = total5 + A[i,j]
            else:
                total6 = total6 + A[i,j]
    #now I know the total for each column, I will be changing it so that
    #it will become 1/total for each 1
    M = np.zeros((6,6), dtype = np.float64)
    
    #I will be looping through the matrix A to find 1s and replace them
    for i in range (0,6):
        for j in range (0,6):
            if A[i,j]==1:
                if j==0:
                    M[i,j] = 1/total1
                elif j==1:
                    M[i,j] = 1/total2
                elif j==2:
                    M[i,j] = 1/total3
                elif j==3:
                    M[i,j] = 1/total4
                elif j==4:
                    M[i,j] = 1/total5
                elif j==5:
                    M[i,j] = 1/total6
    #initialize a vector named r with size 6 and each value is 1/6
    #s = vector size 6 with all entries equal to 1/6
    #threshold of 1e -6
    a = 0.85
    r = np.array([1/6,1/6,1/6,1/6,1/6,1/6], dtype = np.float64)
    s = np.array([1/6,1/6,1/6,1/6,1/6,1/6], dtype = np.float64)    
    threshold = .000001
    
    #updating r until the difference between consecutive r values is
    #below threshold
    converges = True
    while converges:
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
#Testing my code for this section
A = np.array([
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0]
])

test = PageRanker(A)
#print(A)
print("REAL")
print(test)
arrayMtest = np.array([
    [0, 0.33333333, .5, 0  , 0, 0],
    [0, 0  , 1  , .5, 0, 0],
    [1, 0  , 0  , 0  , 0, 0],
    [0, 0.33333333, 0  , 0  , .5, 0],
    [0, 0.33333333, 0  , .5, 0, 1],
    [0, 0  , 0  , 0  , .5, 0]
])
#print("this is real")

#testing that the r part works
# Calculate the eigenvalues and eigenvectors
eigval, eigvec = np.linalg.eig(arrayMtest)
print(eigvec)



    
    
    
    


