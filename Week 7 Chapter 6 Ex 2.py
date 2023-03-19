#
## 2. Write a function day_name that converts an integer number 0 to 6 into the name 
## of a day. Assume day 0 is "Sunday". Once again, return None if the arguments to 
## the function are not valid. Here are some tests that should pass:
## 
## test(day_name(3) == "Wednesday")
## test(day_name(6) == "Saturday")
## test(day_name(42) == None)
#

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]



def day_name(number):
    if number ==  0: #Sunday
        return days[0]
    elif number == 1: #Monday
        return days[1]
    elif number == 2: #Tuesday
        return days[2]        
    elif number == 3: #Wednesday
        return days[3]
    elif number == 4: #Thursday
        return days[4]    
    elif number == 5: #Friday
        return days[5]    
    elif number == 6: #Saturday
        return days[6]

    else:
        return None

day_name(0)
day_name(1)
day_name(2)
day_name(3)
day_name(4)
day_name(5)
day_name(6)
day_name(42)



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
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
# -- Main Code ----------------------------------------------------------------

test_suite()        # Here is the call to run the tests
