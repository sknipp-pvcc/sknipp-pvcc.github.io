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
        kevin.left(144)
        kevin.forward (100)
        

drawStar()