# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:01:40 2018

recursive name swap
"""

def recursive_name_swap(source):
    #base case
    if source == []:
        return []
    else:
        return source[-1:] + recursive_name_swap(source[0:-1])

exp = list(input("word to swap please!"))
   
x = recursive_name_swap(exp)
print(x)

