import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill() # Added this line
    
    
    
    t.left(90)
    t.forward(height)
    t.write(" "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10) # Added this line
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen") # Set up the window and its attributes

tess = turtle.Turtle()

tess.pensize(3) # Create tess and set some attributes

xs = [48,117,200,240,160,260,220]

for a in xs:
    if a  < 100:
        tess.fillcolor('green')
  
    elif a >= 100 and a < 200:
        tess.fillcolor("yellow")
     
        
    else:
        tess.fillcolor("red")

    draw_bar(tess, a)
    



wn.mainloop()
