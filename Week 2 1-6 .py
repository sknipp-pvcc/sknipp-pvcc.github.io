# Sarah Knipp
# ITP.150.40 Python 1
# Week 2 Assignments 

print("1.------------------------------------------")  

one = "All"
has = "work"
nay = "and"
seen = "no"
the = "play"
shining = "makes"
I = "Jack"
should = "a"
watch = "dull"
it = "boy."

print(one, has, nay, seen, the, shining, I, should, watch, it)

print("2.------------------------------------------")

print(6 * 1 - 2)
print(6 * (1 - 2))

print("3.------------------------------------------")
#Random Commentary
ShiningRef ="All " + "work " + "and "+ "no " + "play " + "makes " + "Jack " + "a " + "dull " + "boy."
print(ShiningRef)
#No changes, still works, commentary does not appear

print("4.------------------------------------------")

# bruce + 4
# NameError: name 'bruce' is not defined

bruce = 6
print(bruce + 4)

print("5.------------------------------------------")

P = 10000
r = .08
n =  12
t = int(input("How many years will the money be compounded?: (Enter Number)"))

A = P * ( 1 + r / n ) ** ( n * t)

print('$ ' + format(A,'8,.2f'))

print("6.------------------------------------------")
print("a. " + format(5 % 2))
print("b. " + format(9 % 5))
print("c. " + format(15 % 12))
print("d. " + format(12 % 15))
print("e. " + format(6 % 6))
print("f. " + format(0 % 7))
print("g. " "(7 % 0) (ZeroDivisionError: Integer division or modulo by zero)")
