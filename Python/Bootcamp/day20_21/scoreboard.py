from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        file_path = os.getcwd() + "\\Python\\Bootcamp\\day20_21\\data.txt"
        with open(file_path) as file:
            self.high_score = file.read()
        print(self.high_score)
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            file_path = os.getcwd() + "\\Python\\Bootcamp\\day20_21\\data.txt"
            with open(file_path, mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.home()
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)


        