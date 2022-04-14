#Unlike break, continue will return to the beginning of a loop without exiting entirley
#This loop goes through range 1-10, but only prints odd numbers
current_num = 0	#Set to 0 because it is less than 10
while current_num < 10:		#While the current_num is less than 10 go through loop
	current_num += 1		#Add one to the current num
	if current_num % 2 == 0:	#Check to see if the number is even or odd
		continue	#If even, start at the top of the while loop, its key that the 1 has been added to current_num
	print(current_num)	#Print current_num