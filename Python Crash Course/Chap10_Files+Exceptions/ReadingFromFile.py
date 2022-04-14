#Read an entire file
#Read from the file pi_digits the first few digits of the pi sequence
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents)

#In the first line, the open() function opens the file, which you need to do before you can do any work on it. 
	#Python looks in the same directory where it is being stored, and then returns an object representing pi_digits
	#Python also assigns that object to the name file_object
#The keyword with closes the file once access to it is no longer needed
#Notice how we opened the file, but didn't close it
	#We could close() it but we don't do this because a bug could cause it to never close
	#It also could close to early, which would come back with lots of errors.
#Its not always easy to know when you should close a file, but trust python will close it when it is done using it
#Once we have the object representing pi_digits, we can read the entire contents of the file and print the value of it's contents

#The only dfference between the output and the origional is that the output has an extra line of space as a string
	#we can remove that by using rstrip()
print(contents.rstrip())


#File paths
#Sometimes you will want to store code in a different area than your text files, so you will have to navigate to them relative to where your code is stored
	#Use with open('folderName/fileName.txt') as file_object: syntax
with open('text_files/file1.txt') as file1_object:
	contents1 = file1_object.read()
print(contents1.rstrip())

#Windows uses a \ for file paths, but coding uses a /
#You can also tell python exactly where your file is stored in your computer regardless of where your code is being stored
	#You can find the absolute file path and assign it to a variable, it is longer but more descriptive
filepath = 'C:/Users/dejon/Documents/other_files/otherfile.txt'
with open(filepath) as file2_object:
	contents2 = file2_object.read()
print(contents2)


#Reading line by line
#How to examine each line of a file
	#This can help you scan through lines and interact with any line that reads 'sunny' in a weather data file
#We can usea loop on the file object to examine the lines of a file one at a time
filename = 'pi_digits.txt'

with open(filename) as file3_object:
	for line in file3_object:
		print(line)

#At line 44 we assign the name of the file to a variable 'filename' this is common when working with files because 'filename' dosent represent an actual file
	#it just tells python where to find the file
#At line 46 with open() an object is assigned to the text is assigned to variable file3_object
#At line 47 each line of the file is examined by looping through each line

#There are blank lines in the print
#We can solve this by using rstrip() like we did previously

#The blank lines appear because an invisible newline is added at the end of each line printed


#Making a list of lines from a file
#when you use with, the file object is only avaliavble inside the with block that contains it
#You can save the file's lines outside of the block, and access parts induvidually
file2name = 'pi_digits.txt'

with open(file2name) as file4_object:
	lines = file4_object.readlines()

for line in lines:
	print(line.rstrip())

#At line 68 the readlines() method takes each line from the file and stores it in a list, then the list is printed out in the for loop


#Working with a file's contents
#Once the file si given to your memory, you can do what you want with it
#Here we are going to move it to one line without any whitespace
pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#Use strip instead of rstrip to get rid of all spaces to the rigt and left of the string
#All data from a file is as a string, so it will need to be converted into a number using int() or float()


#Large Files: One Million Digits
#We are going to print the first 50 digits of pi to the 1,000,000 decimal place
file3name = 'text_file/pi_million_digits.txt'

with open(file2name) as file5_object:
	lines1 = file5_object.readlines()

pi2_string = ''

for line in lines1:
	pi2_string += line.strip()

print("\n")
print(f"{pi2_string[:52]}...")
print(len(pi2_string))

#There is no limit to the amount of data python will go through, it is a matter of your memory storage


#Finding characters in a file
#We will try to find my birthday in the first 1,000,000 digits of pi
birthday = input("Input your birthday in form mmddyy: ")
if birthday in pi_string:
	print("your birthday was in the first million digits of pi!")
else:
	print("your birthday was not in the first million digits of pi.")