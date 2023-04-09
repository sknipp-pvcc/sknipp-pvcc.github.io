#this = ["I", "am", "not", "a", "crook"]
#that = ["I", "am", "not", "a", "crook"]
#print("Test 1: {0}".format(this is that))
#that = this
#print("Test 2: {0}".format(this is that))

print(" Lines 1 and 2 are equal to each other, but are still two separate lists.\n Line 4 changes that, to be this. Since that is now this, this is now identical\n to that, regardless to what that was. ")

print("")
print("For Example: ")
print("Test 1 is false because they are different lists with different items in \n each list. When this gets assigned to that, it no longer matters. Now this\n is assigned as that and are the same list")
print("")
this = ["I", "am", "not", "a", "crook"]
that = ["All", "evidence", "points", "to", "you", "are"]
print("")
print("Test 1: {0}".format(this is that))
print("")
print(this)
print(that)
that = this
print("")
print("Test 2: {0}".format(this is that))
print("")
print(this)
print(that)