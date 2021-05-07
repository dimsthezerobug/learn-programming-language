from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ularnya Dimas")

food = Food()
snake = Snake()
scoreboard = ScoreBoard()


game_is_on = True
screen.listen()
while game_is_on:
    snake.move()
    screen.onkey(snake.right, "d")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.change_position()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    top = snake.head.ycor() > 280
    bottom = snake.head.ycor() < -280
    right = snake.head.xcor() > 280
    left = snake.head.xcor() < -280
    collision_with_wall = top or bottom or right or left
    if collision_with_wall:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
