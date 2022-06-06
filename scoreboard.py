from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_highscore(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                self.high_score = file.write(str(self.score))
            self.high_score = self.score

    def update_score(self):
        self.clear()
        self.write(arg=f"score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.high_score = self.high_score
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

