import turtle

import pandas as pd


def get_mouse_click_coordinate(x, y):
    print(x, y)


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coordinate)

states_data = pd.read_csv("50_states.csv")
print(states_data)  # Test

game_over = False
while not game_over:
    user_answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    print(user_answer)

turtle.mainloop()
