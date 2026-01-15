from turtle import Screen
from snake import Snake
import time

SPEED = 0.05

# Entering the dimensions for screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SPEED)
    snake.move()

screen.exitonclick()