# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:00:33 2018

@author: Nathan
"""
# Declaring all the important variables to begin with just to get it done
guess = 0 
upprbnd = 10
lowrbnd = -10
check = True
counter = 1

# let me shorthand the upper and lowerbound check
def val_check(var1, var2) :
    if (var1 - var2) <= 1 :
        return True
    else:
        return False 
    
# lets me shorthand out formula for deminishing returns   
def deminishing_returns():
    x = int(upprbnd/2**counter)
    if x == 0:
        x = 1
    return x
#lets me easily reset the game if the user gives me bad data   
def cheater():
    print("AHA I have it.")
    print("Those steps mean that it must be", guess)
    print("And it only took me", counter, "steps")
    print("If its not someone has been cheating and I don't want to play anymore")
# unsure if I should have made a function to save writing this second part out twice


print("Think of a number between -10 and 10.")
print("Using the power of Maths I shall figure it out.")

while check == True:
    try:
        print("is your number:",guess,"?")
        usr_resp = input("if so let me know with =. Otherwise is it greater than (>) or less than (<)\n")
        # lets the user know the computer has guessed their number 
        if usr_resp == "=" :
            print ("Wohoo I got it. Thanks for playing")
            print ("It only took me", counter, "steps")
            check = False
        # how it handles >  
        elif usr_resp == "greater than" or usr_resp == ">" :
            counter += 1  
            lowrbnd = guess 
            minish_return = deminishing_returns()
            guess = guess + int(minish_return)
            # this is the safeguard to make sure the user isn't givng bad data
            if val_check(upprbnd, lowrbnd) == True :
                cheater()
                check = False
                break       
        #how it handles < 
        elif usr_resp == "less than" or usr_resp == "<" :
            counter += 1
            upprbnd = guess
            minish_return = deminishing_returns()
            guess = guess - int(minish_return)
            # this is the safeguard to make sure the user isn't givng bad data
            if val_check(upprbnd, lowrbnd) == True :
                cheater()
                check = False
                break       
    except ValueError:
        print ("Thats not quite right please input =,< or, >")