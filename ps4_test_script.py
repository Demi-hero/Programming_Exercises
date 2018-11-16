# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:19:07 2018

@author: Nathan

Truth table psudo code
"""

"""Boolians = { 1: [True, True], 2:[False, True]}

print ("{} \t| {} \t| str(equation)".format("x", "y"))
for key in Boolians :
    print ("{} \t| {} \t| eval(equation)".format(
            Boolians[key][0], Boolians[key][1])
    )
    print ("{} \t| {} | eval(equation)".format(
            not Boolians[key][0], not Boolians[key][1])
    )

x = list({1,2,3})
y = [{1,2,3}]
print(x)
type(x)
type(y)
"""

def make_list(stuborn):
    l = []    
    for value in stuborn: 
        l += value 
    return l
make_list({"A","B","c","d"})


def dict_printer(var_dict):
    for key in var_dict:
        print ("{} \t|".format(key),end="")


""" 
for the total amount of variables 
    starting at the first variable set it to true
    once all values have been processed evaluate the dict.
    Then change the last value to False 
    Evaluate the dict
    change the value above to false and the value below to true.
"""

test_dict = {"A":0 ,"B":0 ,"c":0 ,"d":0 }
HEADER = 0

def truth_table(n, var_dict, truths=[]):
    global HEADER
    if not n:
        # generates the header the frist time around
        if HEADER == 0:
            for key in var_dict:
                print ("{} \t|".format(key),end="")
            HEADER += 1
            print("str function")
        # this creates the key value parings and prints the truth table.
        for truth, key in zip(truths, var_dict):
            var_dict[key] = truth
            print("{} \t|".format(truth),end="")
        # evaluates the key:value pair of this itteration
        print ("eval function(var_dict)")
    else:
        for i in [True,False]:
            truth_table(n-1,var_dict,truths+[i])

# dict_printer(test_dict)
truth_table(len(test_dict),test_dict)