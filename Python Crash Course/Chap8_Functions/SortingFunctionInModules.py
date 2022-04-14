#The advantage of functions is that they seperate blocks of code from your main code so it is easier to follow
#Storing your code somewhere else allows you to do more high end logic easier
#Modules allow you to share functions, and you can use libraries which otehrs have written

#Here is how to import an entire module
#This module contains the function make_pizza()
#The function is in a file called PizzaModules.py
import PizzaModules		#Here we import the file from the same directory

PizzaModules.make_pizza(16, 'pepperoni')
PizzaModules.make_pizza(24, 'mushroom', 'extra cheese')

#This is the first approach to importing, where we write import, followed by the name of the module
#If you use this method you only have to do 
	#module_name.function_name()
#You can also import a specific function from a module
	#from module_name import function_name
#You can use this method and import as many functions as you want from the same module as long as they have a comma
	#from module_name import function0, function1, function2
#With this syntax we don't need to use dot notation because its specific which function we want


#Using as to give a function an alias
#Sometimes the name of the module is too big or conflict with another name, so you can use an abbreviation
#Here we give make_pizza an alias "mp" by importing it as mp
from PizzaModules import make_pizza as mp

mp(16, 'pepperoni')
mp(69, 'extra cheese')

#The general syntax is 
	#from module_name import function_name as fn


#Using as to give a module an alias
#This is similar to what we did to the function
#This is often more concise
import PizzaModules as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(30, 'nothin')

#The general form for this is
	#import module_name as mn


#Importing all functions in a module
#You can tell python to import all functions by using an asterix
from PizzaModules import *

make_pizza(16, 'pep')
make_pizza(12, 'less')

#Here you import all modules, this isn't best in bigger modules that you didn't write because you can get mixed up
#It is usually better to be specific so you don't get lost in code

#The general form is
	#from module_name import *


