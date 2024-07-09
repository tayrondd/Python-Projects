from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=self.x_axis, y=self.y_axis)

    def move_up(self):
        self.y_axis += 20
        self.goto(x=self.x_axis, y=self.y_axis)

    def move_down(self):
        self.y_axis -= 20
        self.goto(x=self.x_axis, y=self.y_axis)
