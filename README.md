This is our second mini-project where we use Python to create scripts. There are two different files titled PageRanker.py and game_of_life.py. PageRanker will simulate having 6 pages in a website where each page has links between them. This can be expressed as a matrix, where matrix A shows 0 for no connection between pages and 1 for a connection between pages. PageRanker(A) is a function that will take in arrays such as matrix A and normalize the columns so they sum to 1. I imported numpy as np to aid with the arrays and calculations. I did this by looping through the array with for loops with ranges 0 to 6 adding the total to different values and storing it. I then created an array M with zeros and the same size as array A. I then looped through the array of A, if there was a 1, I would change the value to 1/total of that column and add it to the new matrix. I then initialized the values for a, r, s, and the threshold. I did this because I needed to apply the formula r' = aMr + (1-a)s where M is the normalized matrix, r, and s are vectors of size 6 with all entries equal to 1/6, and a is the damping factor set to 0.85. The rank must be iterated until r converses which means that the difference between consecutive r values is below a threshold of 1e-6. To do this, I created a boolean converges and set it to true and a while loop that only worked when converges were true. In the loop, I created a value updated_r that takes in the formula. I then found the differences between the first and last iterations of r. If each one is below the threshold, then converges is set to false and leaves the loop. If not then r becomes the updated_r. This would then return the value of r. In order to test that the code works, I used np.linalg.eig() to verify the answer.
The second file, game_of_life implements and visualizes Conway's Game of Life. To do this, we must visualize the grid as an array filled with true and false. For this example, the pattern known as "Glider" will be in the middle of the 20 by 20 array. If there is a false, that means that the cell is dead, and true would mean that the cell is alive. If the cell is alive and has less than 2 live neighbors, it will die. If it has 2 or 3 live neighbors, it will continue living. If there are more than 3 live neighbors, then it will die. If the cell is already dead and has exactly 3 live neighbors, then it will become alive. In order to do this, I imported numpy as np. To begin, I created an example array with the known "Glider pattern" somewhere in the middle. I then created a function evolve that takes in a grid. I then created an updatedGrid that is the same size as the grid that was input. I then created a loop that ran through the grid and applied the live or dead conditions to the grid. I also made it so that it would contain mode so that if it was running through the top, bottom, or sides, it would always have a neighbor. I then had to import matplotlib.py as plt and matplolib.animation as animation to be able to visualize the new evolutions.
