'''
Created on 10 ago. 2017

@author: eamanu
'''
from itemleancanvas import *

class LeanCanvas (object):
    '''Lean Canvas is the principal module that connect all client and
    save data about the lean canvas items
    '''
    
    def __init__(self):
        '''constructor
        '''
        self.Problem = ItemProblem() # Problem Instance
        self.Solution = ItemSolution() # Solution instance
        self.Metrics = ItemMetrics() # Metrics Instance
        self.Revenue = ItemRevenue() # Revenue Instance
        self.UniqueVaule = ItemUniqueValues() # Unique Values instance 
        self.Advantage = ItemAdvantage() # Advantage instance
        self.Channels = ItemChannels() # Channels instance
        self.Costs = ItemCosts() # Costs instance
        self.Customers = ItemCustomers() # Customers Instances
        
    def writeProblem(self, problem):
        '''
        Method that write a problem item
        
        Parameter
        ---------
        problem -> String: This is the problem to add to the list
        '''
        self.Problem.writeItem(problem)
        
        