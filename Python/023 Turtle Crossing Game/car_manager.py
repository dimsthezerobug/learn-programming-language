from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    # buat objek yang berjalan sendiri
    def __init__(self):
        self.all_cars = []

    def make_car(self):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(1, 2)
        # random_x = random.randrange(300, 445, 45)
        random_y = random.randrange(-250, 250, 25)
        car.speed(0)
        car.goto(340, random_y)
        self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            if car.xcor() < -340:
                self.all_cars.remove(car)
            car.backward(10)
