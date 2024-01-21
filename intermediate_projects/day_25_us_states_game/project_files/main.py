import turtle

import pandas as pd

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
    print(x, y)


def get_key(dictionary, dict_value):
    for key, value in dictionary.items():
        if dictionary[key] == dict_value:
            return key


def extract_result(dictionary, dict_value):
    dictionary_key = get_key(dictionary[STATE_COLUMN], dict_value)
    x_pos = dictionary[X_COLUMN].get(dictionary_key)
    y_pos = dictionary[Y_COLUMN].get(dictionary_key)
    for _ in [STATE_COLUMN, X_COLUMN, Y_COLUMN]:
        dictionary[_].pop(dictionary_key)
    return dictionary, x_pos, y_pos


def check_user_answer(answer):
    if answer in EXIT_CONDITIONS:
        return answer, True
    else:
        return answer.title(), False


def display_state(state_name, x_pos, y_pos):
    state_label_writer = turtle.Turtle()
    state_label_writer.hideturtle()
    state_label_writer.penup()
    state_label_writer.goto(x_pos, y_pos)
    state_label_writer.write(arg=state_name, move=False)


screen = turtle.Screen()
screen.title(SCREEN_TITLE)
image = IMAGE_FILE_PATH
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coordinate)

states_data = pd.read_csv(INPUT_FILE_PATH)
correct_answer_count = 0
total_state_number = len(states_data)
states_dict = states_data.to_dict()

user_answer = screen.textinput(title=TEXT_INPUT_INITIAL_TITLE, prompt=TEXT_INPUT_PROMPT)

user_answer, game_over = check_user_answer(user_answer)

if user_answer in states_dict[STATE_COLUMN].values():
    correct_answer_count += 1
    states_dict, x_position, y_position = extract_result(states_dict, user_answer)
    display_state(user_answer, x_position, y_position)

while not game_over:
    user_answer = screen.textinput(title=f"{correct_answer_count}/{total_state_number} States Correct",
                                   prompt=TEXT_INPUT_PROMPT)
    user_answer, game_over = check_user_answer(user_answer)

    if user_answer in states_dict[STATE_COLUMN].values():
        correct_answer_count += 1
        states_dict, x_position, y_position = extract_result(states_dict, user_answer)
        display_state(user_answer, x_position, y_position)
    if correct_answer_count == total_state_number:
        game_over = True
states_to_learn = pd.DataFrame(states_dict)
states_to_learn.to_csv(OUTPUT_FILE_PATH, index=False)
turtle.mainloop()
