import time
from turtle import Screen

from ball import Ball
from constants import *
from net import Net
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)  # Set window title
screen.tracer(0)  # Turn off animation

net = Net()
net.draw_net()
right_paddle = Paddle(position=RIGHT_PADDLE_POSITION)
left_paddle = Paddle(position=LEFT_PADDLE_POSITION)
ball = Ball()
ball.start(position=BALL_STARTING_POSITION)
left_scoreboard = Scoreboard(position=LEFT_SCOREBOARD_POS)
right_scoreboard = Scoreboard(position=RIGHT_SCOREBOARD_POS)
final_scoreboard = Scoreboard(FINAL_SCOREBOARD_STARTING_POS)
final_scoreboard.clear()

# Setup keyboard bindings for snake control
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(left_paddle.up, "W")
screen.onkeypress(left_paddle.down, "S")

game_over = False

while not game_over:
    screen.update()  # Update the screen with changes
    time.sleep(0.05)
    ball.move()
    if ball.ycor() > BALL_BOUNCING_WALL_BORDER or ball.ycor() < -BALL_BOUNCING_WALL_BORDER:
        ball.bounce_from_wall()
    if (ball.distance(right_paddle) < BALL_PADDLE_MAX_DISTANCE and ball.xcor() > RIGHT_PADDLE_POSITION[0] - SEGMENT_DIMENSIONS[0]) or (
            ball.distance(left_paddle) < BALL_PADDLE_MAX_DISTANCE and ball.xcor() < LEFT_PADDLE_POSITION[0] + SEGMENT_DIMENSIONS[0]):
        ball.increase_speed()
        ball.bounce_from_paddle()
    if ball.xcor() > SCREEN_WIDTH / 2:
        left_scoreboard.increment_score()
        left_scoreboard.update_score()
        ball.start(position=BALL_STARTING_POSITION)
        if left_scoreboard.score >= MATCH_POINT:
            game_over = True
            final_scoreboard.game_over(message="Left Player Wins!", position=FINAL_SCOREBOARD_LEFT_POS)

    if ball.xcor() < -SCREEN_WIDTH / 2:
        right_scoreboard.increment_score()
        right_scoreboard.update_score()
        ball.start(position=BALL_STARTING_POSITION)
        if right_scoreboard.score >= MATCH_POINT:
            game_over = True
            final_scoreboard.game_over(message="Right Player Wins!", position=FINAL_SCOREBOARD_RIGHT_POS)

screen.exitonclick()
