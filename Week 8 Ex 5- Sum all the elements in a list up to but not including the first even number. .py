#5. Sum all the elements in a list up to but not including the first even number. 
#(Write your unit tests. What if there is no even number?)

numbers = [1, 3, 5, 6, 7, 2, 4, 9]

def sum_up_to_first_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            return total
        else:
            total += num
    return total


result = sum_up_to_first_even(numbers)
print(result)  

print ("If there is no even number, all the numbers in the list will be added")

#Unit Test
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
    test(sum_up_to_first_even(numbers) == 8)
    test(sum_up_to_first_even(numbers) == 9)
# -- Main Code ----------------------------------------------------------------
test_suite()        # Here is the call to run the tests