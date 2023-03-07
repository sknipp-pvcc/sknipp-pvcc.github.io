#15. Write a function num_even_digits(n) that counts the number of even digits in n.
#These tests should pass:

#test(num_even_digits(123456) == 3)
#test(num_even_digits(2468) == 4)
#test(num_even_digits(1357) == 0)
#test(num_even_digits(0) == 1)

def num_even_digits(n):
    if n == 0:
        return 1
    count = 0
    while n != 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n //= 10
    return count

n= 0
even_count = num_even_digits(n)
print("The number of even digits in", n, "is", even_count)


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
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)
# -- Main Code ----------------------------------------------------------------
test_suite()        # Here is the call to run the tests