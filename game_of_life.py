# -*- coding: utf-8 -*-
"""
Game of Life
    For this algorithm, I will be creating an array that will simulate
    Conway's Game of Life. First I will be importing nump to create an array.
    I will be making the arrays true or false and be set to size 20 by 20 as
    an example. I will be creating a function evolve where it accepts a grid
    and applies the principles of Conway's Game of life. I will be
    using mode to make sure that there will always be a neighbour regardless of
    where the squares are to simulate an infinite graph. I will then plot the 
    animation using matplotlib.animation. 
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
#creaing the example array with true and false
"""
grid = np.zeros((20,20), dtype = bool)
grid[12, 10] = True
grid[12, 11] = True
grid[12, 12] = True
grid[10, 11] = True
"""
#using the same example but smaller
grid = np.zeros((5,5), dtype = bool)
grid[1,2] = True
grid[2,2] = True
grid[2,0] = True
grid[3,1] = True
grid[3,2] = True


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
#I will be making it so that the neighbors are changed into a new grid so it doesnt change
#the original
def evolve(grid):
    #countTrue = 0
    #countFalse = 0
    row,col = grid.shape
    
    updatedGrid = np.zeros((row,col), dtype = bool)
    for i in range (0,row):
        for j in range (0,col):
            countTrue = 0
            if grid[(i+1)%row, j]== True: #the right one
                countTrue +=1
            if grid[(i-1)%row, j]==True: #the left one 
                countTrue += 1
            if grid[(i+1)%row, (j+1)%col]== True: #the top right
                countTrue += 1
            if grid[(i-1)%row, (j-1)%col] == True: #the bottom left
                countTrue += 1
            if grid[i,(j+1)%col] == True: #the top
                countTrue += 1
            if grid[i,(j-1)%col] == True: #the bottom
                countTrue += 1
            if grid[(i+1)%row, (j-1)%col]== True: #the bottom right
                countTrue +=1
            if grid[(i-1)%row, (j+1)%col]== True: #the top left
                countTrue +=1
                
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
    return updatedGrid    
#I imported sys to be able to handle to command line
#This code is given by ChatGPT 

if len(sys.argv) != 2:
    print("python game_of_life.py <iterations>")
    sys.exit(1)
try:
    iterations = int(sys.argv[1])
    if iterations<=0:
            print("Please enter a positve integer.")
            sys.exit(1)
except ValueError:
    print("Please enter a value for the evolutionary steps.")
    sys.exit(1)

for _ in range(iterations):
    updated_grid = evolve(grid)
    grid = updated_grid

#This is the code for updating the gif
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap = 'gray', vmin=0, vmax = 1)
def update(num,grid):
    new_data = evolve(grid)
    im.set_data(new_data)
    grid[:,:]= new_data
    return im,

ani = animation.FuncAnimation(fig, update, frames=100, fargs=(grid,), interval=10, blit=True, repeat=False)
writer = animation.PillowWriter(fps=10)
ani.save('animation.gif',writer=writer)
plt.close()

#this is getting the final grid image
fGrid = evolve(grid)
plt.imshow(fGrid, cmap = 'gray',vmin = 0, vmax = 1)
plt.axis('off')
plt.savefig('game_of_life.png', bbox_inches = "tight", pad_inches = 0, format = 'png',dpi=300)
plt.close()
