#Sarah Knipp
#Week 4 - Question 6
#Turtle Triangle

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Sarah Knipp Week 4 Question 6")

kevin = turtle.Turtle()
kevin.pensize(5)
kevin.shape("turtle")
kevin.speed(2)
kevin.color("cyan")


t = kevin

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward (sz)
        t.left(120)

draw_poly(kevin, 3, 80)