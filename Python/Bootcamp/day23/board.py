from turtle import Turtle

STARTING_POSITION = (0, -280)

class Board(Turtle):
    def __init__(self, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(stretch_len=30, stretch_wid=2, outline=1)
        self.color("light green")
        self.create_map()
    
    def create_map(self):
        # road_map = []
        pos = STARTING_POSITION
        self.goto(pos)
        # road_map.append(self)
        for i in range (1,7):
            if i % 2 != 0:
                segment = Turtle(shape="square")
                segment.penup()
                segment.shapesize(stretch_len=30, stretch_wid=7, outline=1)
                segment.color("light gray")
                pos_x, pos_y = pos
                pos_y += 90
                pos = (pos_x, pos_y)
                segment.goto(pos)
                # road_map.append(segment)
            else:
                segment = Turtle(shape="square")
                segment.penup()
                segment.shapesize(stretch_len=30, stretch_wid=2, outline=1)
                segment.color("light green")
                pos_x, pos_y = pos
                pos_y += 90
                pos = (pos_x, pos_y)
                segment.goto(pos)
                # road_map.append(segment)

# class Crosswalk(Turtle):
#     def __init__(self, shape = "square", undobuffersize = 1000, visible = True):
#         super().__init__(shape, undobuffersize, visible)
#         self.penup()
#         self.shapesize(stretch_len=30, stretch_wid=1)
#         self.goto(0,100)
#         self.color("green")