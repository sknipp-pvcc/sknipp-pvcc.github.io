
def scalar_mult(s, v):
    result = []
    for i in range(len(v)):
        result.append(s * v[i])
    return result



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
    test(scalar_mult(5, [1, 2]) == [5,10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

# -- Main Code ----------------------------------------------------------------

test_suite()       
