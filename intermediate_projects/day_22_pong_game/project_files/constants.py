# Game screen constants
SCREEN_WIDTH = 800  # Width of the game screen in pixels
SCREEN_HEIGHT = 600  # Height of the game screen in pixels
SCREEN_COLOR = "black"  # Background color of the game screen
SCREEN_TITLE = "The Great Pong Game"  # Title of the game window
UP = 90  # Angle used for turtle graphics (pointing upwards)

# Paddle constants
PADDLE_COLOR = "white"  # Color of the paddles
PADDLE_SHAPE = "square"  # Shape of the paddles (turtle graphics)
SEGMENT_DIMENSIONS = (20, 20)  # Dimensions of paddle segments
PADDLE_SPEED = 20  # Movement speed of the paddles
RIGHT_PADDLE_POSITION = (350, 0)  # Starting position of the right paddle
LEFT_PADDLE_POSITION = (-350, 0)  # Starting position of the left paddle
PADDLE_MAX_Y_POSITION = 240  # Maximum Y position the paddle can move to
WIDTH_STRETCH_CONSTANT = 5  # Stretch factor for paddle width
LENGTH_STRETCH_CONSTANT = 1  # Stretch factor for paddle length

# Ball constants
BALL_COLOR = "white"  # Color of the ball
BALL_SHAPE = "circle"  # Shape of the ball (turtle graphics)
BALL_SPEED = 5  # Movement speed of the ball
BALL_STARTING_ANGLE_RANGE = 45  # Range of starting angles for the ball
BALL_BOUNCING_WALL_BORDER = 280  # Y-coordinate limit for ball bouncing
BALL_STARTING_POSITION = (0, 0)  # Starting position of the ball
RIGHT = 0  # Angle for ball movement to the right
LEFT = 180  # Angle for ball movement to the left
BALL_PADDLE_MAX_DISTANCE = 50  # Maximum distance for ball-paddle collision detection

# Scoreboard constants
PENCOLOR = "white"  # Color of the scoreboard text
LEFT_SCOREBOARD_POS = (-120, 260)  # Position of the left scoreboard
RIGHT_SCOREBOARD_POS = (100, 260)  # Position of the right scoreboard
FINAL_SCOREBOARD_LEFT_POS = (-330, 200)  # Final position of the final scoreboard if the winner is left paddle
FINAL_SCOREBOARD_RIGHT_POS = (50, 200)  # Final position of the final scoreboard if the winner is right paddle
FINAL_SCOREBOARD_STARTING_POS = (0, 0)  # Starting position of the final scoreboard
FONT = ('Arial', 25, 'bold')  # Font style for the scoreboard text
MATCH_POINT = 5  # Points required to win the match

# Net constants
PEN_COLOR = "white"  # Color for drawing elements like the net
PEN_SIZE = 5  # Size of the pen for drawing elements
CENTER_LINE_HEIGHT = 12  # Height of each segment of the center line (net)