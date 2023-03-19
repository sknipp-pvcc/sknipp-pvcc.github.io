#1. We've said nothing in this chapter about whether you can pass tuples as
#arguments to a function. Construct a small Python example to test whether this
#is possible, and write up your findings.


def function(tuple):
    for thing in tuple:
        print(thing)

tups = (1, 2, 3, 4, 5, "pizza", "dog", "fries", "book", "hard")
function(tups)

print("Seems like you can")