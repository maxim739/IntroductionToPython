#The python standard library is a library of standard python modules which are downloaded when python is installed
#The first module we can use is randint
from random import randint
x = randint(1, 6)
print(x)

#Another helpful one is choice() which takes in a thuple or list and outputs a randomly selected chosen element
from random import choice
players = ['charles', 'marina', 'bob', 'rob', 12]
first_up = choice(players)
print(first_up)

#The random module shouldn't be used for security related projects, but it is good for fun things