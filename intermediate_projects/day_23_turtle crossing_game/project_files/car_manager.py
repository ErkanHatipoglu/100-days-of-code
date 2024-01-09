from car import Car

from constants import *


class CarManager:
    """
    Class to manage the behavior of multiple car objects in the game.
    This includes handling their movement, speed, and collision detection.
    """

    def __init__(self):
        """Initializes the CarManager with an empty list of cars and sets the initial car speed."""
        self.car_list = []  # List to store car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed for the cars

        # Creating the initial set of cars based on NUMBER_OF_CARS constant
        for count in range(NUMBER_OF_CARS):
            car = Car()
            self.car_list.append(car)

    def start_traffic(self):
        """
        Moves each car in the car list. If a car goes off-screen, it is reset to a new position.
        This simulates continuous traffic flow.
        """
        for car in self.car_list:
            if car.xcor() > -SCREEN_WIDTH / 2:
                car.forward(self.car_speed)
            else:
                car.goto(Car.generate_position())  # Reset car position
                car.forward(self.car_speed)

    def increase_speed(self):
        """Increases the moving speed of all cars, making the game more challenging."""
        self.car_speed += MOVE_INCREMENT

    def check_collision(self, player):
        """
        Checks if any car in the car list collides with the player.

        Args:
            player: The player object to check for collision.

        Returns:
            bool: False if any car collides with the player, True otherwise.
        """
        for car in self.car_list:
            if car.distance(player) < COLLISION_DISTANCE:
                return False
        return True
