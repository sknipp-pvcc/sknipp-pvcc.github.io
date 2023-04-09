s = "There was an old shoe, that had old strings, and it was perfectly happy to be old."



def replace(s, old, new):


    return s.replace(old, new)


replace



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


    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
 
 
    s= "I love spom! Spom is my favorite food. Spom, spom, yum!"
 
 
    test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
 
 
    test(replace(s, "o", "a") == "I lave space! Spam in my favarite faad. Spam, spam, yum!")
#
# 
#  -- Main Code ----------------------------------------------------------------

test_suite()       
