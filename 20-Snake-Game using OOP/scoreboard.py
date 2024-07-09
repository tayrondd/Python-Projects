from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highest_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}, Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()
        # self.goto(0, 0)
        # self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
