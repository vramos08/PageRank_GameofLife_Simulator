# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:14:38 2023

@author: viann
"""
import sys
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import math

grid = np.zeros((20,20), dtype = bool)
grid[12, 10] = True
grid[12, 11] = True
grid[12, 12] = True
grid[10, 11] = True

#RULES
# 1. if the current cell is true and has less than 2 alive neighbors
#   it will now be false
# 2. if the current cell is true and has 2 or 3 alive neighbors
#   it will be true
# 3. if the current cell is true and has more than 3 alive it will die
#   befomes false
# 4. if the current cell is false and has exactly three will relive
#   becomes true
#eight enighbors are the boxes around
#I will be making it so that the neighbors are changed into a new grid so it doesnt change it automatically
def evolve(grid):
    countTrue = 0
    countFalse = 0
    updatedGrid = np.zeros((20,20), dtype = bool)
    for i in range (0, 19):
        for j in range (0,19):
            if grid[(i+1)%20, j]== True:
                countTrue +=1
            if grid[(i-1)%20, j]==True:
                countTrue += 1
            if grid[(i+1)%20, (j+1)%20]== True:
                countTrue += 1
            if grid[(i-1)%20, (j-1)%20] == True:
                countTrue += 1
            if grid[i,(j+1)%20] == True:
                countTrue += 1
            if grid[i,(j-1)%20] == True:
                countTrue += 1
            if grid[(i+1)%20, (j-1)%20]== True:
                countTrue +=1
            if grid[(i-1)%20, (j+1)%20]== True:
                countTrue +=1
            countFalse = 8-countTrue
            #now applying the cell conditions
            if grid[i,j]==True:
                if countTrue <2:
                    updatedGrid[i,j] = False
                if countTrue==2 or countTrue==3:
                    updatedGrid[i,j] = True
                if countTrue>3:
                    updatedGrid[i,j] = False
            elif grid[i,j]==False:
                if countTrue==3:
                    updatedGrid[i,j] = True
    