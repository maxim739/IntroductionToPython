#You can use while loops to loop through something while a condition is met
current_num = 1
while current_num <= 5:
	print(current_num)
	current_num += 1
#Every time the code loops through the while loop it adds 1 to current_num
#Make sure that thje while loop wont run forever or you might crash your computer

#Here is a code using user input and while loops, which allows the user decide when to quit
prompt = "Tell me something you want to be repeated to you:"
prompt += "\nEnter 'quit' when you want to end the program: "

message = ""	#This variable keeps track of whatever value the user enters
while message != 'quit':	#This loop runs whenever the value is not 'quit'
	message = input(prompt)
	if message != 'quit':	#This line makes sure the code dosen't print the quit message
		print(message)