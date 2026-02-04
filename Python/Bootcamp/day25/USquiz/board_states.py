from turtle import Turtle

FONT = ("Courier", 8, "normal")

class BoardStates(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.penup()

    def write_state(self, state, coordinate):
        self.goto(coordinate)
        self.write(arg=f"{state}", font=FONT, align="center")