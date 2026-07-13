import turtle as t
import random

tim = t.Turtle()
# Use the Python Turtle documentation to find more colors or set colormode
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


if __name__ == "__main__":
    tim = t.Turtle()
    directions = [0, 90, 180, 270]
    tim.pensize(10)
    tim.speed("fastest")

    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))

    t.done()
