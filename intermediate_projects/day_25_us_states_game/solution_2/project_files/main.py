import turtle

import pandas as pd

SCREEN_TITLE = "US States Game"
TEXT_INPUT_PROMPT = "What's another state's name?"
IMAGE_ADDRESS = "blank_states_img.gif"
STATES_CSV_FILE_ADDRESS = "50_states.csv"
NUMBER_OF_STATES = 50
EXIT_CONDITIONS = [None, "exit", "Exit", "EXIT", "quit", "Quit", "QUIT"]
STATE_COLUMN = "state"
X_COLUMN = "x"
Y_COLUMN = "y"


def get_mouse_click_coordinate(x, y):
    print(x, y)


def display_state(s_name, x_pos, y_pos):
    state_label_writer = turtle.Turtle()
    state_label_writer.hideturtle()
    state_label_writer.penup()
    state_label_writer.goto(x_pos, y_pos)
    state_label_writer.write(arg=s_name.title(), move=False)


screen = turtle.Screen()
screen.title(SCREEN_TITLE)
image = IMAGE_ADDRESS
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coordinate)

states_data = pd.read_csv(STATES_CSV_FILE_ADDRESS)
states_list = []
correct_answer_count = 0
total_state_number = len(states_data)
game_over = False

while not game_over:
    if len(states_list) < NUMBER_OF_STATES:
        user_answer = screen.textinput(title=f"{correct_answer_count}/{total_state_number} States Correct",
                                       prompt=TEXT_INPUT_PROMPT)
        if user_answer in EXIT_CONDITIONS:
            game_over = True
        else:
            user_answer = user_answer.title()

        correct_guess = states_data[states_data[STATE_COLUMN] == user_answer].index.size > 0
        if correct_guess:
            if user_answer not in states_list:
                states_list.append(user_answer)
                correct_answer_count += 1
                index = states_data[states_data[STATE_COLUMN] == user_answer].index[0]
                state_name = states_data.at[index, STATE_COLUMN]
                x_position = states_data.at[index, X_COLUMN]
                y_position = states_data.at[index, Y_COLUMN]
                display_state(state_name, x_position, y_position)
    else:
        game_over = True

states_to_learn = states_data.copy()

for state_key in states_list:
    state_index = states_data[states_data[STATE_COLUMN] == state_key].index[0]
    states_to_learn.drop(index=state_index, axis=0, inplace=True)
states_to_learn.to_csv('states_to_learn.csv', index=False)