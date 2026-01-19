from turtle import Screen
from racket import Racket
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600
X_ONE = -WIDTH//2 + 15
X_TWO = WIDTH//2 - 25
LEFT_POS = (X_ONE,30)
RIGHT_POS = (X_TWO,30)

# Entering the configuration for screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("A Game of Pong")
screen.tracer(0)
screen.listen()

# Starting each racket
l_racket = Racket(start_position=LEFT_POS)
r_racket = Racket(start_position=RIGHT_POS)


# Starting the ball
ball = Ball()
bounce = True

scoreboard = Scoreboard()

screen.onkey(l_racket.move_up,"w")
screen.onkey(l_racket.move_down,"s")
screen.onkey(r_racket.move_up,"Up")
screen.onkey(r_racket.move_down,"Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect colision with top wall
    if ball.ycor() >= 290 or ball.ycor() <= -280:
        ball.bounce_wall()
    
    # Detect colision with paddles
    if ((ball.xcor() > 350 and r_racket.distance(ball) <= 50) or 
        (ball.xcor() < -360 and l_racket.distance(ball) <= 50)) and bounce:
            ball.bounce_paddle()
            bounce = False
    elif -30 < ball.xcor() < 30:
        bounce = True

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect R paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()