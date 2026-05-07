from turtle import Turtle
import random

ORIGIN = (0,0)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(ORIGIN)
        self.color("yellow")
        self.penup()
        self.move()

    def move(self):
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        # self.goto(random_x, random_y)
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

