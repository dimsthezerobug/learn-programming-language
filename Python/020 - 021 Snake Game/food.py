from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#5174E8")
        self.speed(0)
        self.change_position()

    def change_position(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)
