#To learn about testing, we will create a code to test on

def get_formatted(first, last, middle=''):
	"""Generate a neatly formatted name"""
	if middle:
		full_name = f"{first} {middle} {last}"
	else:
		full_name = f"{first} {last}"
	return full_name.title()

print("Enter 'q' at any time to quit")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("\nPlease give me your last name: ")
	if last == 'q':
		break

	formatted_name = get_formatted(first, last)
	print(f"neatly formatted name: {formatted_name}. ")

#If we wanted to add another function to handle middle names, we would want to test every possibility, which would take a while
#Thankfully we can automate this using python


#Unit tests and Test Cases
#The unittest module from python has a library of different tools for testing your code
#A unit test verifies that one specific aspect of a function's behavior is correct
#A test case is a collection of unit tests which prove a function is beving the way its supposed to
#A good test case considers all possible inputs for a function, and provides full coverage of all possibilities


#A passing test
#To write a test case for a function, import the unittest module and create a class which inherits from unittest.TestCase

#You can import a function using the syntax
#from title_file import function_name
import unittest

class NameTestCase(unittest.TestCase):	#Here we create a class which will contain a lot of unit tests for get_formatted
	"""Tests for name_function.py"""	#Its best to name the class something related to the function your about to test, and use the word 'test'
										#This class must inherit from the class unittest.TestCase so python knows how to run the tests you write
	def test_first_last_name(self):
		"""Do names like Janis Jophelin work"""
		formatted_name = get_formatted('janis', 'joplin')	#We call get_formatted on janis joplin and assign the result to formatted_name
		self.assertEqual(formatted_name, 'Janis Joplin')		#Here we use the unittest's more useful featrures, the assert method, to verify you recieved matches from the result you expected
														#Basically we test to see if the answer we get is the same as the one in the single quotes
														#The assertEqual() method will test if we get the value "Janis Joplin", if they aren't equal, let me know
	def test_first_last_middle(self):
		"""Do middle name names work?"""
		formatted_name = get_formatted('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':	#This watches if the file is being run as the main program, if it is the value of '__name__' is set to '__main__'
	unittest.main()		#Here we call unittest.main() to run the test case. When the testing framework runs the file, the value of __name__ won't be __main__ and the block will not be exectued


#The class must inherit from the class unittest.TestCase
#NamesTestCase contains a single method that tests one aspect of get_formatted, and we call it test_first_last_name() becauswe they verify that the names are formatted correctly

#Any method that starts with test_ will automatically when we run test_name_function.py

#Here we run the file directly, but many testing networks import test files before running them
#When a file is imported, the interpreter executes the file as its being imprted 

#The if block looks at the special variable __name__ which is set when the program is executed
	#If this file is being ran as the main program, the value of __name__ is set to __main__
#Here we call the unittest.main() method to run the test case
	#When a testing framework runs a file, the value of __name won't be '__main__' and the block won't be executed

#If the tests are succesful we get an output showing "OK"
#Now we know that this test will work for all names which have a first and last name, like Janis Joplin


#A failing test
#Here we will modify get_formatted() so that it handles middle names, but we will do it in a way which breaks the function for names like Janis Joplin
#now we edit the function 
"""def bad_get_formatted(first, middle, last):
	""This function will give a neatly formatted full name""
	full_name = f"{first} {middle} {last}"
	return full_name.title() """

#Here we run the test on the new function which should return a bad test

#The "E" in the failed test tells us that one of the unit tests in the test case resulted in an error
#In the second section we see that test_first_last_name() in NamesTestCase caused the error, which is helpful when you run a lotr of unit tests
#In the trhird section we see the standard traceback, showing that the function call get_formatted('janis', 'joplin') won't work because it is missing a positional argument
#In the fourth section we see that one unit test was run
#Finally we see that the overall test case failed and that one error occured when running the test case
	#All this info is made to make it easy for you to see what is wrong and what you need to fix


#Responding to a failed test
#When the error message pops up you can see what you are missing
#Now because of the message we know we are missng a third option that is required for the function, now we should just make the middle name optional
#Now we edit the code
"""
def get_formatted(first, last, middle=''):
	if middle:
		full_name = f"{first} {middle} {last}"
	else:
		full_name = f"{first} {last}"
"""
#Now the middle name is optional, and now the function should work for functions like 'Janis Joplin'
#Now trhe test returns as fully "OK"



#Addign new tests
#Now we know that get_formatted() works for simple names, we can test for people who include a middle name
#Now we add another method to NamesTestCase
'''
class NamesTestCase(unittes.TestCase):
	"""Test for name_function.py"""
	def test_first_last_middle(self):
		"""Do middle name names work?"""
		formatted_name = get_formatted('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
'''
#We name this with test_ in front so it runs automatically when we run test_name_function.py
#We name the method so that it represents what we are testing
	#Its fine to have long names here because we are tryng to be as specific as possible

#To test, we get get_formatted() with a first, last, and middle name and use assertEqual to test if we get the output we want
#Now two tests will be ran
	#And we know this function will work for names like Janis Joplin and Mozart Amaedus Motzart
	