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
"""
x = list({1,2,3})
y = [{1,2,3}]
print(x)
type(x)
type(y)

def make_list(stuborn):
    l = []    
    for value in stuborn: 
        l += value 
    return l
print(make_list({"A","B","c","d"}))


""" 
for the total amount of variables 
    starting at the first variable set it to true
    once all values have been processed evaluate the dict.
    Then change the last value to False 
    Evaluate the dict
    change the value above to false and the value below to true.
"""

def truth_table(n, truths=[]):
    if not n:
        return truths
    else:
        for i in [True,False]:
            truth_table(n-1,truths+[i])


truth_table(3)