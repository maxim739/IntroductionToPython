#Stripping WhiteSpace
#rstrip() strips space from the right side
favorite_lang = "Python "
print(favorite_lang)
print(favorite_lang.rstrip())
#To remove Whitespace permenantly, you have to make it a new variable
fav_lang = favorite_lang.rstrip()
#You can also strip from the left side with lstrip()
#Strip from both sides using strip()