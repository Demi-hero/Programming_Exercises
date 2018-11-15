# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 09:26:13 2018

Problem Set 4 

@author: Nathan
"""


class Expr():

    Boolians = { 1: [True,True], 2:[False,True]}
    
    def __str__(self):
        return self.bound_str(0)

    def make_tt(self):
        print ("{} \t| {} \t| str(equation)".format("x", "y"))
        for key in self.Boolians :
            print ("{} \t| {} \t| eval(equation)".format(self.Boolians[key][0],
                    self.Boolians[key][1]))
            print ("{} \t| {} \t| eval(equation)".format(
                    not self.Boolians[key][0], not self.Boolians[key][1])
            )
class LogOpr(Expr):
    
    def __init__(self, left, right): 
        self.left = left
        self.right = right

    def bound_str(self, precidence):
        string = self.left.bound_str(self.precidence) + self.opp + self.right.bound_str(self.precidence)
        if self.precidence < precidence:
            return "(" + string + ")"
        else:
            return string
                      

    def evaluate(self, env):
        return self.func(self.left.evaluate(env), 
                         self.right.evaluate(env))


class And(LogOpr):

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
        string = str(self.value)
        if self.precidence < precidence:
            return "!(" + string + ")"
        else:
            return "!" + string
    
    def evaluate(self,env):
        return not self.value.evaluate(env)
    
class Var(Expr):

    def __init__(self,variable):
        self.variable = variable

    def bound_str(self,precidence):
        return self.variable
    
    def evaluate(self, env):
        return env[self.variable]


VarVal = { "x": False, "y": True }

e1 = Or(Var("x"), Not(Var("x")))
e2 = Eq(Var("x"), Not(Not(Var("x"))))
e3 = Eq(Not(And(Var("x"), Var("y"))), Or(Not(Var("x")), Not(Var("y"))))
e4 = Eq(Not(And(Var("x"), Var("y"))), And(Not(Var("x")), Not(Var("y"))))

str(e3)