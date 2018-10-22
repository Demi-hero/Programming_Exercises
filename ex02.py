# -*- coding: utf-8 -*-
"""
TODO 
- Imitate the layout of the pdf output 
- Handel a user input of = 
- Handel a user input of <
- Handel a user input of > 
- Handel incorrect input
- let the user know it figure out its cheating
"""
# Declaring all the important variables to begin with just to get it done
guess = 50 
max_upper_bound = 100
upper_bound = 100
lower_bound = 1
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
    x = int(max_upper_bound/2**counter)
    if x == 0:
        x = 1
    return x
#lets me easily reset the game if the user gives me bad data   
def cheater():
    print("Those steps take us beyond one of our bounds")
    print("This means you have given inconsitent answers.")
    print("I don't work if you do that. Thanks for playing")
# lets me quickly give the user a guess and asks for their response
def user_input_request():
    print("Is your number:",guess,"?")
    return input("If so let me know with =. Otherwise is it greater than(>) or less than(<).\n")


print("Think of a number between 1 and 100.")
print("Using the power of Maths I shall figure it out.")
user_response = user_input_request()


while check == True:
        # lets the user know the computer has guessed their number 
        if user_response == "=" :
            print ("Wohoo I got it. Thanks for playing")
            print ("It only took me", counter, "steps")
            check = False
        # how it handles >  
        elif user_response == "greater than" or user_response == ">" :
            counter += 1  
            lower_bound = guess 
            guess = guess + int(deminishing_returns())
            # this is the safeguard to make sure the user isn't givng bad data
            if val_check(upper_bound, lower_bound) == True :
                cheater()
                check = False
                break
            user_response = user_input_request()
        #how it handles < 
        elif user_response == "less than" or user_response == "<" :
            counter += 1
            upper_bound = guess
            guess = guess - int(deminishing_returns())
            # this is the safeguard to make sure the user isn't givng bad data
            if val_check(upper_bound, lower_bound) == True :
                cheater()
                check = False
                break
            user_response = user_input_request()
        else:
            print ("Thats not quite right please input =,< or, >")
            break       
