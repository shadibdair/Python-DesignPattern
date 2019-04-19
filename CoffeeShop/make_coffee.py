import coffeeshop

myCoffee = coffeeshop.Concrete_coffee()
print('Ingredients:' +myCoffee.get_ingredients()+ '; Cost'+ str(myCoffee.get_cost())+';sales tax ='+str(myCoffee.get_tax()))

myCoffee=coffeeshop.Milk(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+';Cost'+str(myCoffee.get_cost())+',sales tax= '+str(myCoffee.get_tax()))

myCoffee=coffeeshop.Vanilla(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+';Cost'+str(myCoffee.get_cost())+',sales tax= '+str(myCoffee.get_tax()))

myCoffee=coffeeshop.Sugar(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+';Cost'+str(myCoffee.get_cost())+',sales tax= '+str(myCoffee.get_tax()))



"""
Output:

Ingredients:coffee; Cost1.0;sales tax =0.1
Ingredients: coffee,milk;Cost1.25,sales tax= 0.125
Ingredients: coffee,milk,vanilaa;Cost2.0,sales tax= 0.2
Ingredients: coffee,milk,vanilaa,sugar;Cost2.0,sales tax= 0.2
"""