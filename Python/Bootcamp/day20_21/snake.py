from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-10,0),(-20,0)]
MOVE_DISTANCE = 10
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            part = Turtle(shape="square")
            part.penup()
            part.shapesize(0.5,0.5,1)
            part.color("white")
            part.goto(position)
            self.segments.append(part)
    
    def move(self):
        size = len(self.segments) - 1
        for seg_num in range(size, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)