from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)


        