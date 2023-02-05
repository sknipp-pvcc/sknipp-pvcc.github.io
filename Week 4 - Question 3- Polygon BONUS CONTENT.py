import turtle

wn = turtle.Screen()
wn.bgcolor("OliveDrab")
wn.setup(width = 1280, height = 1024, startx = 100, starty= 100)
wn.title("Sarah Knipp Week 4 Question 3")

kevin = turtle.Turtle()
kevin.pensize(3)
kevin.shape("turtle")
kevin.fillcolor("black")
kevin.speed(8)


size = 20

def DrawSquare (kevin, size, angle):
    """pre-position"""
    halfStep = (size / 2)
    kevin.penup() 
    kevin.forward(halfStep)
    kevin.right(angle)
    kevin.forward(halfStep)
    kevin.right(180)
    kevin.pendown()
    """Draw one square"""
    for i in range(4):
        kevin.forward (size) #length of line
        kevin.left(angle) #angle
    """un-do pre-position"""
    kevin.penup()
    kevin.forward(halfStep)
    kevin.left(angle)
    kevin.forward(halfStep)
    kevin.right(180)
    

            
        


  
def main():
    DrawSquare(kevin, 20, 45)
    DrawSquare(kevin, 20, 45)
    DrawSquare(kevin, 20, 45)
    DrawSquare(kevin, 20, 45)
    DrawSquare(kevin, 20, 45)
    


main()