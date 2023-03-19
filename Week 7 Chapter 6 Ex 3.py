#
## 3. Write the inverse function day_num which is given a day name, and returns its 
## number:
## 
## test(day_num("Friday") == 5)
## test(day_num("Sunday") == 0)
## test(day_num(day_name(3)) == 3) 
## test(day_name(day_num("Thursday")) == "Thursday")
##
## Once again, if this function is given an invalid argument, it should return None:
##
## test(day_num("Halloween") == None)
#

days = [0, 1, 2, 3, 4, 5, 6]



def day_num(number):
    if number ==  "Sunday" : #Sunday
        return days[0]

    elif number == "Monday": #Monday
        return days[1]
    
    elif number == "Tuesday": #Tuesday
        return days[2]    
        
    elif number == "Wednesday": #Wednesday
        return days[3]
    
    elif number == "Thursday": #Thursday
        return days[4]    
    
    elif number == "Friday": #Friday
        return days[5]    
    
    elif number == "Saturday": #Saturday
        return days[6]

    else:
        return None

day_num("Sunday")


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
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num("Wednesday") == 3) #why would day name been in these two locations? They are no longer needed from previous code
    test(day_num("Thursday") == 4)
# -- Main Code ----------------------------------------------------------------

test_suite()        # Here is the call to run the tests
