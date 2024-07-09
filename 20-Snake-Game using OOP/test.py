from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")


screen = Screen()
Food()
screen.exitonclick()