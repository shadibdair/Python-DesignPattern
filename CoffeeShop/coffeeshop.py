import six
from abc import ABCMeta

@six.add_metaclass(ABCMeta)
class Abstract_Coffess(object):

    def get_cost(self):
        pass
    def get_ingredients(self):
        pass
    def get_tax(self):
        return 0.1*self.get_cost()
    

class Concrete_coffee(Abstract_Coffess):
    def get_cost(self):
        return 1.00
    def get_ingredients(self):
        return 'coffee'

@six.add_metaclass(ABCMeta)

class Abstract_Coffess_Decorator(Abstract_Coffess):
    def __init__(self,decorted_coffee):
        self.decorted_coffee=decorted_coffee
    def get_cost(self):
        return self.decorted_coffee.get_cost()
    def get_ingredients(self):
        return self.decorted_coffee.get_cost()

class Sugar(Abstract_Coffess_Decorator):
    def __init__(self,decorted_coffee):
        Abstract_Coffess_Decorator.__init__(self,decorted_coffee)
    def get_cost(self):
        return self.decorted_coffee.get_cost()
    def get_ingredients(self):
        return self.decorted_coffee.get_ingredients() + ',sugar'

class Milk(Abstract_Coffess_Decorator):
    def __init__(self,decorted_coffee):
        Abstract_Coffess_Decorator.__init__(self,decorted_coffee)
    def get_cost(self):
        return self.decorted_coffee.get_cost()+0.25
    def get_ingredients(self):
        return self.decorted_coffee.get_ingredients()+ ',milk'

class Vanilla(Abstract_Coffess_Decorator):
    def __init__(self,decorted_coffee):
        Abstract_Coffess_Decorator.__init__(self,decorted_coffee)
    def get_cost(self):
        return self.decorted_coffee.get_cost()+0.75
    def get_ingredients(self):
        return self.decorted_coffee.get_ingredients()+',vanilaa'