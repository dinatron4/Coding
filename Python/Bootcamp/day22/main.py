from turtle import Screen
from racket import Racket
from ball import Ball
import time

WIDTH = 800
HEIGHT = 600
X_ONE = -WIDTH//2 + 15
X_TWO = WIDTH//2 - 25
SPEED = 0.04
PLAYER_ONE = (X_ONE,30)
PLAYER_TWO = (X_TWO,30)

# Entering the configuration for screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("A Game of Pong")
screen.tracer(0)
screen.listen()

# Starting each racket
racket1 = Racket(start_position=PLAYER_ONE)
racket2 = Racket(start_position=PLAYER_TWO)
ball = Ball()


screen.onkey(racket1.move_up,"w")
screen.onkey(racket1.move_down,"s")
screen.onkey(racket2.move_up,"Up")
screen.onkey(racket2.move_down,"Down")
# screen.onkey(racket2.move_up,"w")
# screen.onkey(racket2.move_down,"s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SPEED)
    ball.move()


screen.exitonclick()