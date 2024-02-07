import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

WINDOW_TITLE = "Pomodoro"
WINDOW_PADX = 100
WINDOW_PADY = 50
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224
CANVAS_CENTER_OFFSET = 3

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title(WINDOW_TITLE)
window.config(padx=WINDOW_PADX, pady=WINDOW_PADY)

canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
tomato_image = tk.PhotoImage(file="assets/images/tomato.png")
canvas.create_image(CANVAS_WIDTH / 2 + CANVAS_CENTER_OFFSET, CANVAS_HEIGHT / 2, image=tomato_image)
canvas.pack()

window.mainloop()
