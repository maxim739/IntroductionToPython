"""A class which can be used to represent a car"""

class Car:
	"""Simple attempt to represent a car"""

	def __init__(self, make, model, year): 	#Define init method and gave parameters
		"""Initalize descirbing a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 25
	
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

#We create a docstring at the first line which can be used to describe the module

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