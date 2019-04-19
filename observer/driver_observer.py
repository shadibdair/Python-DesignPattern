from observer1 import Publisher, Subscriber

pub = Publisher() # Initialized Publisher
'''
we have initialized 3 subscriber with specified name
'''
bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch("It's lunchtime!")

pub.unregister(john)
pub.dispatch("Time for dinner ")

'''
output

Alice got message"It's lunchtime!"
John got message"It's lunchtime!"
Bob got message"It's lunchtime!"
Alice got message"Time for dinner "
Bob got message"Time for dinner "
'''