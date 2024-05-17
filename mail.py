from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
# Old Shizzy w/ Stamps
# # RADIUS = 1
# # CURSOR_RADIUS = 1
#
# tim.hideturtle()
# tim.shape('circle')
# #tim.shapesize(RADIUS / CURSOR_RADIUS, outline=RADIUS/5)
# tim.turtlesize(stretch_len=50, stretch_wid=50)
# tim.penup()
# #tim.circle(RADIUS)
# # tim.stamp()
# # tim.forward(100)
# # tim.stamp()
# # """
#
# for i in range(36):
#     steps = 10
#     angle = 10
#     tim.right(angle)
#     tim.fd(steps)
#     r = random.randint(0, 1)
#     g = random.randint(0, 1)
#     b = random.randint(0, 1)
#     tim.color(r, g, b)
#     tim.fillcolor("")
#     tim.stamp()

tim.circle(100)

# Exit on click
screen.exitonclick()