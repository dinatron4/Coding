from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SPEED = 0.04

# Entering the configuration for screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Starting our snake and listening to inputs
snake = Snake()
screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

# Starting game, food and scoreboard
food = Food()
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SPEED)
    snake.move()

    #Detect colision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    #If head colides with segment in tail, trigger game_is_on False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()