#6. Count how many words occur in a list up to and including the first occurrence 
#of the word “sam”. (Write your unit tests for this case too. What if “sam” does 
#not occur?)


list = ["fire", "play", "grade", "cow", "sodas","sam", "there", "ghost", "cabin"]

def CountWordsUntilSam(list):
    count = 0
    for word in list:
        count += 1
        if word == 'sam':
            return count
        

total = CountWordsUntilSam(list)

print (total)



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
    test(CountWordsUntilSam(list) == 6)
    test(CountWordsUntilSam(list) == 8)
# -- Main Code ----------------------------------------------------------------
test_suite()        # Here is the call to run the tests