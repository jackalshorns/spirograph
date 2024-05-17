from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

TILT = 20
RADIUS = 100

tim.speed("fastest")

def draw_circle():
    for i in range(int(360/TILT) - 1):
        r = random.random()
        g = random.random()
        b = random.random()
        tim.color(r, g, b)
        tim.circle(RADIUS)
        tim.left(TILT)

draw_circle()


# Exit on click
screen.exitonclick()