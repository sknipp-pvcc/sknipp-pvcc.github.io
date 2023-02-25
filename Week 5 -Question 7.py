import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    
    t.begin_fill() # Added this line
    t.color('cyan')
    t.left(90)
    t.forward(height)
    t.pensize(6) #let's make them 3d-ish
    t.pencolor('white') #nice little highlight
    t.write(" "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup() 
    t.forward(12) # Added this line (and just a tad more space between)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("black") # Set up the window and its attributes

tess = turtle.Turtle()
tess.color("blue", "skyblue")
tess.pensize(3) # Create tess and set some attributes

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
