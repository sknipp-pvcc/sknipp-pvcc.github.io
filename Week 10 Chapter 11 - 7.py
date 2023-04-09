def dot_product(u, v):
    if len(u) != len(v):
        return "Error: Lists are not of the same length"
    else:
        result = 0
        for i in range(len(u)):
            result += u[i] * v[i]
        return result

print(dot_product([1,2,3], [1,2,3]))


import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   
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
    test(dot_product([1,1], [1,1]) == 2)
    test(dot_product([1,2], [1,4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

# -- Main Code ----------------------------------------------------------------

test_suite()       
