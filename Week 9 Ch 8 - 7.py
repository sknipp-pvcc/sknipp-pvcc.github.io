# 7. Write a function that reverses its string argument, and satisfies these tests:
# Note: use the testsuite.py test harness from the previous chapter.
# 
#    test(reverse("happy") == "yppah")
#    test(reverse("Python") == "nohtyP")
#    test(reverse("") == "")
#    test(reverse("a") == "a")



def reverse(word):
    return word[::-1]


reverse("dog")






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
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
# -- Main Code ----------------------------------------------------------------
test_suite()        # Here is the call to run the tests