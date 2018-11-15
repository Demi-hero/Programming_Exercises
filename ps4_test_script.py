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