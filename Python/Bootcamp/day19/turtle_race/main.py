from turtle import Turtle, Screen
from random import choice, randint

def starting_turtle(color, y):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(-200,y)
    return turtle

def move_turtles(turtles, user_color):
    for turtle in turtles:
        steps = randint(1,10)
        turtle.forward(steps)
        if turtle.xcor() >= 222.5:
            winning_color = turtle.pencolor()
            if winning_color == user_color:
                print(f"You won. The {user_color} won the race.")
            else:
                print(f"You lost. The {winning_color} won the race.")
            return False
    return True


color_list = ["green", "blue", "red", "orange", "purple", "black", "violet"]
turtles = []
game_is_on = False
screen = Screen()
y = -100

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")
color = user_bet

if user_bet:
    game_is_on = True

for index in range(0,6):    
    turtles.append(starting_turtle(color, y))
    color_list.remove(color)
    color = choice(color_list)
    y += 40

while game_is_on:
    game_is_on = move_turtles(turtles, user_bet)

screen.exitonclick()