import time
from turtle import Screen, Turtle

from ball import Ball
from constants import *
from paddle import Paddle
from scoreboard import Scoreboard


def initialize_turtle():
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, - SCREEN_HEIGHT / 2)
    turtle.setheading(UP)
    turtle.pencolor(PEN_COLOR)
    turtle.pensize(PEN_SIZE)
    return turtle


def draw_center_line():
    """Draws a dashed line using turtle graphics."""
    center_line_turtle = initialize_turtle()
    for i in range(int(SCREEN_HEIGHT / (2 * CENTER_LINE_HEIGHT))):
        center_line_turtle.forward(CENTER_LINE_HEIGHT)
        center_line_turtle.pu()
        center_line_turtle.forward(CENTER_LINE_HEIGHT)
        center_line_turtle.pd()


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)  # Set window title
screen.tracer(0)  # Turn off animation

draw_center_line()
right_paddle = Paddle(x_pos=RIGHT_PADDLE_X_POS, y_pos=PADDLE_Y_POS)
left_paddle = Paddle(x_pos=LEFT_PADDLE_X_POS, y_pos=PADDLE_Y_POS)
ball = Ball()
ball.start(x_pos=BALL_STARTING_X_POSITION, y_pos=BALL_STARTING_Y_POSITION)
left_scoreboard = Scoreboard(LEFT_SCOREBOARD_POS)
right_scoreboard = Scoreboard(RIGHT_SCOREBOARD_POS)
final_scoreboard = Scoreboard((0, 0))
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
    if (ball.distance(right_paddle) < 50 and ball.xcor() > RIGHT_PADDLE_X_POS - SEGMENT_DIMENSIONS[0]) or (
            ball.distance(left_paddle) < 50 and ball.xcor() < LEFT_PADDLE_X_POS + SEGMENT_DIMENSIONS[0]):
        ball.increase_speed()
        ball.bounce_from_paddle()
    if ball.xcor() > SCREEN_WIDTH / 2:
        left_scoreboard.increment_score()
        left_scoreboard.update_score()
        ball.start(x_pos=BALL_STARTING_X_POSITION, y_pos=BALL_STARTING_Y_POSITION)
        if left_scoreboard.score >= MATCH_POINT:
            game_over = True
            final_scoreboard.game_over(message="Left Player Wins!", position=FINAL_SCOREBOARD_LEFT_POS)

    if ball.xcor() < -SCREEN_WIDTH / 2:
        right_scoreboard.increment_score()
        right_scoreboard.update_score()
        ball.start(x_pos=BALL_STARTING_X_POSITION, y_pos=BALL_STARTING_Y_POSITION)
        if right_scoreboard.score >= MATCH_POINT:
            game_over = True
            final_scoreboard.game_over(message="Right Player Wins!", position=FINAL_SCOREBOARD_RIGHT_POS)

screen.exitonclick()
