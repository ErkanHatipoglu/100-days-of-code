import math
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
TEXT_VERTICAL_OFFSET = 18

reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    working_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    reps += 1
    if reps > 8:
        reps = 1
        level_tracking_label.config(text="")
    if reps == 8:
        count_down(long_break_seconds)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(working_seconds)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes_remaining = math.floor(count / 60)
    if minutes_remaining < 10:
        minutes_remaining = f"0{minutes_remaining}"
    seconds_remaining = count % 60
    if seconds_remaining < 10:
        seconds_remaining = f"0{seconds_remaining}"
    canvas.itemconfig(timer_text, text=f"{minutes_remaining}:{seconds_remaining}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            level_tracking_label_text = level_tracking_label.__getitem__("text") + "✔"
            level_tracking_label.config(text=level_tracking_label_text)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title(WINDOW_TITLE)
window.config(padx=WINDOW_PADX, pady=WINDOW_PADY, bg=YELLOW)

title_label = tk.Label(bg=YELLOW, fg=GREEN)
title_label.config(text="Timer", font=(FONT_NAME, 34, "normal"))
title_label.grid(row=0, column=1)

canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="assets/images/tomato.png")
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=tomato_image)
timer_text = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + TEXT_VERTICAL_OFFSET, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button()
start_button.config(text="Start", bg="white", fg="blue", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button()
reset_button.config(text="Reset", bg="white", fg="blue")
reset_button.grid(row=2, column=2)

level_tracking_label = tk.Label()
level_tracking_label.config(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "normal"))
level_tracking_label.grid(row=4, column=1)

window.mainloop()
