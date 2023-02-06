import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Sarah Knipp Week 4 Question 6")

kevin = turtle.Turtle()
kevin.pensize(5)
kevin.shape("turtle")
kevin.speed(2)
kevin.color("cyan")





def drawStar():
    for i in range(5):
        kevin.pendown()
        kevin.forward (100)
        kevin.right(144)
        kevin.penup()

drawStar()
kevin.forward(350)
kevin.right(144)

drawStar()
kevin.forward(350)
kevin.right(144)

drawStar()
kevin.forward(350)
kevin.right(144)

drawStar()
kevin.forward(350)
kevin.right(144)

drawStar()
kevin.forward(350)
kevin.right(144)

#If you don't pick the pen up, it makes a giant start that has a little star at each point.
