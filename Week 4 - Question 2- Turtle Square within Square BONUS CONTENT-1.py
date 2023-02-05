#Sarah Knipp
#Week 4 - Question 2
#Turtle Square within Square

import turtle

wn = turtle.Screen()
wn.bgcolor("OliveDrab")
wn.setup(width = 1280, height = 1024, startx = 100, starty= 100)
wn.title("Sarah Knipp Week 4 Question 1")

kevin = turtle.Turtle()
kevin.pensize(3)
kevin.shape("turtle")
kevin.fillcolor("black")
kevin.speed(3)


size = 20

def DrawSquare (kevin, size):
    """Draw one square"""
    for i in range(4):
        kevin.forward (size) #length of line
        kevin.left(90)
        kevin.back(20)     #angle
        

#def Resize():
 #   for i in range(15):
  #      kevin.forward(size)
   #     kevin.left(90) 
       

  
def main():
    DrawSquare(kevin, 20)
    DrawSquare(kevin, 40)
    DrawSquare(kevin, 60)
    DrawSquare(kevin, 80)
    DrawSquare(kevin, 100)
    DrawSquare(kevin, 120)
    DrawSquare(kevin, 140)
    DrawSquare(kevin, 160)
    DrawSquare(kevin, 180)
    DrawSquare(kevin, 200)
    DrawSquare(kevin, 220)
    DrawSquare(kevin, 240)
    DrawSquare(kevin, 260)
    DrawSquare(kevin, 280)
    DrawSquare(kevin, 300)
    DrawSquare(kevin, 320)
    DrawSquare(kevin, 340)
    
    
    
    
    #Resize()

main()

