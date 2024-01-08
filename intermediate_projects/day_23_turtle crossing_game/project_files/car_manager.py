from car import Car

from constants import *


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        for count in range(NUMBER_OF_CARS):
            car = Car()
            self.car_list.append(car)

    def start_traffic(self):
        for car in self.car_list:
            if car.xcor() > -SCREEN_WIDTH / 2:
                car.forward(self.car_speed)
            else:
                car.goto(Car.generate_position())
                car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def check_collision(self, player):
        for car in self.car_list:
            if car.distance(player) < COLLISION_DISTANCE:
                return False
        return True
