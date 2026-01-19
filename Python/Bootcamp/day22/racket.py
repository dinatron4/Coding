from turtle import Turtle

MOVE_DISTANCE = 10
STEP = 15
UP = 90
DOWN = 270

class Racket:
    
    def __init__(self, start_position):
        paddle = Turtle(shape="square")
        paddle.color("white")
        paddle.penup()
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.goto(start_position)

    def move_up(self):
        self.head.seth(UP)
        size = len(self.segments) - 1
        for seg_num in range (size, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(STEP)

    def move_down(self):
        self.segments[-1].seth(DOWN)
        size = len(self.segments) - 1
        for seg_num in range (0, size, 1):
            new_x = self.segments[seg_num + 1].xcor()
            new_y = self.segments[seg_num + 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[-1].forward(STEP)
        pass
    