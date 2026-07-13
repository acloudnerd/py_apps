from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=550, height=450)
screen.bgcolor("black")

RACE_COLORS = ["yellow", "green", "cyan", "violet"]
print(" | ".join(RACE_COLORS))
user_bet = screen.textinput(title="Place your bet",
                            prompt=f"Pick a color from: {' | '.join(RACE_COLORS)}\n\nYour choice: ").lower()

if user_bet in RACE_COLORS:
    print("Valid choice")
else:
    print("That color is not in the race!")

all_turtles = []

for color in RACE_COLORS:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    all_turtles.append(new_turtle)

# for i in all_turtles:
#     print(i.pencolor())
height = 450
y_spacing = height / 4

for index, turtle in enumerate(all_turtles):
    # print(index, turtle)
    turtle.penup()
    turtle.goto(-230, (index * y_spacing) - (height / 2) + (y_spacing / 2))
    turtle.pendown()

race_on = True

while race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1, 10))

        if turtle.xcor() >= 230:
            race_on = False
            winner_color = turtle.pencolor()
            break

if user_bet == winner_color:
    print("You won the bet!")
else:
    print(f"You lost! The winner was {winner_color}")

screen.exitonclick()
