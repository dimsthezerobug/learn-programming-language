from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.speed(0)
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align=ALIGNMENT, font=FONT)
