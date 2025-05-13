import turtle

# Brick setup
bricks = []

def create_bricks():
    brick_rows = 5
    brick_cols = 10
    brick_width = 70
    brick_height = 30
    brick_gap = 10

    for row in range(brick_rows):
        for col in range(brick_cols):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color("green")
            brick.penup()
            brick.goto(-300 + (col * (brick_width + brick_gap)), 250 - (row * (brick_height + brick_gap)))
            bricks.append(brick)
    return bricks
