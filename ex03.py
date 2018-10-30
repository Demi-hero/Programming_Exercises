# -*- coding: utf-8 -*-
"""
Spyder Editor

TODO:
    Find More Than One Solution#
    Fold Never Give Up & Solve together
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

def place_queen(board,col):
    if col >= grid_size:
        nice_grid(grid)
        input("More?")
        return
    for i in range(grid_size):
        # checks the grid to see if its been edited and if its valid
            if is_valid(i,col): 
            # sets the grid location to Q,tries to add the next queen,Backtrack on failure
                grid[i][col] = 'Q'     
                place_queen(board,col+1)
                grid[i][col] = '.'
    

place_queen(grid,0)

'''
def solve():
    
   # n = number of columns to be solved for 
   # need to use this to deal with global varaibles 
    while True :
        # Recurs until it has a solution (In theory) then asks if you want 
        # another one
        never_give_up(grid,0)         
        nice_grid(grid)    
        cont = input("More?")
        if cont == 'no' :
            break
        
            
solve()    
'''