FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-260,260)
        self.hideturtle()
        self.write(f"Level: {self.score}",align="left", font=FONT)

    def add_score(self):
        self.score+=1
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        over=Turtle()
        over.color("black")
        over.hideturtle()
        over.write("GAME OVER", align="center", font=FONT)
