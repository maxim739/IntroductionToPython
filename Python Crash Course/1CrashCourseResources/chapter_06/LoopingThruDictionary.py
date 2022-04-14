user0 = {'usernames': 'efermi',
	'first': 'enrico',
	'last': 'fermi',}
for key, value in user0.items():
	print(f"\nKey: {key}")			#Use the for loop to loop through all value in dict
	print(f"Value: {value}")		#Print the key value, and then the value
#You could use any letter to replace the key, value in the first part of the for loop
#The second part is the name of the dict, followed by items() which returns a list of key value pairs

fav_lang = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name, lang in fav_lang.items():
	print(f"\n{name.title()}'s favorite language is {lang.title()}.")

#You can also loop through all the keys in a dictionary
for name in fav_lang.keys():	#This line telsl python to pull keys from fav_langs and assign them to the variable "name"
	print(name.title())			#Looping through jeys is default when oython is told to loop through a list

for name in fav_lang:			#This is the same output as before
	print(name.title())			#You might want to include keys to make you rcode easier to read

#You can also access the value associated with any key you want by using the current key
#In this next loop it will only print their favorite language when its one of our friends

friends = ['phil', 'sarah']		#Here we make a list of people who are our friends, who we want to make a message for
print("\n")
for name in fav_lang.keys():	#Here inside the loop we print each person's name
	print(f"Hi {name.title()}")
	if name in friends:			#If their name matches one in the list, if it is we determine their fav language using their name as a key
		language = fav_lang[name].title()	#Here is where we acess the value from using their name as a key and then add it to variable language
		print(f"\t{name.title()}, I see you love {language}!")

#You can also use the keys() method for more than looping
#It can also return just all keys
if 'erin' not in fav_lang.keys():
	print("\nErin, please take out poll!\n")

#Looping through dictionaries in a particular order
#Usually in python the dictionary returns items in the same order they were inserted
#One way to change the order is to sort the keys returned in a for loop, and use sorted() to get them in order
for name in sorted(fav_lang.keys()): #This is the same as the the other sor statments, except that the sorted function is wrapped around the dictionary.keys()
	print(f"{name.title()}, thank you for taking the poll.")	#This loop tells python to list all keys in the dict, and then sort the list before looping it

#You can also loop through just the value in a dictionary
print("\nThe following languages have been mentioned:")
for language in fav_lang.values():	#The for statment pulls each value and assigns it to the variable language
	print(language.title())			#When the variables are printed, we get a list of all chosen languages
#This method prints all keys, without checking for repeats, which would be terrible in a larger data set
#To see languages without repitition, set(0) is used
print("\nHere they are without repeats:")
for language in set(fav_lang.values()):
	print(language.title())
#When you wrap set around a list that contains duplicate items, python identifies unique items and builds a set from those items
#In line 55 set is used to pull unique languages from fav_lang.values(). The repult is a list of nonrepetitive languages mentioned

#You can also build a set with brackets and commas seperating the items
lang = {'python', 'c', 'ruby', 'c', 'python'}
print("\n")
print(lang)
#These sets do not retain values in any specific order
#If you see brackets and no values, then it is a set