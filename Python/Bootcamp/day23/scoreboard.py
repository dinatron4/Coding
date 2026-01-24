from turtle import Turtle

FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.color("black")
        self.penup()
        self.level = 1
        self.goto(-290,282)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",align= "CENTER" ,font=FONT)

