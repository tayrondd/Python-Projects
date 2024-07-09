from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
Turtle().shape(image)

tortuga = Turtle()
tortuga.penup()
# tortuga.hideturtle()

# panda
data = pandas.read_csv("50_states.csv")

answered_states = []
score = 0

while len(answered_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What`s another state`s name")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        # Missed states
        missing_states = []
        for state in data.state.to_list():
            if state not in answered_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("missed_states.csv")
        break

    state = data[data["state"] == answer_state]
    if state.empty:
        print("Wrong Answer")
    elif answer_state in answered_states:
        print("state is already written")
    else:
        # panda stuff
        x_cor = int(state.x)
        y_cor = int(state.y)
        state_item = state.state.item()

        # print(state_item)
        # print(x_cor)
        # print(y_cor)

        # turtle
        tortuga.goto(x_cor, y_cor)
        tortuga.write(answer_state, align="center")

        # score
        score += 1
        answered_states.append(state_item)


