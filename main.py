from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

# Game constants
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
SCREENSIZE = 600
DELAY = 0.1
speed_factor = 1

# setup screen
screen = Screen()
screen.setup(width=SCREENSIZE, height=SCREENSIZE)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create the snake
snake = Snake(start_pos=STARTING_POSITIONS, default_step=MOVE_STEP)

# Create food
food = Food(screensize=SCREENSIZE, default_step=MOVE_STEP)

# Create a scoreboard
score = Score(screensize=SCREENSIZE, default_step=MOVE_STEP)

game_over = False
while not game_over:
    screen.update()
   
    # move the snake
    snake.move()

    # Control direction
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Left", fun=snake.left)

    # Detect collision with the food
    if snake.head.distance(food) < 10: 
        score.increase_score()
        food.position_food()
        snake.increase_snake_size()
   
    # Detect collision with the wall
    if round(snake.head.xcor(),0) == -SCREENSIZE/2 or round(snake.head.xcor(),0) == SCREENSIZE/2 or round(snake.head.ycor(),0) == -SCREENSIZE/2 or round(snake.head.ycor(),0) == SCREENSIZE/2:
        game_over = True
        score.game_over()

    # # detect collision with tail/body
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 5:
            game_over = True
            score.game_over()

    # increase speed as the score increases
    if score.score % 5 == 0:
        speed_factor = 1 - score.score/50
        print(speed_factor, DELAY*speed_factor)
    time.sleep(DELAY*speed_factor)

screen.exitonclick()