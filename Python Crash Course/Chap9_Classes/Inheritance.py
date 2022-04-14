#You don't always have to start from scratch when writing a new class. If a new class is a specialized version of the old one you can use inheritance
#The new class can inherit attributes and methods from another class 
#The origional class is called a parent class and the new one is called a chile class
#The child class can inherit any attibutes from the parent class and make up it's own attributes and methods

#Using the __init__() method for a child class
#You will often want to call the init method from the parent so you can initialize everything and make them avaliable in the child class
#In this example we will model an electric car, which can be based on the previous car class
#This way we only need to write new attributes for electric cars in this class
class Car:	
	"""A simple attempt to represent a car"""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it")

	def update_odometer(self, milage):
		if milage >= self.odometer_reading:
			self.odometer_reading = milage
		else:
			print("You can't roll back an odometer!")

	def inciment_odometer(self, miles):
		self.odometer_reading += miles

	def fill_gas_tank(self):
		print("The gas tank is filled")

class Battery:
	"""A simple attempt to model the battery of an alectric car"""
	def __init__(self, battery_size = 95):
		"""Initialize battery attributes"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print statment about battery size"""
		print(f"This car has a {self.battery_size}-kWh battery in the battery class. ")

	def get_range(self):
		if self.battery_size == 95:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"\nThis car has a range of {range} miles. ")

class ElectricCar(Car):
	"""Represents aspects of a car, but for electric vehicles"""
	def __init__(self, make, model, year):
		"""Initialize attribute of a parent class"""
		super().__init__(make, model, year)
		self.battery_size = 75
		self.battery = Battery()

	def describe_battery(self):
		"""Print statment describing battery size"""
		print(f"This car has a {self.battery_size}-kWh battery")

	def fill_gas_tank(self):
		print("This electric car dosen't have a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

#At line 10 we create the parent class which must be in the same file as the child class, and must appear before
#At line 56 define the child class Electric car, and the parent class must be in parenthesis
#The info in the __init__ method takes the information required to make a Car instance
#The super() function at 60 allows you to call a method from a parent class
	#This line tells python to call the __init__ method from the Car class
#We test this when we call the elctric car class to make a new instance and assign it to a variable

#Defining attibutes and method for the child class
#You can add other attributes which make the child seperate from the parent
#Here we will add battery size and a method which prints out a description of a battery
my_tesla.describe_battery()
#At line 61 we add a new attribute of self.battery_size and set it to 75
	#This instance will be associated with Electric car class, but not the Car class
#At line 64 a new method is created which prints info about the battery

#Overriding methods from the parent class
#You can override any method from the parent class which dosen't fit in the child class.
#You do this by defining a methd in the child class with the same name as the one in the parent class, python will override the parent method and go with the child one
my_car = Car('dodge', 'ram', 1998)
my_car.fill_gas_tank() 		#Here this is an instance which uses the Car parent class, so the gas tank can be filled

my_tesla.fill_gas_tank() 	#Because this method was overwritten in the Electric car class, when we call this in the child class it is a new method

#Instances as Attributes
#When we add a lot fo instances and attribute, the code can get lengthy, so we want to split that up
#We casay we have a lot of battery attributes, we can create a new class Battery and use a Battery instance as an attribute to an electric car class
my_tesla.battery.describe_battery()
#AT line 38 we create a new battery class
#This class doesn't have any parameters except self and a set battery size
	#Because battery_size is already defined it is at size 75 unless another value is provided
#The method describe_battery is also moved to this class
#In the ElectricCar class we also add an attibute called self.battery 
	#This line tells python to create a new instance of Battery and assign it to self.battery
	#This happens every time the __init__ method is called 
#When we create a new electric car and assign it to my_tesla, in order to describe the battery we need to work throught the battery attribute
	#my_tesla.BATTERY.describe_battery()
#That line tells python to look at the instance my_tesla, find it's battery attibute, and call the method describe_battery thats associated with the Battery instance outside of the attribute
#This is a lot of extra work, but now the ElectricCar class is not cluttered
#For example I added the range method
my_tesla.battery.get_range()


#A syou get more advanced it becomes harder to see where to put different methods