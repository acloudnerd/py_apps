import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((300, 0))
l_paddle = Paddle((-300, 0))
l_paddle.color("pink")

ball = Ball()

scoreboard = Scoreboard()
scoreboard.update_score()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with the wall above and below
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision between the ball and the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 260 or ball.distance(l_paddle) < 50 and ball.xcor() < -260:
        ball.bounce_x()

    if ball.xcor() > 300:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -300:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
