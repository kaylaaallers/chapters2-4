
import turtle

def drawPoly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(3)

drawPoly(tess, 8, 50)

from test import testEqual

def sumTo(n):
    result = (n * (n + 1)) / 2
    return result

# Now lets see how well this works
t = sumTo(0)
print("The sum from 1 to 0 is",t)
t = sumTo(10)
print("The sum from 1 to 10 is",t)
t = sumTo(5)
print("The sum from 1 to 5 is",t)


import turtle

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

wolfram = turtle.Turtle()
drawFivePointStar(wolfram)



