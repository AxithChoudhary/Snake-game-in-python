import time
from turtle import Turtle, Screen
from food import Food
from score import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Down", fun=snake.move_down)
screen.update()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.HEAD.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    if snake.HEAD.ycor() > 270 or snake.HEAD.ycor() < -290 or snake.HEAD.xcor() > 290 or snake.HEAD.xcor() < -290:
        # is_game_on = False
        score.restart()
        snake.restart()


    for pos in range(1, len(snake.segments)):
        if snake.HEAD.position() == snake.segments[pos].position():
            # is_game_on = False
            score.restart()
            snake.restart()



screen.exitonclick()
