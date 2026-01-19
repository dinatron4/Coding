from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.75,0.75,1)
        self.color("white")
        self.speed("fastest")

    def move(self):
        self.forward(10)
        pass
        