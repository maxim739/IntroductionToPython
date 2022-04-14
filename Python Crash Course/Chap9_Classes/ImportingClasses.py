#You can import classes from other modules to keep your main code neat

#Importing a single class
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(50)
my_new_car.get_odometer()

#This a very effective way to program because it makes the main code a lot shorter


#Sorting multiple classes in a module
#You can store as many classes as you want in a module, although they should all be related
#The classes Battery and ElectricCar both surround cars,so we can add them to the car.py module
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#Importing multiple classes from a module
#You can import as many classes as you need into a program file
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
my_tesla2 = ElectricCar('tesla', 'roadster', 2019)
print(my_beetle.get_descriptive_name())
print(my_tesla2.get_descriptive_name())
#You can import multiple classes by using a comma to seperate the classes from the same file

#IMporting an entire module
#You can import an entire module by using import file_name
import car


#Importing all classes from a module
	#From module_name import *
from car import *
#This method is not recommended because you can't see what classes you just imported, which leads to confusion
#It is better to import the entire module and use the module_name.ClassName stntax


#Importing a module into a module
#You might want to use this when you have multiple files and one module depends on another in a different module
#Here is a representation of the cars module when you do this
	#from car import Car
	#class Battery
	#class ElectricCar(Car)
#We can create a child class because the parent class is refrenced in this module at the top, otehrwise there would be an error message


#Using aliases
#sometimes you will want to use an alias to keep code simple

from car import ElectricCar as EC

my_tesla3 = EC('tesla', 'model 3', 2019)
print(my_tesla3.get_descriptive_name())


#The more you code the better you will find your workflow, which will make coding more streamlined the more that you do it.
