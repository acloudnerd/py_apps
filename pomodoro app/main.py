import math
from tkinter import *
from PIL import Image, ImageTk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT_TUPLE = (FONT_NAME, 50, "bold")
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global  reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=YELLOW, font=(FONT_NAME, 50, "bold"), bg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Busy Working", fg=RED, font=(FONT_NAME, 50, "bold"), bg=PINK)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor((reps + 1) / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Lufuno-ro")
window.config(padx=100, pady=10, bg=PINK)
window.resizable(False, False)

title_label = Label(text="Timer", fg=RED, font=(FONT_NAME, 50, "bold"), bg=PINK)
title_label.grid(column=1, row=0)

CANVAS_W, CANVAS_H = 200, 250

canvas = Canvas(width=CANVAS_W, height=CANVAS_H, bg=PINK, highlightthickness=0)
pil_img = Image.open("baby_lufuno_bg_removed.png").resize((CANVAS_W, CANVAS_H)).convert("RGBA")
background = Image.new("RGBA", (CANVAS_W, CANVAS_H), PINK)
background.paste(pil_img, mask=pil_img.split()[3])
lufuno_img = ImageTk.PhotoImage(background.convert("RGB"))
canvas.create_image(CANVAS_W // 2, CANVAS_H // 2, image=lufuno_img)
timer_text = canvas.create_text(CANVAS_W // 2, CANVAS_H // 2 + 50, text="00:00", font=FONT_TUPLE, fill=RED)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=1)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=1)

check_marks = Label(fg=GREEN, bg=PINK, highlightthickness=0)
check_marks.grid(column=1, row=2)

window.mainloop()
