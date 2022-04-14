# Now we will find more powerful pattern finding tools
import re
phoneNumRegex = re.compile(f'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 802-882-8822')
mo.group()
print(mo.group())

# Now we will try to just find a group of the pattern
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('My number is 415-555-4242')
print(mo2.group())
# This dies the same thing as before, but splits the pattern into groups
print(mo2.group(1))
# This just prints the firts part of the pattern which was in the parenthesis
print(mo2.group(2))
# This prints all of the numbers in the pattern which were a part of the second group
# In regular expressions parenthesis mark where the group begins and ends
# If you want to find literal parenthesis in your text use parenthesis in the raw string
phoneNumRegex3 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo3 = phoneNumRegex3.search('My number is (415) 555-4242')
print(mo3.group())

# Now we will use pipe characters | to match any strings that all have one unqiue prefix
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo4 = batRegex.search('Batmobile lost a wheel')
print(mo4.group())
# Here we find that batmobile is bat+mobile and we make it a pattern that we print
mo5 = batRegex.search('Batmotorcycle lost a wheel')
if mo5 == None:
    print("There is no batmotorcycle")
# This will return 'None' because this string concoction is not in the sting given
# If the search method can't find the Regex pattern you are looking for, it is going to return 'None'
print(mo4.group(1))
# If we want to find out which suffix was found, we pass 1 to the group method, and it will find the suffix


# Recap:
# Groups are created in regex strings with parentheses
# Thr first set if group one, the second is group two...
# Calling group() or group(0) returns the full matching string, and group(1) returns group 1's matching string and so on
# Use \(and\) to mathc literal parenthesis in the regex string
# The | can match one of the many possible groups