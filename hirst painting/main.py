import turtle

t = turtle.Turtle()
t.speed(0)

def draw_shape(sides, color):
    t.penup()
    t.goto(0, 0)
    t.setheading(0)   # reset direction
    t.pendown()
    t.color(color)

    angle = 360 / sides
    for _ in range(sides):
        t.forward(100)
        t.right(angle)

draw_shape(4, "blue")    # square
draw_shape(3, "pink")    # triangle
draw_shape(5, "orange")  # pentagon
draw_shape(6, "red")     # hexagon

t.hideturtle()
turtle.done()