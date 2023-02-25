
import math

a = float(input("length of side a: "))
b = float(input("length of side b: "))

def find_hypot():
    c = ((a * a) + (b * b))
    print("The length of the hypotenuse: ")
    print (math.sqrt(c))
  



find_hypot()