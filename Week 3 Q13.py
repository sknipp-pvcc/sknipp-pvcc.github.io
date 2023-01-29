#
## Write a turtle program that prints out your initials in turtle graphics
## You will probably have to use "block letters" to do this. 
## The height of each letter should be 100 moves
#

# Sarah Knipp
# ITP.150.40 Python 1
# Week 3 Assignments Question py3

import turtle

wn = turtle.Screen()
wn.bgcolor("OliveDrab")
wn.title("Sarah Knipp Week 3 Question 12")

jeff = turtle.Turtle()
jeff.pensize(5)
jeff.shape("turtle")
jeff.fillcolor("black")
jeff.speed(5)


jeff.pendown()

jeff.left(90) #turn down 
jeff.forward(50) #line 1 down
jeff.penup()
jeff.forward(20) #line 2 down

jeff.pendown()
jeff.forward(50)

jeff.right(45)
jeff.forward(25)

jeff.right(45)
jeff.forward(25)

jeff.right(45)
jeff.forward(25)

jeff.right(45)
jeff.forward(50)

jeff.penup()
jeff.forward(20)

jeff.pendown()
jeff.forward(50)

jeff.right(45)
jeff.forward(25)

jeff.right(45)
jeff.forward(25)

jeff.right(45)
jeff.forward(25)


jeff.right (135)
jeff.penup()
jeff.forward(30) #jump to center line

#center line drawn
jeff.pendown()
jeff.left(90)   #turn for vertical rise center line
jeff.forward (50)
jeff.penup ()
jeff.forward(20)
jeff.pendown()
jeff.forward(50)

#horizontal slashes (right side)

jeff.backward (50)
jeff.right(90)
jeff.forward(30)

#horizontal slashes (left side)

jeff.backward(30)
jeff.right(35)

jeff.forward(30)


jeff.right(145)
jeff.penup()


jeff.forward(30)

jeff.pendown()


jeff.forward(25)
jeff.back(30)

jeff.right(35)
jeff.forward(30)
jeff.penup()
#S complete above this line

#begin K

jeff.right(145)
jeff.forward(50)
jeff.pendown()
jeff.forward(40)


jeff.right(140)
jeff.forward(25)


jeff.left(55)
jeff.forward(30)


jeff.left(145)
jeff.forward(40)


jeff.right(60)
jeff.forward(20)


jeff.right(120)
jeff.forward(50)


jeff.left(75)
jeff.forward(80)


jeff.right(115)
jeff.forward(20)


jeff.right(65)
jeff.forward(75)


jeff.left(135)
jeff.forward(25)

jeff.right(90)
jeff.forward(30)

jeff.penup()
jeff.forward(50)
jeff.right(90)

jeff.stamp()










