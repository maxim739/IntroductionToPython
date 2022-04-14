#With writing to a file you can save data when the program stops running and can access it later, very good for storing data
#To write to a file you need to open it with open() and then use a signifier to show that you want to write to that file
#We will print something to a file instead of printing to screen
filename = 'text_files/writeto.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming!")
#The open() has two arguments, one is still the name of the file we want to open, and the other is the 'w' which tells python to open the file in write mode
	#You can open a file in many modes
		#'r' is read mode
		#'w' is write mode
		#'a' is append mode
		#'r+' allows you to read and write to a file
#The open function will automatically create a file if it dosen't already exist
	#Be careful before opening a file in write mode, because if the file dosen't exist it will erase the contents fo the file before returning it
#file_object.write() adds the text in parenthesis to the file

#In python you can only write strings to files, so you will have to convert intigers to strings with str()


#Writing multiple lines
#Python dosen't add newlines to text, so if you print without the use of \n the text will all be on the same line
with open(filename, 'w') as file2_object:
	file2_object.write("I love programming! \n")
	file2_object.write("I love creating new games! \n")
#You can also use other formatting command similar to \n, like tab characters and blank lines to format your text


#Appending to a file
#This will add text to an already existing file instead of erasing the text already on it
#If the file doen't exist python will create it for you
with open(filename, 'a') as file3_object:
	file3_object.write("I also love creating meanig in data! \n")
	file3_object.write("I love creating apps which run in the browser! \n")