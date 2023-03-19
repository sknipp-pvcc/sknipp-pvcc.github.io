# 9. Write a function that removes all occurrences of a given letter from a string:
# 
# test(remove_letter("a", "apple") == "pple")
# test(remove_letter("a", "banana") == "bnn")
# test(remove_letter("z", "banana") == "banana")
# test(remove_letter("i", "Mississippi") == "Msssspp")
# test(remove_letter("b", "") = "")
# test(remove_letter("b", "c") = "c")

words = "So many blurbs to write, so little time"

def remove_letter(letter, string):
    return string.replace(letter, '')

remove_letter("o", words)




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
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")
# -- Main Code ----------------------------------------------------------------
test_suite()        # Here is the call to run the tests