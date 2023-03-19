#
## 15. Now write the function is_odd(n) that returns True when n is odd and False 
## otherwise. Include unit tests for this function too.
## 
## Finally, modify it so that it uses a call to is_even to determine if its argument 
## is an odd integer, and ensure that its test still pass.
#


def is_odd(n):
    if n % 2:
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
    test(is_odd(5) == True)
    test(is_odd(6) == False)

# -- Main Code ----------------------------------------------------------------

test_suite()        # Here is the call to run the tests
  