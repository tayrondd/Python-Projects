import turtle
from turtle import Turtle, Screen
from random import randint, choice

tortuga = Turtle()
screen = Screen()

screen.colormode(255)
def random_color():
    tortuga.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))

#1
# for _ in range(4):
#     tortuga.forward(100)
#     tortuga.left(90)

#2
# for _ in range(15):
#     tortuga.down()
#     tortuga.forward(10)
#     tortuga.up()
#     tortuga.forward(10)

#3
# angles = 3 #start with a triangle
# for _ in range(10):
#     for _ in range(angles):
#         tortuga.forward(100)
#         tortuga.right(360/angles)
#     random_color()
#     angles += 1

#4
# directions = [0, 90, 180, 270]
# tortuga.speed("fastest")
# tortuga.pensize(15)
# for _ in range(100):
#     random_color()
#     tortuga.forward(50)
#     tortuga.setheading(choice(directions))

#5
tortuga.speed("fastest")
size_of_gad = 5
for _ in range(int(360/size_of_gad)):
    random_color()
    tortuga.circle(100)
    tortuga.setheading(tortuga.heading() + size_of_gad)

screen.exitonclick()