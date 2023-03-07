#14. What will num_digits(0) return? Modify it to return 1 for this case. Why does a 
#call to num_digits(-24) result in an infinite loop? (hint: -1//10 evaluates to -1) 
#Modify num_digits so that it works correctly with any integer value. Add these tests:

#test(num_digits(0) == 1)
#test(num_digits(-12345) == 5)



def num_digits(n):
    count = 0
    while n != 0 and n != -1:
        count = count + 1
        n = n // 10
        print (n)
    return count

num_digits(12345)

print("a. The while loop does not even start due to n not equal zero being untrue")
print("b. -24 does not work because you can't count up by one to get to negative 24 from zero.")




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
    #test(num_digits(0) == 1)
    #test(num_digits(-12345) == 5)
# -- Main Code ----------------------------------------------------------------
test_suite()        # Here is the call to run the tests