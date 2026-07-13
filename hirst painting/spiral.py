import turtle as t
import random
from random_color import random_color


tee = t.Turtle()
t.colormode(255)

tee.speed("fastest")
def size_of_graph(size):
    for _ in range(int(360/size)):
        tee.color(random_color())
        tee.circle(100)
        tee.setheading(tee.heading() + size)

size_of_graph(10)
screen = t.Screen()
screen.exitonclick()
