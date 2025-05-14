import turtle
import paddle
import ball
import brick
import sound

level = 1
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
bricks = brick.create_bricks(level)

# Game loop
score = 0
high_score = 0


# Score display setup
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-350, 260)

def update_score_display():
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {high_score}", font=("Arial", 16, "normal"))

# Initial score display
update_score_display()


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
        if score > high_score:
            high_score = score
        update_score_display()

    # Check if all bricks are destroyed
    if len(bricks) == 0:
        ball.reset_ball()
        if level <= 5:
            level += 1
        bricks = brick.create_bricks(level)
        print(f"Level {level}!")
        
    # Pause the game if no bricks left
    if len(bricks) == 0 and level > 5:
        print(f"Game Over! You scored {score} points.")
        break

# Keep the window open until clicked
screen.exitonclick()
