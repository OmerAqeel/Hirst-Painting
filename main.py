import turtle
from turtle import Turtle, Screen
import random

# import colorgram as cg
#
# rgb_colors = []
# colours = cg.extract("spot.jpg", 72)
#
# for color in colours:
#     r = float(color.rgb[0])
#     g = float(color.rgb[1])
#     b = float(color.rgb[2])
#
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

colours_list = [(233, 233, 236), (233, 232, 228), (236, 230, 233), (224, 234, 229), (176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89), (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187), (131, 184, 161), (48, 187, 202), (172, 187, 222), (232, 173, 164), (154, 209, 219), (100, 51, 43), (34, 64, 115), (44, 80, 79), (215, 207, 37), (52, 58, 66), (31, 87, 90), (76, 51, 43), (40, 67, 65), (84, 37, 55)]

turtle.colormode(255)

timScreen = Screen()

tim = Turtle()
tim.penup()
tim.speed("fastest")

def moveUp():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

#Setting the starting point of the turtle
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for fd in range(1, 101):
    tim.dot(20, random.choice(colours_list))
    tim.forward(50)

    if fd % 10 == 0:
        moveUp()

timScreen.exitonclick()
