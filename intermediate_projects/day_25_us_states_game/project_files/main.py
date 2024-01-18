import turtle


def get_mouse_click_coordinate(x, y):
    print(x, y)


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coordinate)

user_answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(user_answer)

turtle.mainloop()
