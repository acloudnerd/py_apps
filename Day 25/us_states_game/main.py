import turtle
from turtle import Turtle

import pandas as pd
from tkinter import PhotoImage

screen = turtle.Screen()

# Load image
image = PhotoImage(file="./blank_states_img.gif")

# Get image dimensions
width = image.width()
height = image.height()

# Resize turtle window
screen.setup(width, height)

#  Set background
screen.bgpic("./blank_states_img.gif")

# data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
# print(all_states)
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct state(s)",
                                    prompt="What the current state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        s = Turtle()
        s.hideturtle()
        s.penup()
        state_data = data[data.state == answer_state]
        s.goto(state_data.x.item(), state_data.y.item())
        s.write(answer_state)

# screen.mainloop()
