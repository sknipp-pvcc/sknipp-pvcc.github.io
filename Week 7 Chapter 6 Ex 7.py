#
## 7. Write a function to_secs that converts hours, minutes and seconds to a total 
## number of seconds. Here are some tests that should pass:
##
## test(to_secs(2, 30, 10) == 9010)
## test(to_secs(2, 0, 0) == 7200)
## test(to_secs(0, 2, 0) == 120)
## test(to_secs(0, 0, 42) == 42)
## test(to_secs(0, -10, 10) == -590)
#

def to_secs(hours, minutes, seconds):
    total = hours * 3600 + minutes * 60 + seconds
    return total

to_secs(5,9,52)

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
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
# -- Main Code ----------------------------------------------------------------

test_suite()        # Here is the call to run the tests
