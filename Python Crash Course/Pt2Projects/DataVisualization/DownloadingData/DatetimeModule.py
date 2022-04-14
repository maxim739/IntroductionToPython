from datetime import datetime

first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(first_date)

# The first argument contains the date we want to interpret
# The sacond argument shows how the first argument is formatted
# %Y is the 4 digit yes
# %m is the month from 01 to 12
# %d is the number day from 01 to 31

# %A is the weekday name, like 'Monday'
# %B is the month name, like 'January'
# %m is the month as a number frp, 01 to 12
# %d is the day as a number, from 01 to 31
# %Y is a four digit year, as in 2019
# %y is the two digit year, as in 19
# %H is the hor in a 24 hour format (00 - 23)
# %I is the hour, in a 12 hour format (01 - 12)
# %p is am or pm
# %M is minutes (00 - 59)
# %S is seconds (00 - 61)
