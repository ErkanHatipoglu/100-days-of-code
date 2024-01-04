import time
from turtle import Screen, Turtle

from ball import Ball
from constants import *
from paddle import Paddle


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
ball = Ball(x_pos=0, y_pos=0)
ball.start()

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
    time.sleep(0.01)
    ball.move()
    if ball.ycor() > BALL_BOUNCING_BORDER or ball.ycor() < -BALL_BOUNCING_BORDER:
        ball.setheading(-ball.heading())
screen.exitonclick()
