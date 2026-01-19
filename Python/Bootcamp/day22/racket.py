from turtle import Turtle

STEP = 20
UP = 90
DOWN = 270

class Racket(Turtle):
    
    def __init__(self,start_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(start_position)

    def move_up(self):
        x, y = self.position()
        if y <= 230:
            self.goto(x, y + STEP)

    def move_down(self):
        x, y = self.position()
        if y >= -230:
            self.goto(x, y - STEP)            