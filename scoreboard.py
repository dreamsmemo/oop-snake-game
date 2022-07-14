from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score = {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=-110, y=0)
        self.color("red")
        self.write("GAME OVER", font=("Courier", 30, "bold"))