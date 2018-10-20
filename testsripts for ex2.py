# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:31:45 2018

@author: Nathan
"""

guess = 50 
lowbnd = 1
upbnd = 100
counter = 1

def cheater():
    print("AHA I have it.")
    print("Those steps mean that it must be", guess)
    print("If its not someone has been cheating and I don't want to play anymore")

    
def val_check(var1, var2) :
    if (var1 - var2) < 1 :
        return True
    else:
        return False 

def deminishing_returns():
    x = int(100/2**counter)
    if x == 0:
        x = 1
    return x

check = True

while check == True:
    exit  = input("do you want to continue Y/N")      
    if exit == "Y" or exit == "y":
        counter += 1  
        lowbnd = guess 
        # this is the safeguard to make sure the user isn't givng bad data
        if val_check(upbnd, lowbnd) == True :
            cheater()
            check = False
            break
        minish_return = deminishing_returns()
        guess = guess + minish_return
        print(counter, upbnd, lowbnd)
    else:
        check = False