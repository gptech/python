__author__ = 'jason'
import sys
import time
import random

#Variables

# Just using two choices wasn't random enough so just repeat entries to give it more
#to work with.
vacation = random.choice([True, False, True, False, True, False, True, False])

#Functions

def isweekday():

#Use time module to determine the day of week. If the name of day of week
#is anything besides Sat or Sun return True

    name = (time.strftime("%A"))
    if name == "Saturday" or "Sunday":
        return False
    else:
        return True

def sleep_in(weekday, vacation):

#Pass the parameters true or false for the weekday and vacation day
    if weekday == True and vacation == True:
        return True
    elif weekday == True and vacation == False:
        return False
    elif weekday == False and vacation== False:
        return True
    elif weekday == False and vacation == True:
        return True




def main():
#Main Code


#Find out out if it's a weekday and store it in this variable.
#Pass that and the vacation variable we defined up at the top globally and print the value.
    weekday = isweekday()

    do_we_sleep_in = sleep_in(weekday, vacation)

    print do_we_sleep_in

if __name__ == '__main__':
    sys.exit(main())
