# -*- coding: utf-8 -*-
"""
Spyder Editor
TODO:
        Get rid of Global Variables?
"""

GRID_SIZE = 8
GRID = []

def grid_generator(n):
    global GRID
    GRID = ["."] * n
    for i in range(n):
        GRID[i] = ['.'] * n
    
grid_generator(GRID_SIZE)

# function to print a nice grid of inditerminate size
def nice_grid(board):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            print(board[x][y],end=' ')
        print()

# function to check if the location is a Q        
def spot_check(y0,x0):
    global GRID
    if GRID[y0][x0] == 'Q':
        return True
    return False

#checks the 4 diagonal directions for queenly threats
def diagonal_checker (y_pos,x_pos):
    xtl,xbl,xtr,xbr = x_pos,x_pos,x_pos,x_pos
# To the top left of the board
    for i in range(y_pos-1,-1,-1):
        xtl -= 1
        if xtl == -1:
            break
        if spot_check(i,xtl):
            return False
# Top Right of the Board
    for i in range(y_pos-1,-1,-1):
        xtr += 1
        if xtr == GRID_SIZE:
            break
        if spot_check(i,xtr):
            return False
# To the bottom left of the board
    for i in range(y_pos+1,GRID_SIZE):
        xbl -= 1
        if xbl == -1:
            break
        if spot_check(i,xbl):
            return False
# Bottom Right of the Board
    for i in range(y_pos+1,GRID_SIZE):
        xbr += 1
        if xbr == GRID_SIZE:
            break
        if spot_check(i,xbr):
            return False
        
#checks all directions for queenly checks
def is_valid(y,x):
    global grid
    if spot_check(y,x):
        return False
    for value in range(0,GRID_SIZE):
        if GRID[y][value] == 'Q':
            return False
    for value in range(0,GRID_SIZE):
        if GRID[value][x] == 'Q':
            return False
    if diagonal_checker(y,x) == False:
        return False
    return True

def place_queen(board,col):
    '''
    Checks to see if the grid size is excided if not will for the row its on
    Check if the coordinates can suport a queen, if so sets the grid location 
    to Q, then attempts to add the next queen via recursion,
    Will Backtrack on failure to place a queen. 
    After each successful grid is generated will ask for user input
    No matter what they do will output until all possible solutions are shown. 
    '''
    global GRID
    if col >= GRID_SIZE:
        nice_grid(GRID)
        input("More?")
        return
    for i in range(GRID_SIZE):
        # checks the grid to see if its been edited and if its valid
            if is_valid(i,col): 
                GRID[i][col] = 'Q'     
                place_queen(board,col+1)
                GRID[i][col] = '.'
    




def solve():
  # it solves the problem   
  place_queen(GRID,0)
        
            
solve()    