from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.movement_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.setheading(180)
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-250, 250)
            new_car.goto(300, y_position)
            self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            car.forward(self.movement_speed)

    def get_cars_cor(self):
        for car in self.cars_list:
            return car.xcor()

    def increase_movement(self):
        self.movement_speed += MOVE_INCREMENT
