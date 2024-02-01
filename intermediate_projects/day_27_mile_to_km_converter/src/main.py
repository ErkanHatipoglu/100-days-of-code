import tkinter

LABEL_FONT = ("Arial", 12, "italic")
WINDOW_TITLE_TEXT = "Mile to km Converter"
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 100
PAD_X = 20
PAD_Y = 20
MILES_TO_KM_COEFFICIENT = 1.609344


def convert_miles_to_km():
    miles = float(miles_input.get())
    km_result_label["text"] = round((MILES_TO_KM_COEFFICIENT * miles), 2)


window = tkinter.Tk()
window.title(WINDOW_TITLE_TEXT)
window.minsize(WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(padx=PAD_X, pady=PAD_Y)

equals_label = tkinter.Label(text="is equal to", font=LABEL_FONT)
equals_label.grid(column=0, row=1)

miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

km_result_label = tkinter.Label(text="0", font=LABEL_FONT)
km_result_label.grid(column=1, row=1)

calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

miles_label = tkinter.Label(text="miles", font=LABEL_FONT)
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="km", font=LABEL_FONT)
km_label.grid(column=2, row=1)

window.mainloop()