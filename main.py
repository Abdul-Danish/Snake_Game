# snake game (Day- 20-21):
import random
from turtle import Turtle, Screen
import scoreboard
import time
import snake
import food


screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = scoreboard.ScoreBoard()

food = food.Food()

# x_coordinates = [(0, 0), (-20, 0), (-40, 0)]
# segments = []

snake = snake.Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")


still_alive = True
while still_alive:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collition with food
    if snake.segments[0].distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detect collition with wall
    if snake.segments[0].xcor() > 380 or snake.segments[0].xcor() < -380 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.update_highscore()
        scoreboard.reset()
        snake.reset()

    # Detect collition with tail
    for segment in snake.segments[2:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.update_highscore()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
