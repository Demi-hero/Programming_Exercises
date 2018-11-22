# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 09:26:13 2018

Problem Set 4 

ToDo:
    Done?
@author: Nathan
"""


class Expr:
    # parent class for all the classes
    
    def __init__(self):
        self.header = 0
        
    def __str__(self):
        return self.bound_str(0)

                
    def create_truth_list(self,n, m, truths=[]):
        if not n:
            m[:] = m + [truths]
        else:
            for i in [True, False]:
                self.create_truth_list(n-1, m, truths+[i])

    def make_list(self,var_set):
        variables = []    
        for value in var_set: 
            variables += value 
        # hands back a list of stuff    
        return variables
    
    # support function for make truth table
    def variable_walk_down(self):
        return list(self.variable_fetch())
         
  
    def make_tt(self,tautology = 0):
        # make the variable and dictionary needed for the table
        bool_dict = {}
        truth_list = []
        truth_table = ""
        # make a list of variables 
        tt_var = self.make_list(self.variable_walk_down())
        # make a list of lists reping TT rows
        self.create_truth_list(len(tt_var),truth_list)
        # assigne the expression variabls to dictionary keys and create the 
        # header
        for var in tt_var :
            bool_dict[var] = ""
            truth_table = truth_table + "{} \t|".format(var)
        truth_table = truth_table + "{} \n".format(self.bound_str(0))
        # append the evaluation to the end of each line in truth list
        for lines in truth_list:
            for key,boolian in zip (bool_dict, lines):
                bool_dict[key] = boolian                 
            lines = lines.append(self.eval(bool_dict))
            if tautology and not self.eval(bool_dict):
                return False
        # self.create_truth_table(len(tt_var),bool_dict,tautology)
        if not tautology:
            for lines in truth_list: 
                for values in range (len(lines)-1):
                    truth_table = truth_table + "{} \t|".format(lines[values])
                truth_table = truth_table + "{} \n".format(lines[-1])
            return truth_table
        # this only fires on Tautology call no false evaluations 
        return True
    
    
    def isTauto(self):
        # does the truth table work with none of the printing
        return self.make_tt(tautology=1)


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
        return self.left.variable_fetch() | (self.right.variable_fetch())              

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