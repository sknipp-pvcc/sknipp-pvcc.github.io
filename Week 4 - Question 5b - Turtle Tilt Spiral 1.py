#Sarah Knipp
#Week 4 - Question 5b
#Turtle Spiral

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Sarah Knipp Week 4 Question 5b")

kevin = turtle.Turtle()
kevin.pensize(5)
kevin.shape("turtle")
kevin.speed(15)
kevin.color("darkblue")

jeff = turtle.Turtle()
jeff.pensize(4)
jeff.shape("turtle")
jeff.speed(25)
jeff.color("blue")

fred = turtle.Turtle()
fred.pensize(3)
fred.shape("turtle")
fred.speed(25)
fred.color("royalblue")

george = turtle.Turtle()
george.pensize(2)
george.shape("turtle")
george.speed(25)
george.color("skyblue")



size = 2 

def spiral_kevin():
    jeffMemory = 0 #remember where you are, don't just jump elsewhere
    kevinMemory = 0 
    fredMemory = 0
    georgeMemory = 0
    for i in range (200):
        for y in range(6):
            kevin.forward(size * kevinMemory)
            kevin.left(89)
            kevinMemory = kevinMemory + 1
        for x in range(5):
            jeff.forward(size * jeffMemory)
            jeff.left(89)
            jeffMemory = jeffMemory + 1
        for g in range(4):
            fred.forward(size * fredMemory)
            fred.left(89)
            fredMemory = fredMemory + 1     
        for q in range(6):
            george.forward(size * georgeMemory)
            george.left(89)
            georgeMemory = georgeMemory + 1     
       
        
       
       

  
def main():
    spiral_kevin()














main()

