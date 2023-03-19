# 
## 6. Write a function days_in_month which takes the name of a month, and returns the
## number of days in the month. Ignore leap years:
## 
## test(days_in_month("February") == 28)
## test(days_in_month("December") == 31)
## 
## If the function is given invalid arguments, it should return None.
#

days = [28, 30, 31]

def days_in_month(month):
    if month ==  "January" : 
        return days[2]
    elif month == "February": 
        return days[0]
    elif month == "March": 
        return days[2]         
    elif month == "April": 
        return days[1]  
    elif month == "May": 
        return days[2]     
    elif month == "June": 
        return days[1]     
    elif month == "July": 
        return days[2]
    elif month == "August": 
            return days[2] 
    elif month == "September": 
            return days[1]
    elif month == "October": 
            return days[2]
    elif month == "November": 
            return days[1]
    elif month == "December": 
            return days[2]
    else:
        return None
    

#double check I didn't set the days wrong

print (days_in_month("January"))
print (days_in_month("February"))
print (days_in_month("March"))
print (days_in_month("April"))
print (days_in_month("May"))
print (days_in_month("June"))
print (days_in_month("July"))
print (days_in_month("August"))
print (days_in_month("September"))
print (days_in_month("October"))
print (days_in_month("November"))
print (days_in_month("December"))

#Unit Testing

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

# -- Our function -------------------------------------------------------------
# Code your function here . . .

def test_suite():
    """ Run the suite of tests for code in this module (this file). """
    # You add code here for each test suite.
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)

# -- Main Code ----------------------------------------------------------------

test_suite()        # Here is the call to run the tests
