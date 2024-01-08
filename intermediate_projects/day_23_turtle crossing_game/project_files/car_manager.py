import random
from turtle import Turtle

from constants import *


def generate_position():
    x_pos_coefficient = random.randint(0, 12)
    x_pos = CAR_MIN_STARTING_X_POS + X_POSITION_SCALE_FACTOR * x_pos_coefficient * CAR_DIMENSIONS[0]
    y_pos_coefficient = random.randint(1, 13)
    y_pos = CAR_MIN_STARTING_Y_POS + Y_POSITION_SCALE_FACTOR * y_pos_coefficient * CAR_DIMENSIONS[1]
    return x_pos, y_pos


def generate_car():
    car = Turtle()
    car.shape(CAR_SHAPE)
    car.penup()
    car.setheading(LEFT)
    car.goto(generate_position())
    car.color(random.choice(COLORS))
    car.shapesize(stretch_wid=WIDTH_STRETCH_CONSTANT, stretch_len=LENGTH_STRETCH_CONSTANT)
    return car


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        for count in range(NUMBER_OF_CARS):
            car = generate_car()
            self.car_list.append(car)

    def start_traffic(self):
        for car in self.car_list:
            if car.xcor() > -SCREEN_WIDTH / 2:
                car.forward(self.car_speed)
            else:
                car.goto(generate_position())
                car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def check_collision(self, player):
        for car in self.car_list:
            if car.distance(player) < COLLISION_DISTANCE:
                return False
        return True
