# Game screen constants
SCREEN_WIDTH = 600  # Width of the game screen in pixels
SCREEN_HEIGHT = 600  # Height of the game screen in pixels
SCREEN_TITLE = "Turtle Crossing Game"  # Title of the game window
SCREEN_COLOR = "white"  # Background color of the game screen

# Player Constants
STARTING_POSITION = (0, -280)  # Initial position of the player
MOVE_DISTANCE = 10  # Distance the player moves in one keystroke
FINISH_LINE_Y = 280  # Y-coordinate of the finish line
PLAYER_DIMENSIONS = (20, 20)  # Dimensions of the player
PLAYER_SHAPE = "turtle"  # Shape of the player
UP = 90  # Angle for upward movement

# CarManager constants
STARTING_MOVE_DISTANCE = 5  # Initial move distance for cars
NUMBER_OF_CARS = 25  # Total number of cars in the game
COLLISION_DISTANCE = 30  # Distance for collision detection

# Scoreboard constants
FONT = ("Courier", 24, "normal")  # Font style for the scoreboard text
PEN_COLOR = "black"  # Pen color for the scoreboard text
SCOREBOARD_POSITION = (-280, 260)  # Position of the scoreboard
HOME = (-85, 0)  # Home position for certain text displays

# Car constants
CAR_SHAPE = "square"  # Shape of the cars
LEFT = 180  # Angle for leftward movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # Possible colors of the cars
WIDTH_STRETCH_CONSTANT = 1  # Width stretch factor for the car
LENGTH_STRETCH_CONSTANT = 2  # Length stretch factor for the car
MOVE_INCREMENT = 10  # Incremental increase in car movement speed
CAR_MIN_STARTING_X_POS = 300  # Minimum X starting position for a car
CAR_MIN_STARTING_Y_POS = -270  # Minimum Y starting position for a car
X_POSITION_SCALE_FACTOR = 1.5  # Scale factor for random X position
Y_POSITION_SCALE_FACTOR = 2  # Scale factor for random Y position
CAR_DIMENSIONS = (40, 20)  # Dimensions of the car
