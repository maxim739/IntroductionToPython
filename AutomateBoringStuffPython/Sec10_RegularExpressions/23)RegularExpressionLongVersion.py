# This code will look for phone numbers given to it
# Will see American or Canadian phonenumber format
def isPhoneNumber(text):
    if len(text) != 12:
        return False # The phone number is not the right size
    for i in range(0, 3):
        if not text[1].isdecimal():  # This checks to see that text[i] is not a decimal character
            return False  # This means that there would be no area code
    if text[3] != '-':  # If the 3rd character in string is not a dash
        return False
    for i in range(4, 7): # This checks to see if the next three characters are numbers
        if not text[i].isdecimal():
            return False
    if text[7] != '-': # Check to see if there is the second dash
        return False
    for i in range(8, 12):  # Loop through the last four charcaters
        if not text[i].isdecimal(): # Looks to see if last four characters are numbers
            return False # If they aren't numbers return false
    return True  # Return true if all previous statments are passed not returning False

message = 'Call me at 802-882-1926 or 802-324-0612'
foundNum = False
for i in range(len(message)):  # Looks at each character in the string
    chunk = message[i:i+12]  # Goes through every character in the string and takes a slice
# The slice is that number and the 12 following numbers, and it looks for a phone number in that slice
    if isPhoneNumber(chunk):
        print(f"Phone number has been found {chunk}")
        foundNum = True
        
if not foundNum:  # If there are no isPhoneNumber's returning True
    print("I could not find any phone numbers")
    
# You can make something happen in an if statmnet by using "not" and then the false variable    