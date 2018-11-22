# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 13:12:56 2018

@author: Nathan


 def create_truth_table(n, var_dict, tautology = 0, truths=[]):
        # Base case where n = 0, have also included some things that allow 
        # it to do my taut checking for me.
        
        if not n:
        # this creates the key value parings and prints the truth table.
        
        for truth, key in zip(truths, var_dict):
                var_dict[key] = truth
                if not tautology:
                    store = ("{} \t|".format(truth),end="")
        
        if not tautology:
            # evaluates the key:value pair of this itteration and prints it
                print (self.eval(var_dict))
            if not self.eval(var_dict):
                self.taut_flag = 0
      
        
        # recurs until we hit the max lenght of the variable list.
        else:
            for i in [True,False]:
                self.create_truth_table(n-1,var_dict,tautology,truths+[i])



def make_tt(self,tautology = 0):
        # make the variable and dictionary needed for the table
        bool_dict = {}
        expresion_variables = self.make_list(self.variable_walk_down())
        Truthtable_string = ""
        for var in expresion_variables :
            bool_dict[var] = ""
            if not tautology:
                Truthtable_string = Truthtable_string + ("{} \t|".format(var),
                                                         end=' ')
        if not tautology:
            print ("{}".format(self.bound_str(0)))
        self.create_truth_table(len(tt_var),bool_dict,tautology)
        return ""                
"""                
                
def create_truth_list(n, m, truths=[]):
    if not n:
        m[:] = m + [truths]
    else:
        for i in [True, False]:
            create_truth_list(n-1, m, truths+[i])
            
bool_table = []
var_dict = { "A": "",  "B":"", "C" : "", "D" : ""}

def draw_truth_table(table = bool_table,dictionary = var_dict):
    truth_table = ""
    # create dictionary
    create_truth_list(len(dictionary),table)
    # create the header
    for keys in var_dict:
        truth_table = truth_table + "{} \t|".format(keys)
    truth_table = truth_table + "str function.\n"
    # for each line go through each varabile and asign it to a dict
    # then evaluate that dict and append it to the valid line
    for lines in bool_table:
        for key,boolian in zip (var_dict, lines):
            var_dict[key] = boolian 
        lines = lines.append("Evaluation Value")
    # for each valid line in the list append that 
    for lines in bool_table: 
        for valules in lines:
            truth_table = truth_table + "{} \t|".format(valules)
        truth_table = truth_table + "\n"
    return truth_table

print(draw_truth_table(bool_table,var_dict))    