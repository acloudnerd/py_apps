import turtle as turtle_module
import random

turtle_module.colormode(255)
tee = turtle_module.Turtle()
tee.speed(0)
tee.hideturtle()
color_list = [(238, 242, 246), (196, 165, 119), (143, 81, 58), (220, 200, 142), (60, 94, 119), (163, 152, 54),
              (137, 161, 177), (129, 35, 24), (71, 37, 30), (52, 116, 86), (189, 95, 81), (145, 176, 150),
              (100, 75, 78), (165, 146, 158), (22, 90, 70), (226, 177, 168), (33, 58, 72), (134, 25, 30), (65, 44, 46),
              (180, 203, 179), (87, 145, 129), (25, 83, 86), (18, 66, 54), (40, 65, 90), (109, 128, 148),
              (169, 102, 105), (220, 177, 181)]
tee.penup()
tee.setheading(225)
tee.forward(300)
tee.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots + 1):

    tee.dot(20, random.choice(color_list))
    tee.forward(50)

    if dot_count % 10 == 0:
        tee.setheading(90)
        tee.forward(50)
        tee.setheading(180)
        tee.forward(500)
        tee.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
