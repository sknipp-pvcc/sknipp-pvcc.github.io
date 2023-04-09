a = [1, 2, 3]
b = a [:]
b [0] = 5

print(a)
print(b)

print("Before:")
print("a = [1,2,3]")
print("b = [ ]")

print("After:")
print("a = [1, 2, 3]")
print("b = [5, 2, 3]")
print("The third line assigns 5 to the element 0 in b")