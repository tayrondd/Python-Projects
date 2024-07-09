from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_answer = screen.textinput(title="Make you bet!", prompt=f"Which turtle will win the race? Enter a color: \n {colors}")

all_turtle = []
x_position = -230
y_position = 100
for color in colors:
    new_tortuga = Turtle(shape="turtle")
    new_tortuga.penup()
    new_tortuga.color(color)
    new_tortuga.goto(x=x_position, y=y_position)
    all_turtle.append(new_tortuga)
    y_position -= 40


if user_answer:
    is_race_on = True

while is_race_on:
    for tortuga in all_turtle:
        if tortuga.xcor() > 230:
            is_race_on = False
            winning_color = tortuga.pencolor()
            if winning_color == user_answer:
                print(f"You`ve won! The {winning_color} turtle is the winner!")
            else:
                print(f"You`ve lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        tortuga.forward(rand_distance)

screen.exitonclick()