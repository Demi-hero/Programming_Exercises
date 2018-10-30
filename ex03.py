# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 09:56:54 2018

@author: Nathan
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
TODO:
        Get rid of Global Variables?
"""

grid_size = 8

def grid_generator(n):
    grid = ["."] * n
    for i in range(n):
        grid[i] = ['.'] * n
    return grid

grid = grid_generator(grid_size)

# function to print a nice grid of inditerminate size
def nice_grid(board):
    for y in range(grid_size):
        for x in range(grid_size):
            print(board[x][y],end=' ')
        print()

# function to check if the location is a Q        
def spot_check(y0,x0):
    if grid[y0][x0] == 'Q':
        return False

#checks the 4 diagonal directions for queenly threats
def diagonal_checker (y_pos,x_pos):
    xtl,xbl,xtr,xbr = x_pos,x_pos,x_pos,x_pos
# To the top left of the board
    for i in range(y_pos-1,-1,-1):
        xtl -= 1
        if xtl == -1:
            break
        if spot_check(i,xtl) == False:
            return False
# Top Right of the Board
    for i in range(y_pos-1,-1,-1):
        xtr += 1
        if xtr == grid_size:
            break
        if spot_check(i,xtr)== False:
            return False
# To the bottom left of the board
    for i in range(y_pos+1,grid_size):
        xbl -= 1
        if xbl == -1:
            break
        if spot_check(i,xbl)== False:
            return False
# Bottom Right of the Board
    for i in range(y_pos+1,grid_size):
        xbr += 1
        if xbr == grid_size:
            break
        if spot_check(i,xbr)== False:
            return False
        
#checks all directions for queenly checks
def is_valid(y,x):
    if spot_check == False:
        return False
    for value in range(0,grid_size):
        if grid[y][value] == 'Q':
            return False
    for value in range(0,grid_size):
        if grid[value][x] == 'Q':
            return False
    if diagonal_checker(y,x) == False:
        return False
    return True

def place_queen(board,col=0):
    # base case
    if col >= grid_size:
        nice_grid(grid)
        input("More?")
        return
    # this will incriment along the rows 1 by one.
    for i in range(grid_size):
        # checks the grid to see if selected coordinate is valid
            if is_valid(i,col): 
                # sets the grid location to Q
                grid[i][col] = 'Q'     
                # places a queen in the next row down
                place_queen(board,col+1)
                #Backtrack on failure
                grid[i][col] = '.'
    

def solve():
    # Because I was naughty and didn't get rid of all my global variables
    # does also exit after finding all the variables I did check
    place_queen(grid)       
        
solve()    

