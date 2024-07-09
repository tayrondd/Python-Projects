import random
from turtle import Turtle, Screen
import random

tortuga = Turtle()
screen = Screen()
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
              (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
              (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86),
              (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162),
              (156, 212, 190), (87, 46, 33), (37, 45, 83), (245, 205, 7), (35, 88, 88), (103, 24, 56)]
screen.colormode(255)
tortuga.penup()
tortuga.speed("fastest")
tortuga.hideturtle()


def draw_line():
    for _ in range(10):
        tortuga.color(random.choice(color_list))
        tortuga.dot(size=20)
        tortuga.forward(50)


x = -250
y = -250
for _ in range(10):
    tortuga.goto(x=x, y=y)
    draw_line()
    y += 50

screen.exitonclick()
