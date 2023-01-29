# Sarah Knipp
# ITP.150.40 Python 1
# Week 3 Assignments Question 12

import turtle


wn = turtle.Screen()
wn.bgcolor("OliveDrab")
wn.title("Sarah Knipp Week 3 Question 12")

jeff = turtle.Turtle()
jeff.pensize(5)
jeff.shape("turtle")
jeff.fillcolor("black")
jeff.speed(1)

turn = 30


def clock():
    

    jeff.pencolor("yellow")
    jeff.penup()
    jeff.forward(200)
    jeff.pendown()
    jeff.forward(30)
    jeff.penup()
    jeff.forward(30)
    jeff.stamp()
    jeff.home()
    jeff.left(turn*i)
    

for i in range(12):
    clock()

        

        


clock()
