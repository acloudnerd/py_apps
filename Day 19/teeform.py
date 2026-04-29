from turtle import Turtle, Screen
import random

MOVE_STEP = 10
TURN_STEP = 10
COLORS = ["white", "red", "orange", "yellow", "green", "cyan", "violet"]

tee = Turtle()
tee.speed(0)
tee.pencolor(random.choice(COLORS))
tee.pensize(1)

screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Draw")


color_index = 0
pen_size = 1

def move_forward():
    tee.forward(MOVE_STEP)

def move_backward():
    tee.backward(MOVE_STEP)

def turn_left():
    tee.left(TURN_STEP)

def turn_right():
    tee.right(TURN_STEP)

def toggle_pen():
    if tee.isdown():
        tee.penup()
    else:
        tee.pendown()

def increase_size():
    global pen_size
    pen_size = min(pen_size + 1, 20)
    tee.pensize(pen_size)

def decrease_size():
    global pen_size
    pen_size = max(pen_size - 1, 1)
    tee.pensize(pen_size)

def change_color():
    global color_index
    color_index = (color_index + 1) % len(COLORS)
    tee.pencolor(random.choice(COLORS))

def clear():
    global pen_size, color_index
    tee.clear()
    tee.penup()
    tee.home()
    tee.pendown()
    pen_size = 1
    color_index = 0
    tee.pensize(pen_size)
    tee.pencolor(random.choice(COLORS))

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="p", fun=toggle_pen)
screen.onkey(key="Up", fun=increase_size)
screen.onkey(key="Down", fun=decrease_size)
screen.onkey(key="space", fun=change_color)
screen.onkey(key="c", fun=clear)

screen.exitonclick()