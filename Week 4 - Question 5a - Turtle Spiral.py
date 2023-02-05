#Sarah Knipp
#Week 4 - Question 5a
#Turtle Spiral

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Sarah Knipp Week 4 Question 5a")

kevin = turtle.Turtle()
kevin.pensize(3)
kevin.shape("turtle")
kevin.fillcolor("purple")
kevin.speed(8)
kevin.color("purple")

size = 5 

def spiral():
    for i in range(110):
        kevin.forward(size * i)
        kevin.left(90) 
       

  
def main():
    spiral()

main()

