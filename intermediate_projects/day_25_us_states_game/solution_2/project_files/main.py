import turtle

import pandas as pd

# Constants for game configuration
SCREEN_TITLE = "US States Game"
TEXT_INPUT_PROMPT = "What's another state's name?"
IMAGE_FILE_PATH = "blank_states_img.gif"
INPUT_FILE_PATH = "50_states.csv"
OUTPUT_FILE_PATH = "states_to_learn.csv"
NUMBER_OF_STATES = 50
EXIT_CONDITIONS = [None, "exit", "Exit", "EXIT", "quit", "Quit", "QUIT"]
STATE_COLUMN = "state"
X_COLUMN = "x"
Y_COLUMN = "y"


def get_mouse_click_coordinate(x, y):
    """
    Print the x and y coordinates of a mouse click on the screen.
    Intended for debugging and setup, not used in the main game logic.

    Args:
        x (int): The x-coordinate of the mouse click.
        y (int): The y-coordinate of the mouse click.
    """
    print(x, y)


def display_state(s_name, x_pos, y_pos):
    """
    Display a state's name on the map at the specified coordinates.

    Args:
        s_name (str): The name of the state.
        x_pos (int): The x-coordinate on the map where the state name will be displayed.
        y_pos (int): The y-coordinate on the map where the state name will be displayed.
    """
    state_label_writer = turtle.Turtle()
    state_label_writer.hideturtle()
    state_label_writer.penup()
    state_label_writer.goto(x_pos, y_pos)
    state_label_writer.write(arg=s_name.title(), move=False)


# Set up the screen with the map image
screen = turtle.Screen()
screen.title(SCREEN_TITLE)
image = IMAGE_FILE_PATH
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coordinate)

# Load the data about states from a CSV file
states_data = pd.read_csv(INPUT_FILE_PATH)
states_list = []  # List to keep track of correctly guessed states
correct_answer_count = 0
total_state_number = len(states_data)
game_over = False

# Main game loop
while not game_over:
    # Check if all states have been guessed
    if len(states_list) < NUMBER_OF_STATES:
        # Show the current score and ask the user for their guess
        user_answer = screen.textinput(title=f"{correct_answer_count}/{total_state_number} States Correct",
                                       prompt=TEXT_INPUT_PROMPT)
        # Allow the user to exit the game
        if user_answer in EXIT_CONDITIONS:
            game_over = True
        else:
            # Format the user's answer to match the data format
            user_answer = user_answer.title()

        # Check if the answer is correct (exists in the dataset)
        correct_guess = states_data[states_data[STATE_COLUMN] == user_answer].index.size > 0
        if correct_guess:
            # Avoid counting the same correct guess more than once
            if user_answer not in states_list:
                # Add the correct guess to the list and update the score
                states_list.append(user_answer)
                correct_answer_count += 1
                # Retrieve and display the state's name and position on the map
                index = states_data[states_data[STATE_COLUMN] == user_answer].index[0]
                state_name = states_data.at[index, STATE_COLUMN]
                x_position = states_data.at[index, X_COLUMN]
                y_position = states_data.at[index, Y_COLUMN]
                display_state(state_name, x_position, y_position)
    else:
        # End the game if all states have been guessed
        game_over = True

# Create a DataFrame of states that weren't correctly guessed
states_to_learn = states_data.copy()

# Remove the states that were correctly guessed from the DataFrame
for state_key in states_list:
    state_index = states_data[states_data[STATE_COLUMN] == state_key].index[0]
    states_to_learn.drop(index=state_index, axis=0, inplace=True)

# Save the states that need to be learned to a CSV file
states_to_learn.to_csv(OUTPUT_FILE_PATH, index=False)
