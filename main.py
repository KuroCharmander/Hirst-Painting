# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

import turtle
import random

# Colors extracted from a Hirst dot painting using the package colorgram
color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40),
              (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159),
              (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102),
              (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39),
              (164, 209, 187), (151, 206, 220)]


def random_color():
    """Return a random tuple of RGB colors from color_list."""
    return random.choice(color_list)


def draw_row():
    """Draw the 10 dots in the row."""
    for _ in range(10):
        t.dot(20, random_color())
        t.forward(50)


def draw_painting(x, y):
    """Draw 10 rows of dots starting from the bottom row up at position (x, y)."""
    t.setposition(x, y)
    for _ in range(10):
        draw_row()
        t.setposition(x, t.ycor() + 50)


t = turtle.Turtle()
turtle.colormode(255)
t.hideturtle()
t.speed(0)
t.penup()
draw_painting(-225, -225)


screen = turtle.Screen()
screen.exitonclick()
