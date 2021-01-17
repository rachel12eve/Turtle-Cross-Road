import time
from turtle import Screen
from player import Player
from car_manager import CarManager

from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
speed=0.1

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    carmanager.create_car()
    carmanager.car_movement()

    for car in carmanager.all_cars:
        if car.distance(player)<=21:
            print(car.distance(player))
            scoreboard.game_over()
            time.sleep(0.8)
            game_is_on=False


    if player.ycor()==280:
        player.restart()
        scoreboard.add_score()
        if scoreboard.score > 1 and scoreboard.score % 2 == 0:
            speed *= 0.8
            print(speed)






screen.onclick()

