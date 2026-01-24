import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from board import Board


# Starting screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross Game")
screen.tracer(0)

board = Board()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Generate random cars along the way every 6th iteration
    car_manager.create_car()
    
    #Moving the cars
    car_manager.move_cars()

    #Detecting collision with the turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 19:
            scoreboard.game_over()
            game_is_on = False

    #Checking if turtle reached final line
    if player.is_at_finish_line():
        print("You have crossed the road!")
        scoreboard.increase_level()
        player.goto_start()
        car_manager.level_up()


screen.exitonclick()