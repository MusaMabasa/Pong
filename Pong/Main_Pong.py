from turtle import Screen
from Paddle import Paddle
from Scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

r_player = Paddle((350,0))
l_player = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(fun=r_player.move_up, key="Up")
screen.onkey(fun=r_player.move_down, key="Down")
screen.onkey(fun=l_player.move_up, key="w")
screen.onkey(fun=l_player.move_down, key="s")


game_on = True
while game_on:

    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_player) < 50 and ball.xcor() < 340 or ball.distance(l_player) < 50 and ball.xcor() < 340:
        ball.bounce_x()
        #right player miss
    if ball.xcor() > 350:
        ball.reset_ball()
        ball.bounce_x()
        score.l_point()

        #left player miss
    if ball.xcor() < -350:
        ball.reset_ball()
        ball.bounce_x()
        score.r_point()


screen.exitonclick()