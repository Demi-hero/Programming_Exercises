# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 11:26:55 2018

@author: Nathan
"""
grid = ["." ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.'],['.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.']

    
y,x = 0,0

def spot_check(y0,x0):
    if grid[y0][x0] == "Q":
        return False
    else:
        print ("No Clash")

def diagonal_checker (y_pos,x_pos):
    xtl,xbl,xtr,xbr = x_pos,x_pos,x_pos,x_pos
# To the top left of the board
    for i in range(y_pos-1,-1,-1):
        xtl -= 1
        if xtl == -1:
            break
        if spot_check(i,xtl) == False:
            return False
        print(i,xtl)
# Top Right of the Board
    for i in range(y_pos-1,-1,-1):
        xtr += 1
        if xtr == 8:
            break
        if spot_check(i,xtr)== False:
            return False
        print(i,xtr)
# To the bottom left of the board
    for i in range(y_pos+1,8):
        xbl -= 1
        if xbl == -1:
            break
        if spot_check(i,xbl)== False:
            return False
        print(i,xbl)
# Bottom Right of the Board
    for i in range(y_pos+1,8):
        xbr += 1
        if xbr == 8:
            break
        if spot_check(i,xbr)== False:
            return False
        print(i,xbr)


if diagonal_checker(y,x) == False:
    print("Wooo!")