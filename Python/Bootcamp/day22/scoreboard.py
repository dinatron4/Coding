from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,240)
        self.write(arg=f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100,240)
        self.write(arg=f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)


        