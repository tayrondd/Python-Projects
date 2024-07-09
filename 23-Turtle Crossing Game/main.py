import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

car_list = []

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Detect turtle reach y_max
    if player.ycor() >= 280:
        player.go_home()
        scoreboard.add_level()
        car_manager.increase_movement()

    # create cars and move them
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision between turtle and cars
    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
