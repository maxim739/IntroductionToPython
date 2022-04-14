#The car class, this will store information and have a method to summarize it
class Car:
	"""Simple attempt to represent a car"""

	def __init__(self, make, model, year): 	#Define init method and gave parameters
		"""Initalize descirbing a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0
	
	def get_descriptive_name(self):		#Define a method to put the model, make, and year in a single string
		"""Return formatted description"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def get_odometer(self):
		"""Print statment to get car's milage"""
		print(f"This car has {self.odometer} miles on it. ")

	def update_odometer(self, milage):
		"""Update the odometer"""
		"""Reject rolling the milage back"""
		if milage >= self.odometer:
			self.odometer = milage
		else:
			print("\nYou can't roll back an odometer! ")

	def incriment_odometer(self, x):
		"""Add the given amount to the odometer reading"""
		self.odometer += x


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

#Setting a default value for an attribute
	#When an instance is created, some attributes don't have to be defined, and are defined in the init method
	#This is why the attribute called odometer reading is in the self method without beign a parameter

	#We also make a method to call the odometer reading
my_new_car.get_odometer()
#In the next step we are going to change the milage


#Modifying attribute values
#You can do this three ways
	#change the value direct through instance
	#Set the value through a method
	#Incriment the value through a method

#Modifying an attribute's value directly
my_new_car.odometer = 23
my_new_car.get_odometer()

#Modifying an Attribute's Value through a method
	#Here we create a method called update_odometer
my_new_car.update_odometer(49)
my_new_car.get_odometer()

#I also extended the function so that you can't subtract milage
my_new_car.update_odometer(40)
my_new_car.get_odometer()


#Incriment an attribuite's value through a method
#We use this when we want to incriment by a certain value rather than change to a completley new value
#Add def incriment_odometer(self, miles):
#This method takes in the amount of miles and adds the value to the self.odometer reading
my_used_car = Car('subaru', 'outback', '2015')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.get_odometer()

my_used_car.incriment_odometer(100)
my_used_car.get_odometer()