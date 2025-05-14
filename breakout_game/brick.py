import turtle
import random

# Brick setup

def random_shape():
    return random.choice(["square", "turtle", "circle", "triangle", "classic"])

def get_color_by_hp(hp):
    if hp == 5:
        return "red"
    elif hp == 4:
        return "purple"
    elif hp == 3:
        return "orange"
    elif hp == 2:
        return "blue"
    elif hp == 1:
        return "green"
    else:
        return "gray"

# Rastgele boyut seçimi
def random_size():
    stretch_wid = random.uniform(1.0, 2.0)
    stretch_len = random.uniform(2.0, 4.0)
    return stretch_wid, stretch_len

def create_bricks(level):
    global bricks
    bricks = []

    brick_rows = 5
    brick_cols = 10
    brick_gap = 10
    brick_width = 70
    brick_height = 30

    base_hp = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5
    }
    shape = random_shape()
    stretch_wid, stretch_len = random_size()
    for row in range(brick_rows):
        
        for col in range(brick_cols):
            draw_brick = False

            # Seviye desenleri
            if level == 1:
                draw_brick = True
            elif level == 2:
                if row % 2 == 0:
                    draw_brick = True
            elif level == 3:
                if (row + col) % 2 == 0:
                    draw_brick = True
            elif level == 4:
                if col == 0 or col == brick_cols - 1:
                    draw_brick = True
            elif level == 5:
                center = brick_cols // 2
                if col >= center - row and col <= center + row:
                    draw_brick = True

            if draw_brick:
                brick = turtle.Turtle()
                
                
                brick.shape(shape)
                brick.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)

                # Tuğla alanına göre HP hesapla (örnek: 1 alan = 1 HP, max 10)
                area = stretch_wid * stretch_len
                hp = min(int(base_hp[level] * area), 10)

                brick.color(get_color_by_hp(hp))
                brick.penup()

                x = -350 + (col * (brick_width + brick_gap))
                y = 200 - (row * (brick_height + brick_gap)) + 20
                brick.goto(x, y)

                bricks.append({
                    "turtle": brick,
                    "hp": hp,
                    "dx": random.choice([-1, 1]) * 2 if level == 5 else 0
                })
    return bricks