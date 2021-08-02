# import colorgram
# Extracting the colors fom picture

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

# extracted colors

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

extracted_color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

#requirments

# 10 x 10 dots
# 20 in size
# 50 aparts

# tim.setheading(225)
# tim.forward(350)
# tim.setheading(0)
# print(tim.ycor())
# print(tim.xcor())
tim.penup()
tim.speed("fastest")
tim.hideturtle()

y_cordinate = - 200
for _ in range(10):
    tim.goto(-200, y_cordinate )
    y_cordinate +=50

    for _ in range(10):
        random_color = random.choice(extracted_color_list)
        tim.dot(20, random_color)
        tim.penup()
        tim.forward(50)

screen = t.Screen()
screen.exitonclick()