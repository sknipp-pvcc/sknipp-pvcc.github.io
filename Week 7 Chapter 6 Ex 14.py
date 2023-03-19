# 
## 14. Write a function called is_even(n) that takes an integer as an argument and 
## returns True if the argument is an even number and False if it is odd.
##
## Add your own tests to the test suite.
#

def is_even(number):
    if not number % 2:
        return True
    else: 
        return False
    

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
    test(is_even(5) == False)
    test(is_even(6) == True)

# -- Main Code ----------------------------------------------------------------

test_suite()        # Here is the call to run the tests
  