from turtle import Turtle, Screen

TIMMY = Turtle()

def start_position():
    TIMMY.left(180)
    TIMMY.forward(400)
    TIMMY.right(90)
    TIMMY.forward(400)
    TIMMY.right(90)
    TIMMY.clear()

print(TIMMY)
TIMMY.shape("turtle")
TIMMY.color("red", "chartreuse")
start_position()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()