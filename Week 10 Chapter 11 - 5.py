

def add_vectors(u, v):
    result = []
    for i in range(len(u)):
        result.append(u[i] + v[i])
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
    test(add_vectors([1,1], [1,1]) == [2,2])
    test(add_vectors([1,2], [1,4]) == [2,6])
    test(add_vectors([1,2,1], [1,4,3]) == [2,6,4])

# -- Main Code ----------------------------------------------------------------

test_suite()       
