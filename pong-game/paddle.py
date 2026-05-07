from turtle import Turtle

STARTING_POSITION = (300, 0)
SPEED = 25
UP_DIRECTION = 1
DOWN_DIRECTION = -1


class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.y_position = starting_position[1]
        self.goto(starting_position)

    def move_up(self):
        self.y_position += SPEED * UP_DIRECTION
        self.goto(self.xcor(), self.y_position)

    def move_down(self):
        self.y_position += SPEED * DOWN_DIRECTION
        self.goto(self.xcor(), self.y_position)
