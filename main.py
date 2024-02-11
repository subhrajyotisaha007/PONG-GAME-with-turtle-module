import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600,width=800)
screen.title('PONG')
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up,'w')
screen.onkey(left_paddle.down,'s')

game_on =True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.refresh()
        score.lscore()
    if ball.xcor() <-380:
        ball.refresh()
        score.rscore()

screen.exitonclick()