# W - move towards
# S - move backwards
# A - turn left
# D - turn right
# C - clear the screen and move back to center

from turtle import Turtle, Screen


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_page():
    tim.reset()

tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_page)
screen.exitonclick()