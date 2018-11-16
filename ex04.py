# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 09:26:13 2018

Problem Set 4 

ToDo:
    Truth Table
        
        Create a dict of variables
        Iterate over dictionary to turn things in to true and false
        both of these can be done with a recursive backtracker
    Tautology
        run truth table
        if all values are true return true

@author: Nathan
"""


class Expr:
    # parent class for all the classes
        
    def __str__(self):
        return self.bound_str(0)
        

    def make_list(stuborn):
        coercive = []    
        for value in stuborn: 
            coercive += value 
        return coercive
    
    def truth_table(variables):
        # this should recursively build a truth table
        # will only accept lists though
        pass
    
    # support function for make truth table
    def variable_fetch(self):
        new_list = self.variable_fetch()
        return list(new_list)
  
    #
    def make_tt(self):
        # make the variable and dictionary needed for the table
        bool_dict = {}
        tt_var = make_list(self.variable_fetch())
        for var in tt_var :
            bool_dict[var] = True
            print("{} \t|".format(var),end=' ')
        print("{}".format(self.bound_str(0)))
        
        

class LogOpr(Expr):
    # Parent class for all binary operations
    def __init__(self, left, right): 
        self.left = left
        self.right = right

    def bound_str(self, precidence):
        string = (self.left.bound_str(self.precidence) + 
                  self.opp + self.right.bound_str(self.precidence))
        if self.precidence < precidence:
            return "(" + string + ")"
        else:
            return string
    
    def variable_fetch(self):
        return self.left.variable_fetch().union(self.right.variable_fetch())              

    def eval(self, env):
        return self.func(self.left.eval(env), 
                         self.right.eval(env))


class And(LogOpr):
    # this is a seperate class of opperatior single opp but as there is
    # only one I have not created an explicite SingOpp class
    precidence = 3
    opp = '&'

    def func(self, left, right) :
        return left & right


class Or(LogOpr):

    precidence = 2
    opp = "|"

    def func(self, left, right):
        return left | right


class Eq(LogOpr):
    precidence = 1
    opp = '=='

    def func(self, left, right):
        return left == right


class Not(Expr):
    
    precidence = 4

    def __init__(self, value):
        self.value = value

    def bound_str(self, precidence):
        string = str(self.value.bound_str(self.precidence))
        if self.precidence < precidence:
            return "!(" + string + ")"
        else:
            return "!" + string
    
    def variable_fetch(self):
        return self.value.variable_fetch()
    
    def eval(self,env):
        return not self.value.eval(env)
    
class Var(Expr):

    def __init__(self,variable):
        self.variable = variable

    def bound_str(self,precidence):
        return self.variable
    
    def eval(self, env):
        return env[self.variable]
    
    def variable_fetch(self):
        return {self.variable}


VarVal = { "x": False, "y": True }

e1 = Or(Var("x"), Not(Var("x")))
e2 = Eq(Var("x"), Not(Not(Var("x"))))
e3 = Eq(Not(And(Var("x"), Var("y"))), Or(Not(Var("x")), Not(Var("y"))))
e4 = Eq(Not(And(Var("x"), Var("y"))), And(Not(Var("x")), Not(Var("y"))))
# print(str(e3))
# print(e3.variable_fetch())
print(e3.make_tt())