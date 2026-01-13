# import colorgram
# import os

# print(os.getcwd())

# colors = colorgram.extract('image.jpg', 100)
# color_list = []

# for color in colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     color_list.append(new_color)

# print(color_list)
from turtle import Turtle, Screen
from random import choice

def draw_dot(timmy, color):
    timmy.dot(25, color[0], color[1], color[2])
    timmy.forward(50)

color_list = [(203, 34, 66), (71, 116, 151), (228, 161, 193), (246, 253, 251), (252, 246, 250), (150, 184, 70), (151, 160, 164), (242, 235, 46), (37, 161, 80), (35, 31, 32), (137, 205, 187), (240, 99, 54), (75, 65, 40), (33, 162, 165), (240, 246, 249), (221, 49, 65), (142, 210, 191), (145, 69, 64), (38, 155, 73), (137, 191, 57), (214, 144, 167), (67, 59, 37), (241, 170, 155), (207, 18, 76), (153, 206, 210), (59, 135, 199), (165, 195, 220), (235, 239, 12), (242, 14, 29)]

tim = Turtle()
screen = Screen()
x = -220
y = -180
tim.teleport(x,y)
tim.penup()
tim.hideturtle()
screen.colormode(255)
# tim.speed(0)
# tim.left(90)

for _ in range (10):
    for _ in range(10):
        color = choice(color_list)
        draw_dot(tim, color)
    y += 50
    tim.teleport(x,y)

screen.exitonclick()