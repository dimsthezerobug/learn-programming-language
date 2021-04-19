import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Wich turtle will win the race? Enter color: ")
colors = ["red", "orange", "yellow", "green", "purple", "blue"]
y_position = [-125, -75, -25, 25, 75, 125]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 221.5:
            is_race_on = False
            the_winner = turtle.pencolor()
            if user_bet == the_winner:
                print(f"You've won, {the_winner} turtle is the winner!")
            else:
                print(f"You've los, {the_winner} turtle is the winner!")

screen.exitonclick()
