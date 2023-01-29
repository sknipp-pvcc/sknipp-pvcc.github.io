# Sarah Knipp
# ITP.150.40 Python 1
# Week 3 Assignments Question 6


# A tale of Two Turtles: Kevin and Jeff
# Kevin spends his day eating grass (in weirdly geometric patterns). But is careful to not over graze.
# Jeff has no such care for overgrazing, and thus, just leaves a path of dirt.

#helpful page in putting this together (https://realpython.com/beginners-guide-python-turtle/)


import turtle
wn = turtle.Screen()
wn.bgcolor("OliveDrab")
wn.title("Sarah Knipp Week 3 Question 6")

kevin = turtle.Turtle()
kevin.pensize(5)
kevin.shape("turtle")
kevin.fillcolor("black")
kevin.pencolor("yellow")
kevin.speed(2)


#triangle

kevin.forward(50)
kevin.left(120)
kevin.forward(50)
kevin.left(120)
kevin.forward(50)
kevin.left(120)

kevin.penup()

#square

kevin.forward(-100)
kevin.pendown()
kevin.forward(50)
kevin.left(90)
kevin.forward(50)
kevin.left(90)
kevin.forward(50)
kevin.left(90)
kevin.forward(50)
kevin.left(90)

kevin.penup()

#hexagon

kevin.right(-100)
kevin.forward(-100)
kevin.pendown()
kevin.left(60)
kevin.forward(30)
kevin.left(60)
kevin.forward(30)
kevin.left(60)
kevin.forward(30)
kevin.left(60)
kevin.forward(30)
kevin.left(60)
kevin.forward(30)
kevin.left(60)
kevin.forward(30)

kevin.penup()

#octogon

kevin.right(300)
kevin.forward(100)
kevin.pendown()
kevin.forward(28)
kevin.left(45)
kevin.forward(28)
kevin.left(45)
kevin.forward(28)
kevin.left(45)
kevin.forward(28)
kevin.left(45)
kevin.forward(28)
kevin.left(45)
kevin.forward(28)
kevin.left(45)
kevin.forward(28)
kevin.left(45)
kevin.forward(28)
kevin.left(45)


#Now with loops

jeff = turtle.Turtle()
jeff.pensize(5)
jeff.shape("turtle")
jeff.fillcolor("black")
jeff.pencolor("sienna")
jeff.speed(2)


#triangle
for i in range(3):
    jeff.forward(50)
    jeff.left(120)

jeff.penup()

#square
jeff.forward(-100)
jeff.pendown()

for i in range(4):
    jeff.forward(50)
    jeff.left(90)

jeff.penup()

#hexagon
jeff.right(-100)
jeff.forward(-100)
jeff.pendown()

for i in range(6):
    jeff.left(60)
    jeff.forward(30)

jeff.penup()

#octogon
jeff.right(300)
jeff.forward(100)
jeff.pendown()

for i in range(8):
    jeff.forward(28)
    jeff.left(45)
