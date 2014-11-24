__author__ = 'jason'
import sys
import random

#Make a class for the monkey with a method to randomly determine if it's smiling.
class Monkey(object):
    def is_it_smiling(self):
        return random.choice([True, False, True, False, True, False, True, False])


#Make Two Seperate Monkey Objects
MonkeyA = Monkey()
MonkeyB = Monkey()


# Figure out if monkey A and B are smiling and store them in values
MonkeyA_Smile = MonkeyA.is_it_smiling()
MonkeyB_Smile = MonkeyB.is_it_smiling()


#Compare the values pulled above and return a value to determine if we're in trouble.
def are_we_in_trouble(MonkeyA_Smile, MonkeyB_Smile):
    if MonkeyA_Smile == True and MonkeyB_Smile == True:
        return True
    elif MonkeyA_Smile == False and MonkeyB_Smile == True:
        return False
    elif MonkeyA_Smile == True and MonkeyB_Smile == False:
        return False
    elif MonkeyA_Smile == False and MonkeyB_Smile == False:
        return False


well_are_we = are_we_in_trouble(MonkeyA_Smile, MonkeyB_Smile)

print well_are_we