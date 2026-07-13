from tkinter import *
import pandas as pd
import random



BACKGROUND_COLOR = "#B1DDC6"
IMG_W, IMG_H = 800, 526
FONT = ("Verdana", 60, "bold")
FLIP_TIME = 3000

to_learn = []

try:
    data = pd.read_csv("./data/french_words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict("records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if not to_learn:
        canvas.itemconfig(card_title, text="Done!", fill="black")
        canvas.itemconfig(card_word, text="You've learned all the words!", fill="black")
        canvas.itemconfig(card_background, image=front_image)
        return
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(FLIP_TIME, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image=back_image)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/french_words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(FLIP_TIME, flip_card)

canvas = Canvas(width=IMG_W, height=IMG_H)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(IMG_W/2, IMG_H/2, image=front_image)
card_title = canvas.create_text(IMG_W/2, 150, text="Title", font=FONT)
card_word = canvas.create_text(IMG_W/2, IMG_H/2, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)



cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
right_button = Button(image=check_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()