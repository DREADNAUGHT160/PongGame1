# importing area
from turtle import Turtle, Screen
from pad import Paddle
from ball import Ball
from score import Score
import time

# screen class calling
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong game")
screen.listen()
screen.tracer(0)

# setting a divider
divider = Turtle()
divider.goto(0, 300)
divider.pencolor("white")
divider.setheading(270)
divider.goto(0, -300)

# paddle setting
user_paddle = Paddle(370, 0)
ai_paddle = Paddle(-370, 0)

# score setting
ball = Ball()

# score setting
ai_score = Score(-200)
user_score = Score(200)

# controlling the right paddle
screen.onkeypress(user_paddle.go_up, "Up")
screen.onkeypress(user_paddle.go_down, "Down")

# controlling the left paddle
screen.onkeypress(ai_paddle.go_up, "w")
screen.onkeypress(ai_paddle.go_down, "s")

# game over command
screen.onkeypress(user_score.game_over, "e")

# while loop for game repeatability
while user_score.game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    # detect the boarders
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.y_bounce()

    # detect the paddles
    if ball.distance(user_paddle) < 50 and ball.xcor() > 350 or ball.distance(ai_paddle) < 60 and ball.xcor() > -350:
        ball.x_bounce()

    # detect if the ball miss the paddle
    if ball.xcor() > 400:
        ai_score.add_score()
        ball.ball_reset()
    if ball.xcor() < -400:
        user_score.add_score()
        time.sleep(.1)
        ball.ball_reset()

screen.exitonclick()
