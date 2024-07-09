# Key functions
# w = forward
# s = backwards
# d = clockwise
# a = counter-clockwise
# c = clear
# enter = paint a dot

from turtle import Turtle, Screen
tortuga = Turtle()
screen = Screen()


def move_forward():
    tortuga.forward(10)


def move_backwards():
    tortuga.backward(10)


def move_clockwise():
    tortuga.right(10)


def move_counter_clockwise():
    tortuga.left(10)


def clean_screen():
    tortuga.clear()
    tortuga.penup()
    tortuga.home()
    tortuga.pendown()


def paint_dot():
    tortuga.dot(size=10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clean_screen)
screen.onkey(key="space", fun=paint_dot)
screen.exitonclick()