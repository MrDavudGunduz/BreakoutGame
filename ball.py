import turtle
import sound

# Ball setup
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)
ball.dx = 0.4
ball.dy = 0.4

def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

def check_wall_collision():
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        sound.play_bounce_sound()

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        sound.play_bounce_sound()

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        sound.play_bounce_sound()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        sound.play_bounce_sound()

def check_paddle_collision(paddle):
    if (ball.ycor() > paddle.ycor() - 10) and (ball.ycor() < paddle.ycor() + 10) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1
        sound.play_bounce_sound()

def check_brick_collision(bricks):
    for brick in bricks:
        if ball.distance(brick["turtle"]) < 35:  # Adjust the collision threshold as needed
            brick["turtle"].clear()  # Remove the drawing associated with the brick
            brick["turtle"].hideturtle()  # Hide the turtle object after the collision
            bricks.remove(brick)  # Remove the brick from the list
            ball.dy *= -1  # Change ball direction
            sound.play_hit_sound()  # Play sound effect
            return True
    return False

def reset_ball():
    ball.goto(0, -230)
    ball.dy *= -1
