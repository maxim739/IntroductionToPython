#Functions are named blocks of code which are designed to do one specific job
#When you want to preform a specific task, you can call the function to do it
#This is helpful when you want to preform the same segment of code over and over without typing it all over again
#You can also store functions in seperate files called modules, which help organize your main prigram files

#Here is a simple function named greet user, which prints a greeting
def greet_user():	
	'''Display a simple greeting'''
	print("Hello")
greet_user()
#In line 7, keyword def tells python that you are defining a function
	#Def tells python the name of the function, and somtimes which information is needed for the function
#The indented segments after are the body of the function
	#Line 8 is a docstring, which in enclosed in triple quotes, this tells what the function does, and python uses it to generate documentation for functions in your program
	#Line 9 is the only actual segment of code, which prints the word "Hello"
#You then need to call the function, which is done by just calling it like it is in like 10, because there is no other necessary information


#Passing information to a function
#Here we are going to modify the function to not only say hello, but greet the user
def greet_user1(username):	#We modify so that the function can take a variable
	"""Display another greeting"""
	print(f"Hello {username.title()}! ")	#We can use that variable inside of the function
greet_user1('jesse')	#We can call the function by also supplying a string as that variable


#Arguments and paramters
#In the prevoius example the "username" in parenthesis is a parameter, which is a variable needed for the function to work
#The value of 'jesse' in greet_user1('jesse') is an argument. This is a piece of information passed from a function to call a function