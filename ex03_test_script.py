# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 11:26:55 2018

@author: Nathan

"""

GRID_SIZE = 8

def grid_generator(n):
    grid = ["."] * n
    for i in range(1,n):
        grid[i] = ['.'] * n
    return grid

GRID = grid_generator(GRID_SIZE)

print(GRID)