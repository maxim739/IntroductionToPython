#Python uses special objects called exceptions to handle wrrors which arise during the program's execution
#If you write code to handle these exceptions the code will continue running, otherwise it would create an error and stop the program
#Exceptions are handled in try-except blocks, which will keep the code running
	#It also tells python what to do when one exception is raised


#Handling he ZeroDivisionError
#Thhis is a simple error that python creates when you try to divide something by zero

#print(5/0)
#Python can't do this, so it sends out an error message
#Based on the error message we can now try and make a try=except block for it


#Using try-exept blocks
#When you think an error might occur you can make a try-except code for it so the code will keep running
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")
#If the code in the try block works, python skips over the except. If it dosen't work then python looks for a block with a matching error code to tell it what to do
#The code after the except block will keep running because python knows how to handle the error


#Using exceptions to prevent crashes
#This is especially important when the code has stuff to do after the error occurs, often when the user is prompted for input
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")
'''
while True:
	first_number = input("\nFirst number:")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
#If you used this code right now, someone could try to divide by zero and it would raise an error, which is why we use the try block
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)'''
#We create the else block in case the error message is not nedded, and it will print the answer

#In the try block we assign the divided value to a variable, and if there isn't an error the variable is printed. If there is an error the text is displayed
#If people know how to look at error messages which display on the screen they could see how your code works and exploit it, so it is good to make code robust
#By using these try-exept blocks the code becomes more robust and user friendly


#Handling the FileNotFOundError Exception
#A file may be in a different folder, you could have mispelled the name, ect. You can write a try-exept block for this
filename = 'text_files/alice.txt'

try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry the file {filename} does not exist. ")
#The encoding argument is used when your system's default encoding dosen't match the file's encoding


#Analyzing text
#Lets anaylze book under public domain
#Lets pull the text of alice in wonderland and count the number of words in the text
#Here we use split() to split up the title of alice in wonderland
title = 'Alice in wonderland'
p = title.split()
print(p)
#The split() method seoerates a string into parts from the spaces and then stores them in a list
#Here we will use the split method on the whole alice in wonderland text
try:
	with open (filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry the file {filename} does not exist. ")
else:
	#Count the number of words in this text
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has {num_words} words. ")


#Working with multiple files
#Here we create a function to handle the bulk of the work
def count_words(filename):
	#Count the number of words in a file
	try:
		with open (filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry the file {filename} does not exist. ")
	else:
		#Count the number of words in this text
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has {num_words} words. ")

filename = 'text_files/alice.txt'
count_words(filename)
#We can write a loop to count the words in any text we want to analyze
#We do this by storing the names of files in a list, and then call count_words on the list
filenames = ['text_files/alice.txt', 'text_files/moby_dick.txt', 'text_files/siddhartha.txt', 'text_files/little_women.txt']
for file in filenames:
	count_words(file)
#The try-except method here is very beneficial because possible errors don't stop the code so the rest of the texts lengths can be found


#Failing Silently
#Sometimes you don't want an error message to pop up
#Then you can use the pass statment

#except FileNotFoundError:
	#pass

#The pass statment also acts as a placeholder
#For example we could write missing filenames to a txt file and we could later read those files
#The pass method basically also can act as a reminder to put somethign in a block later

#You must decide which errors the user sees, whch would be helpful to the user, and which errors would make their experience worse