import turtle

import pandas as pd


def get_mouse_click_coordinate(x, y):
    print(x, y)


def get_key(dictionary, dict_value):
    for key, value in dictionary.items():
        if dictionary[key] == dict_value:
            return key


def extract_result(dictionary, dict_value):
    dictionary_key = get_key(dictionary["state"], dict_value)
    x_pos = dictionary["x"].get(dictionary_key)
    y_pos = dictionary["y"].get(dictionary_key)
    print(f"x position: {x_pos}, y position:{y_pos}")
    for _ in ["state", "x", "y"]:
        dictionary[_].pop(dictionary_key)
    return dictionary, x_pos, y_pos


def check_user_answer(answer):
    if answer is None:
        return answer, True
    else:
        return answer.lower(), False


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coordinate)

states_data = pd.read_csv("50_states.csv")
states_data["state"] = states_data["state"].str.lower()
correct_answer_count = 0
total_state_number = len(states_data)
states_dict = states_data.to_dict()

user_answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")

user_answer, game_over = check_user_answer(user_answer)

if user_answer in states_dict["state"].values():
    correct_answer_count += 1
    states_dict, x_position, y_position = extract_result(states_dict, user_answer)

while not game_over:
    user_answer = screen.textinput(title=f"{correct_answer_count}/{total_state_number} States Correct",
                                   prompt="What's another state's name?")
    user_answer, game_over = check_user_answer(user_answer)

    if user_answer in states_dict["state"].values():
        correct_answer_count += 1
        states_dict, x_position, y_position = extract_result(states_dict, user_answer)
    if correct_answer_count == total_state_number:
        game_over = True

turtle.mainloop()
