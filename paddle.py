import turtle

# Paddle setup
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

def move_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 20)

def move_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 20)
