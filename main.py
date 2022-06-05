from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
import random
from scoreboard import Scoreboard

screen_length = 600

snake = Snake("blue")
food = Food(screen_length)
scoreboard = Scoreboard()
screen = Screen()
screen.colormode(255)
screen.setup(width=screen_length, height=screen_length)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)                                        # make our game update when we tell it to, will make our animation smoother
                                                        # With tracer set to zero, we will only update on command, when we call screen.update()

screen.listen()

screen.onkey(snake.up, "Up")                            # We check for key movement
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

playing = True
while playing:
    snake.move()

    if snake.does_eat(food):
        food.reset()
        food.hideturtle()
        food = Food(screen_length)
        snake.add_square()
        scoreboard.add_to_score()

    if snake.is_out_of_bounds(screen_length):
        playing = False
    
    if snake.does_crash():
        playing = False
    
    screen.update()                             # We only want to update after every square has been moved to make our animation smoother
    time.sleep(.1)                              # Slow down our snake

score = scoreboard.get_score()
final_score = Turtle()
final_score.color('white')
final_score.penup()
final_score.write(f"You've Lost! Final Score: {score}", align="center", font=("Courier", 28, "normal"))

screen.exitonclick()
