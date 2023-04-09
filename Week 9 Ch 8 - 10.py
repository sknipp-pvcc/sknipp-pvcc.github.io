# 10. Write a function that recognizes palindromes. (Hint: use your reverse 
# function to make this easy!):
# 
# test(is_palindrome("abba"))
# test(not is_palindrome("abab"))
# test(is_palindrome("tenet"))
# test(not is_palindrome("banana"))
# test(is_palindrome("straw warts"))
# test(is_palindrome("a"))
## test(is_palindrome("")) # is an empty string a palindrome?


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string



is_palindrome("")
print (is_palindrome(""))
print ("Apparently an empty string is a palindrome")



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
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome("")) # is an empty string a palindrome?
# -- Main Code ----------------------------------------------------------------
test_suite()        # Here is the call to run the tests