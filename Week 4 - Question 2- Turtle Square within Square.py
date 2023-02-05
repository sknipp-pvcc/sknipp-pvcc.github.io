import turtle

wn = turtle.Screen()
wn.bgcolor("OliveDrab")
wn.setup(width = 1280, height = 1024, startx = 100, starty= 100)
wn.title("Sarah Knipp Week 4 Question 1")

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
    DrawSquare(kevin, 20, 90)
    DrawSquare(kevin, 40, 90)
    DrawSquare(kevin, 60, 90)
    DrawSquare(kevin, 80, 90)
    DrawSquare(kevin, 100, 90)
    
    DrawSquare(kevin, 120, 90)
    DrawSquare(kevin, 140, 90)
    DrawSquare(kevin, 160, 90)
    DrawSquare(kevin, 180, 90)
    
    DrawSquare(kevin, 200, 90)
    DrawSquare(kevin, 220, 90)
    DrawSquare(kevin, 240, 90)
    DrawSquare(kevin, 260, 90)
    DrawSquare(kevin, 280, 90)
    
    DrawSquare(kevin, 300, 90)
    DrawSquare(kevin, 320, 90)
    DrawSquare(kevin, 340, 90)
    DrawSquare(kevin, 360, 90)
    DrawSquare(kevin, 380, 90)

    DrawSquare(kevin, 400, 90)
    DrawSquare(kevin, 420, 90)
    DrawSquare(kevin, 440, 90)
    DrawSquare(kevin, 460, 90)
    DrawSquare(kevin, 480, 90)

    DrawSquare(kevin, 500, 90)
    DrawSquare(kevin, 520, 90)
    DrawSquare(kevin, 540, 90)
    DrawSquare(kevin, 560, 90)
    DrawSquare(kevin, 580, 90)

    DrawSquare(kevin, 600, 90)
    DrawSquare(kevin, 620, 90)
    DrawSquare(kevin, 640, 90)
    DrawSquare(kevin, 660, 90)
    DrawSquare(kevin, 680, 90)





main()