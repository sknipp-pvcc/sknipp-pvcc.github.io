#
## 19. Now do the opposite: write the function c2f which converts Celsius to 
## Fahrenheit:
## 
## test(c2f(0) == 32)
## test(c2f(100) == 212)
## test(c2f(-40) == -40)
## test(c2f(12) == 54)
## test(c2f(18) == 64)
## test(c2f(-48) == -54)
#

def c2f(celsius):
    fahrenheit = (celsius * 1.8) + 32 #formula for C to F
    return round(fahrenheit)  



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
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)
# -- Main Code ----------------------------------------------------------------

test_suite()        # Here is the call to run the tests