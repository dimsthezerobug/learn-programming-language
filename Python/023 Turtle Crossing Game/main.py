import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

player = Player()
# player.make_player()

screen.listen()
screen.onkeypress(player.move, "Up")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    car_manager.make_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if player.distance(car) < 31:
            game_is_on = False

screen.exitonclick()
