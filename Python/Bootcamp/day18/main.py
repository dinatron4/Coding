from turtle import Turtle, Screen
from random import randint, choice

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r, g, b)

def drawing_polygon(timmy, num_sides):
    angle = (num_sides - 2)*180/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(180-angle)

def random_walk(timmy):
    angle = choice([0,90,180,270])
    timmy.forward(30)
    timmy.seth(angle)

def circle_shape(timmy, num_circles):
   timmy.circle(100)
   timmy.left(-360/circles) 

circles = 72
tim = Turtle()
screen = Screen()
# tim.teleport(-60,60)
# tim.width(5)
tim.speed(0)
screen.colormode(255)

# tim.shape("turtle")

# for i in range(3,11):
#     random_color = [randint(0,255), randint(0,255), randint(0,255)]
#     tim.color(random_color[0], random_color[1], random_color[2])
#     tim.pencolor(random_color[0], random_color[1], random_color[2])
#     drawing_polygon(tim, i)

# for i in range(500):
#     random_color = [randint(0,255), randint(0,255), randint(0,255)]
#     tim.color(random_color[0], random_color[1], random_color[2])
#     tim.pencolor(random_color[0], random_color[1], random_color[2])
#     random_walk(tim)

for _ in range(circles):
    color = random_color()
    tim.color(color)
    tim.pencolor(color)
    circle_shape(tim, circles)

screen.exitonclick()