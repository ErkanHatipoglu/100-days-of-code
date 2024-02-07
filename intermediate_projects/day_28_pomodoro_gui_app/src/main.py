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
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title(WINDOW_TITLE)

canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
tomato_image = tk.PhotoImage(file="assets/images/tomato.png")
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=tomato_image)
canvas.pack()

window.mainloop()
