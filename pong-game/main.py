import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((300, 0))
l_paddle = Paddle((-300, 0))
l_paddle.color("pink")

ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

screen.exitonclick()
