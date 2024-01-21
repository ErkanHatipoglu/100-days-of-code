import turtle
import pandas as pd

# Constants for the game
SCREEN_TITLE = "US States Game"
TEXT_INPUT_PROMPT = "What's another state's name?"
IMAGE_FILE_PATH = "blank_states_img.gif"
INPUT_FILE_PATH = "50_states.csv"
OUTPUT_FILE_PATH = "states_to_learn.csv"
TEXT_INPUT_INITIAL_TITLE = "Guess the State"
EXIT_CONDITIONS = [None, "exit", "Exit", "EXIT", "quit", "Quit", "QUIT"]
STATE_COLUMN = "state"
X_COLUMN = "x"
Y_COLUMN = "y"


def get_mouse_click_coordinate(x, y):
    """
    Print the x, y coordinates of a mouse click on the screen.

    Args:
        x (int): The x-coordinate of the mouse click.
        y (int): The y-coordinate of the mouse click.
    """
    print(x, y)


def get_key(dictionary, dict_value):
    """
    Get the key for a given value in a dictionary.

    Args:
        dictionary (dict): The dictionary to search.
        dict_value (Any): The value for which to find the corresponding key.

    Returns:
        The key corresponding to the given value, if found. None otherwise.
    """
    for key, value in dictionary.items():
        if dictionary[key] == dict_value:
            return key


def extract_result(dictionary, dict_value):
    """
    Extract the result from the dictionary based on the provided value.
    Removes the corresponding entry from the state, x, and y columns in the dictionary.

    Args:
        dictionary (dict): The dictionary containing state, x, and y columns.
        dict_value (Any): The value to search for in the state column.

    Returns:
        tuple: Updated dictionary, x position, and y position.
    """
    dictionary_key = get_key(dictionary[STATE_COLUMN], dict_value)
    x_pos = dictionary[X_COLUMN].get(dictionary_key)
    y_pos = dictionary[Y_COLUMN].get(dictionary_key)
    for _ in [STATE_COLUMN, X_COLUMN, Y_COLUMN]:
        dictionary[_].pop(dictionary_key)
    return dictionary, x_pos, y_pos


def check_user_answer(answer):
    """
    Check the user's answer. Determine if the game should end based on the answer.

    Args:
        answer (str): The user's answer.

    Returns:
        tuple: The user's answer (formatted) and a boolean indicating whether the game should end.
    """
    if answer in EXIT_CONDITIONS:
        return answer, True
    else:
        return answer.title(), False


def display_state(state_name, x_pos, y_pos):
    """
    Display the state name on the screen at the given x, y coordinates.

    Args:
        state_name (str): The name of the state to display.
        x_pos (int): The x-coordinate on the screen.
        y_pos (int): The y-coordinate on the screen.
    """
    state_label_writer = turtle.Turtle()
    state_label_writer.hideturtle()
    state_label_writer.penup()
    state_label_writer.goto(x_pos, y_pos)
    state_label_writer.write(arg=state_name, move=False)


# Setting up the screen for the turtle graphics
screen = turtle.Screen()
screen.title(SCREEN_TITLE)
image = IMAGE_FILE_PATH
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coordinate)

# Loading states data from a CSV file using pandas
states_data = pd.read_csv(INPUT_FILE_PATH)
correct_answer_count = 0
total_state_number = len(states_data)
states_dict = states_data.to_dict()

# Initial user interaction
user_answer = screen.textinput(title=TEXT_INPUT_INITIAL_TITLE, prompt=TEXT_INPUT_PROMPT)
user_answer, game_over = check_user_answer(user_answer)

# Check if the initial answer is correct
if user_answer in states_dict[STATE_COLUMN].values():
    correct_answer_count += 1
    states_dict, x_position, y_position = extract_result(states_dict, user_answer)
    display_state(user_answer, x_position, y_position)

# Main game loop
while not game_over:
    # Update the title to show the number of correct answers
    user_answer = screen.textinput(title=f"{correct_answer_count}/{total_state_number} States Correct",
                                   prompt=TEXT_INPUT_PROMPT)
    user_answer, game_over = check_user_answer(user_answer)

    # Check if the user's answer is correct
    if user_answer in states_dict[STATE_COLUMN].values():
        correct_answer_count += 1
        states_dict, x_position, y_position = extract_result(states_dict, user_answer)
        display_state(user_answer, x_position, y_position)

    # If all states are guessed correctly, end the game
    if correct_answer_count == total_state_number:
        game_over = True

# Export the states that were not guessed correctly to a CSV file
states_to_learn = pd.DataFrame(states_dict)
states_to_learn.to_csv(OUTPUT_FILE_PATH, index=False)

# Keep the screen open until manually closed
turtle.mainloop()
