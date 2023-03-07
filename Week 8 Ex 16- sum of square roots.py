# 16. Write a function sum_of_squares(xs) that computes the sum of the squares of the
# numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return
# 4+9+16 which is 29:


xs = (2, 3, 4)
sum_sqrt = 0

def sum_of_square_roots(xs):
    sum_sqrt = 0
    for square in xs:
        sum_sqrt += square ** 2
    return sum_sqrt


print (sum_of_square_roots(xs))



#Unit Testing
#Not sure I am understanding the point of this or if doing correctly

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
    # example: test(my_function(10) == 10)
    # exmaple: test(my_function(12) != 0)
   
    test(sum_of_square_roots([2, 3, 4]) == 29)
    test(sum_of_square_roots([ ]) == 0)
    test(sum_of_square_roots([2, -3, 4]) == 29)
# -- Main Code ----------------------------------------------------------------
test_suite()        # Here is the call to run the tests











#test(sum_of_squares([2, 3, 4]) == 29)
#test(sum_of_squares([ ]) == 0)
#test(sum_of_squares([2, -3, 4]) == 29)
