from turtle import Turtle

class Scoreboard(Turtle):                           # Here we implement a scoreboard to present to the player
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def add_to_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def get_score(self):
        return self.score

