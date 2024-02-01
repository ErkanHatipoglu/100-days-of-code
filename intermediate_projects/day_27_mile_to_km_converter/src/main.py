import tkinter

# Constants for styling and configuration
LABEL_FONT = ("Arial", 12, "italic")
WINDOW_TITLE_TEXT = "Miles to km Converter"
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 100
PAD_X = 20
PAD_Y = 20
MILES_TO_KM_COEFFICIENT = 1.609344  # Conversion coefficient from miles to kilometers


def convert_miles_to_km():
    """
    Convert the value from miles to kilometers.

    This function retrieves the input value (assumed to be in miles), converts it to kilometers,
    and updates the km_result_label's text to show the result.
    """
    miles = float(miles_input.get())  # Retrieve and convert the input from the miles_input Entry widget to float
    km_result_label["text"] = round((MILES_TO_KM_COEFFICIENT * miles),
                                    2)  # Calculate, round off to 2 decimal places, and display in km_result_label


# Setting up the main window
window = tkinter.Tk()
window.title(WINDOW_TITLE_TEXT)
window.minsize(WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(padx=PAD_X, pady=PAD_Y)  # Configure padding for the window

# Creating and placing the 'equals' label in the grid
equals_label = tkinter.Label(text="is equal to", font=LABEL_FONT)
equals_label.grid(column=0, row=1)

# Input for miles
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

# Label to display the result in kilometers
km_result_label = tkinter.Label(text="0", font=LABEL_FONT)
km_result_label.grid(column=1, row=1)

# Button to trigger the conversion
calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

# Label for 'miles' unit next to the input
miles_label = tkinter.Label(text="miles", font=LABEL_FONT)
miles_label.grid(column=2, row=0)

# Label for 'km' unit next to the result
km_label = tkinter.Label(text="km", font=LABEL_FONT)
km_label.grid(column=2, row=1)

# Run the application
window.mainloop()
