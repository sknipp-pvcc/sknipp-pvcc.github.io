#Sarah Knipp
#Week 4 - Question 1
#Draw squares with turtle

import turtle

wn = turtle.Screen()
wn.bgcolor("OliveDrab")
wn.title("Sarah Knipp Week 3 Question 12")

kevin = turtle.Turtle()
kevin.pensize(5)
kevin.shape("turtle")
kevin.fillcolor("black")
kevin.speed(2)




def DrawSquare ():
    """Draw one square"""
    for i in range(4):
       kevin.forward (20) #length of line
       kevin.left(90)     #angle

        
def MoveAlong():
    """Ditch that last square"""
    kevin.penup()
    kevin.forward(40)
    kevin.pendown()


def main():
    """Repeat Both Funtions"""
    for i in range(5):
        DrawSquare()
        MoveAlong()


main()





