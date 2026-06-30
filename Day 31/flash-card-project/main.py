from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
IMG_W, IMG_H = 800, 526
FONT = ("Verdana", 60, "bold")

# with open("./data/french_words.csv") as data_file:
#     content = data_file.readlines()
#     print(content)

data = pd.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text = "French")
    canvas.itemconfig(card_word, text = current_card["French"])


window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)


canvas = Canvas(width=IMG_W, height=IMG_H)

front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(IMG_W/2, IMG_H/2, image=front_image)
card_title = canvas.create_text(IMG_W/2, 150, text="Title", font=FONT)
card_word = canvas.create_text(IMG_W/2, IMG_H/2, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
right_button = Button(image=check_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()