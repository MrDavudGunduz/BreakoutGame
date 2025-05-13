import turtle
import paddle
import ball
import brick
import sound


# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle movement bindings
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

# Create the bricks
bricks = brick.create_bricks()

# Game loop
score = 0
while True:
    screen.update()

    # Move the ball
    ball.move_ball()

    # Check for wall collisions
    ball.check_wall_collision()

    # Check for paddle collision
    ball.check_paddle_collision(paddle.paddle)

    # Check for brick collision
    if ball.check_brick_collision(bricks):
        score += 1

    # Check if all bricks are destroyed
    if len(bricks) == 0:
        ball.reset_ball()
        sound.play_game_over_sound()
        print(f"Game Over! You scored {score} points.")
        break

# Keep the window open until clicked
screen.exitonclick()
