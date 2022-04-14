# Match a certin number of repititions of the group
# If you want to match the group only five times, or only if the number is more than 3, etc
# Here we learn how to match for a specific number of repititions
import re

batRegex = re.compile(r'Bat(wo)?man')
# The (wo)? means that the (wo) group can appear once or not at all and still recognize it
# ? says to match the preceding group 0 or 1 times, appear once or not at all
mo = batRegex.search('The adventures of Batman') # Here it dosen't appear
mo2 = batRegex.search('The adventures of Batwoman') # Here it appears once
mo3 = batRegex.search('The adventures of Batwowoman') # Here it dosen't match because it happens more than once
print(mo.group())
print(mo2.group())
try:
    print(mo3.group())
except AttributeError:
    print("Batwowoman dosen't work")
    
# Now we see how to use it on regex
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo4 = phoneRegex.search('My phone number is 555-555-5555')
print(mo4)
phoneRegex2 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # Now it works with and without an area code
mo5 = phoneRegex2.search('My phone number is 555-5555')
print(mo5)

# If you want to have a question mark in your text, use \? like re.compile(r'dinner\?')
