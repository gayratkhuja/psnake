import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if food.distance(snake.ret_pos()) < 15:
        food.refresh()
        snake.get_fat()
        score_board.update_score()

    # Detect collision with wall
    if snake.ret_pos().xcor() > 280 or snake.ret_pos().xcor() < -280 or snake.ret_pos().ycor() > 280 or snake.ret_pos().ycor() < -280:
        score_board.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.ret_pos().distance(segment) < 10:
            score_board.game_over()
            game_is_on = False

screen.exitonclick()
