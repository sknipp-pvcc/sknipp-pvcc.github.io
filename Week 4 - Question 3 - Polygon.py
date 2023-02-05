import turtle

wn = turtle.Screen()
wn.bgcolor("OliveDrab")
wn.setup(width = 1280, height = 1024, startx = 100, starty= 100)
wn.title("Sarah Knipp Week 4 Question 3")

tess = turtle.Turtle()
tess.pensize(3)
tess.shape("turtle")
tess.fillcolor("black")
tess.speed(8)


t = tess

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward (sz)
        t.left(45)

draw_poly(tess,8, 50)




