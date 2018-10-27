# -*- coding: utf-8 -*-
"""
Spyder Editor


"""

grid = ['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.']


def nice_grid():
    for row in grid:
        for value in row:
            print (value, end = ' ')
        print()
        
def spot_check(y0,x0):
    if grid[y0][x0] == 'Q':
        return False

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
        if xtr == 8:
            break
        if spot_check(i,xtr)== False:
            return False
# To the bottom left of the board
    for i in range(y_pos+1,8):
        xbl -= 1
        if xbl == -1:
            break
        if spot_check(i,xbl)== False:
            return False
# Bottom Right of the Board
    for i in range(y_pos+1,8):
        xbr += 1
        if xbr == 8:
            break
        if spot_check(i,xbr)== False:
            return False
        

def is_valid(y,x):
    if spot_check == False:
        return False
    for value in range(0,8):
        if grid[y][value] == 'Q':
            return False
    for value in range(0,8):
        if grid[value][x] == 'Q':
            return False
    if diagonal_checker(y,x) == False:
        return False
    return True




def solve(n):
    ''' 
    n = number of queens to be solved for 
    '''
    ## makes sure every possible value is usable
    for y in range(0,8):
        for x in range (0,8):        
            # checks the grid to see if its been edited and if its valid
            if is_valid(y,x):
                # sets the grid location to Q
                grid[y][x] = 'Q'    
                # tries to add the next queen 
                solve(n-1)
                # if no solutions are found for here set the grid to .
                grid[y][x] = '.'
    nice_grid()
    input("More?")


solve(8)    