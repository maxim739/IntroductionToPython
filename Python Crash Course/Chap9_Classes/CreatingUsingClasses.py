#Classes combine functions and data into one package that can be used in flexible and efficient ways
#They are used in object oriented programs to represent real world things and situations
#When you write a class you define the general behavior that a whole category of objects can have

#Creating and using a class
#Here is a class which represents a dog
#This class will have name and age, as well as the behavoirs of sit and roll over
class Dog:	#In this line we name the class, classes are always uppercase
	"""A simple attempt to model a dog"""	#We write the docstring describing what the class does
	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age
	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(f"{self.name} is now sitting. ")
	def roll_over(self):
		"""Simulate rolling over in response to a command"""
		print(f"{self.name} rolled over! ")

#The __init__() method
#They work like classes, except init calls methods
#In line 10 its used as a special method that python runs when we create a new instance based on the Dog class
#In the dog class we give the class three parameters, and the self parameter is required, and goes before the others
#self has to be included because when dog is called, the method call will pass the self argument, which gives the user acess to the attributes themselves
#When we make an instance of dog, well pass dog and a name and age, and the self is run automatically

#The variables defined at 12 and 13 have the prefix self, which allows them to be used throughout the class
#self.name = name takes the variable assignmed to the parameter name, and assigns it to name
#These are called attributes

#The two other methods dont need any more information, so they only have self, in the future we can make them more complex


#Making an instance of a class
#Think of a class as a set of instructions for how to make an instance
#The class dog is a set of instructions that tells python to make induvidual instances representing specific dogs
#Here is us making one specific dog

my_dog = Dog('Willie', 6)	#Here we tell python to create a dog whos name is willie and whos age is 6

print(f"My dog's name is {my_dog.name}. ")
print(f"My dog is {my_dog.age} years old. ")

#After line 40 python reads this line, calls the init method in dog with the arguments willie and 6
#Then the init function method creates an instance representing the particular dog and the name and age attributes
#Python then retuens that instance and assigns it to my_dog
#Uppercases like Dog are the class, and instances like my_dog are lowercase

#Acessing atributes
#we acess the value of an instance using dot notation
#we can acess it with
	#my_dog.name
print(my_dog.name)

#calling methods
#After creating an instance of dog we can use dot notation to clal and method defined in dog
#Lets make the dog sit and roll over
my_dog.sit()
my_dog.roll_over()
#This method is very useful because its descriptive


#Lets cerate a new instance
your_dog = Dog('Lucy', 3)

print(f"\nYour dog's name is {your_dog.name}. ")
print(f"Your dog is {your_dog.age} years old. ")
your_dog.roll_over()
your_dog.sit()