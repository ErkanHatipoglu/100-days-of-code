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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title(WINDOW_TITLE)
window.config(padx=WINDOW_PADX, pady=WINDOW_PADY, bg=YELLOW)

canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="assets/images/tomato.png")
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=tomato_image)
canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + TEXT_VERTICAL_OFFSET, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.pack()

window.mainloop()
