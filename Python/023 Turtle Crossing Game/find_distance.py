from turtle import Turtle, Screen

screen = Screen()

car = Turtle("square")
car.shapesize(1, 2)
car.goto(30, 0)

turtle = Turtle("turtle")
turtle.left(90)
turtle.forward(10)

print(turtle.distance(car))


screen.exitonclick()
