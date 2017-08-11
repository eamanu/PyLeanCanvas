'''
Created on 10 ago. 2017

@author: eamanu
'''

class Item (object):
    
    def __init__(self):
        '''Constructor
        '''
        self.id = None
        self.description
        self.property
        self.edited

class ItemLeanCanvas(object):
    '''
    This is the item Lean Canvas Class. This is the 
    parent of the all items of Lean Canvas.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.itemsDescrip = {}
    
    def writeItem(self, item):
        '''Write the item description in the core
        params
        ------
        item -> string: This is the item to write        
        '''
        
        self.itemsDescrip = item    
    
    def readItems(self):
        '''Read the items descriptions
        params
        ------
        None
        
        Return
        ------
        itemDescriptions -> dict
        '''
        
        return self.itemsDescrip
  
class ItemProblem(ItemLeanCanvas):
    '''This is the item problems
    '''
    def __init__(self):
        '''Constructor
        '''
        
class ItemSolution(ItemLeanCanvas):
    '''This is the item Solution
    '''
    def __init__(self):
        '''Constructor
        '''
class ItemMetrics(ItemLeanCanvas):
    '''This is the item Metrics
    '''
    def __init__(self):
        '''Constructor
        '''
        
class ItemRevenue(ItemLeanCanvas):
    '''This is the item Revenue
    '''
    def __init__(self):
        '''Constructor
        '''
        
class ItemUniqueValues(ItemLeanCanvas):
    '''This is the item UniqueValues
    '''
    def __init__(self):
        '''Constructor
        '''
        
class ItemAdvantage(ItemLeanCanvas):
    '''This is the item Advantage
    '''
    def __init__(self):
        '''Constructor
        '''
        
class ItemChannels(ItemLeanCanvas):
    '''This is the item Channels
    '''
    def __init__(self):
        '''Constructor
        '''
        
class ItemCosts(ItemLeanCanvas):
    '''This is the item Costs
    '''
    def __init__(self):
        '''Constructor
        '''
        
class ItemCustomers(ItemLeanCanvas):
    '''This is the item Customers
    '''
    def __init__(self):
        '''Constructor
        '''
        
