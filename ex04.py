# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 09:26:13 2018

Problem Set 4 

ToDo:
    Truth Table
        Stop showing None
    Tautology
        run truth table
        if all values are true return true

@author: Nathan
"""


class Expr:
    # parent class for all the classes
        
    taut_flag = 1
    
    def __init__(self):
        self.header = 0
        
    def __str__(self):
        return self.bound_str(0)
    
    def truth_table_genisis(self,n, var_dict, taut, truths=[]):
        # Base case where n = 0, have also included some things that allow 
        # it to do my taut checking for me.
        
        if not n:
        # this creates the key value parings and prints the truth table.
            for truth, key in zip(truths, var_dict):
                var_dict[key] = truth
                if not taut:
                    print("{} \t|".format(truth),end="")
            #if self.eval(var_dict)) :
            # evaluates the key:value pair of this itteration and prints it
            if not taut:
                print (self.eval(var_dict))
            if not self.eval(var_dict):
                self.taut_flag = 0
        # recurs until we hit the max lenght of the variable list.
        else:
            for i in [True,False]:
                self.truth_table_genisis(n-1,var_dict,taut,truths+[i])

    def make_list(self,stuborn):
        coercive = []    
        for value in stuborn: 
            coercive += value 
        # hands back a list of stuff    
        return coercive
    
    # support function for make truth table
    def variable_fetch(self):
        new_list = self.variable_fetch()
        return list(new_list)
  
    def make_tt(self, taut = 0):
        # make the variable and dictionary needed for the table
        bool_dict = {}
        tt_var = self.make_list(self.variable_fetch())
        for var in tt_var :
            bool_dict[var] = ""
            if not taut:
                print("{} \t|".format(var),end=' ')
        if not taut:
            print("{}".format(self.bound_str(0)))
        self.truth_table_genisis(len(tt_var),bool_dict,taut)
        return ""
        
    def isTauto(self):
        # does the truth table work with none of the printing
        self.make_tt(taut = 1)
        if self.taut_flag:
            return True
        else:
            return False

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
# print(e3.make_list(e3.variable_fetch()))
#print(e3.eval(VarVal))
print(e3.make_tt())
