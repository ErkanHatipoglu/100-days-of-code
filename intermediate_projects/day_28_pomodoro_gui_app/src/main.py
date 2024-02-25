import math
import tkinter as tk
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
# Define the application's color scheme and time settings
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"  # Font style for the app
WORK_MIN = 25  # Duration of work period in minutes
SHORT_BREAK_MIN = 5  # Duration of short break in minutes
LONG_BREAK_MIN = 20  # Duration of long break in minutes

# Window configuration constants
WINDOW_TITLE = "Pomodoro"
WINDOW_PADX = 100
WINDOW_PADY = 50
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224
TEXT_VERTICAL_OFFSET = 18  # To center text vertically in the canvas

# Global variables
reps = 0  # Tracks the number of repetitions/work sessions completed
timer = None  # Reference to the window's timer


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Resets the timer to its initial state.
    """
    global reps
    window.after_cancel(timer)  # Cancel the ongoing timer
    title_label.config(text="Timer", fg=GREEN)  # Reset the title label
    level_tracking_label.config(text="")  # Clear the level tracking label
    canvas.itemconfig(timer_text, text="00:00")  # Reset the timer text
    reps = 0  # Reset the repetition counter


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Starts the timer mechanism based on the current session (work or break).
    """
    global reps
    working_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    reps += 1
    if reps > 8:
        reps = 1  # Reset reps after completing a full cycle
        level_tracking_label.config(text="")
    if reps == 8:
        count_down(long_break_seconds)  # Initiate long break
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)  # Initiate short break
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(working_seconds)  # Initiate work session
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
    Manages the countdown process for the timer.

    Args:
        count (int): The countdown time in seconds.
    """
    minutes_remaining = math.floor(count / 60)
    if minutes_remaining < 10:
        minutes_remaining = f"0{minutes_remaining}"
    seconds_remaining = count % 60
    if seconds_remaining < 10:
        seconds_remaining = f"0{seconds_remaining}"
    canvas.itemconfig(timer_text, text=f"{minutes_remaining}:{seconds_remaining}")  # Update timer display
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Schedule the next second
    else:
        # Display appropriate message at the end of work/break session
        if reps == 7:
            messagebox.showinfo("Time for a long break!", "20-minute break time! Stretch, relax, and refresh yourself.")
        elif reps % 2 == 0:
            messagebox.showinfo("Back to work!", "Break's over, let's get back to work!")
        else:  # Work session
            messagebox.showinfo("Time for a break!", "You've completed a session, time to take a short break.")
        start_timer()
        if reps % 2 == 0:
            level_tracking_label_text = level_tracking_label.__getitem__("text") + "✔"
            level_tracking_label.config(text=level_tracking_label_text)


# ---------------------------- UI SETUP ------------------------------- #
# Initialize the main window
window = tk.Tk()
window.title(WINDOW_TITLE)
window.config(padx=WINDOW_PADX, pady=WINDOW_PADY, bg=YELLOW)  # Window styling

# Timer label setup
title_label = tk.Label(bg=YELLOW, fg=GREEN)
title_label.config(text="Timer", font=(FONT_NAME, 34, "normal"))
title_label.grid(row=0, column=1)

# Canvas for tomato image and timer text
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="assets/images/tomato.png")  # Load tomato image
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=tomato_image)  # Display tomato image
timer_text = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + TEXT_VERTICAL_OFFSET, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))  # Timer text setup
canvas.grid(row=1, column=1)

# Start and reset buttons setup
start_button = tk.Button()
start_button.config(text="Start", bg="white", fg="blue", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button()
reset_button.config(text="Reset", bg="white", fg="blue", command=reset_timer)
reset_button.grid(row=2, column=2)

# Level tracking label setup
level_tracking_label = tk.Label()
level_tracking_label.config(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "normal"))
level_tracking_label.grid(row=4, column=1)

# Start the Tkinter event loop
window.mainloop()
