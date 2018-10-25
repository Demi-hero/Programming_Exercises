# -*- coding: utf-8 -*-
"""
TODO 
- Handel a user input of = 
- Handel a user input of <
- Handel a user input of > 
- Handel incorrect input
- let the user know it figured out its cheating
"""
# Declaring all the important variables to prevent magic numbers
guess = 50 
max_upper_bound = 100
upper_bound = 100
lower_bound = 1
check = True
counter = 1

# A check on the upper and lowerbound distance
def val_check(var1, var2) :
    if (var1 - var2) < 1 :
        return True
    else:
        return False 
    
# A formula for deminishing returns after each guess  
def deminishing_returns():
    x = int(max_upper_bound/2**counter)
    if x == 0:
        x = 1
    return x
#Tells the user I know they cheated
def cheater():
    print("Those steps take us beyond one of our bounds")
    print("This means you have given inconsitent answers.")
    print("I don't work if you do that. Thanks for playing")

# gives the user a guess and asks for their response
def user_input_request():
    print('Is your number: {guess}?'.format(guess=guess))
    return input("If so let me know with =. Otherwise is it greater than(>) or less than(<).\n")


print("Think of a number between 1 and 100.")
print("Using the power of Maths I shall figure it out.")
user_response = user_input_request()

# The important part 
while check:
        # lets the user know the computer has guessed their number 
        if user_response == "=" :
            print ("Wohoo I got it. Thanks for playing")
            print("It only took me {counter} step(s)")
            check = False
        # how it handles >  
        elif user_response == "greater than" or user_response == ">" :
            counter += 1  
            lower_bound = guess + 1
            guess = guess + int(deminishing_returns())
            # this is the safeguard to make sure the user isn't givng bad data
            if val_check(upper_bound, lower_bound):
                cheater()
                check = False
                break
            user_response = user_input_request()
        #how it handles < 
        elif user_response == "less than" or user_response == "<" :
            counter += 1
            upper_bound = guess - 1
            guess = guess - int(deminishing_returns())
            # this is the safeguard to make sure the user isn't givng bad data
            if val_check(upper_bound, lower_bound):
                cheater()
                check = False
                break
            user_response = user_input_request()
        else:
            # what is given when they input bad entry data
            print ("Thats not quite right please input =,< or, >")
            break       
