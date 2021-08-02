import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.color("coral")
timmy.pencolor("magenta")

# #making a square
# for _ in range(0, 4):
#
#     timmy.forward(100)
#     timmy.right(90)

# #Drawing a dashed line
# for _ in range(0,50):
#     timmy.forward(3)
#     timmy.penup()
#     timmy.forward(3)
#     timmy.pendown()

# Drawing triangle, square, pentagon, hexagon, heptagon, octagon, nanogon, decagon
colours = ["cyan", "purple", "red", "blue", "green", "pink", "coral", "grey"]

# for sides in range(3, 11):
#     timmy.pencolor(random.choice(colours))
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(360/sides)

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b) #tuple

# random walk

# for _ in range(200):
#     angles = [0,90,180,270]
#     random_angle = random.choice(angles)
#     timmy.pensize(10)
#     timmy.forward(30)
#     timmy.seth(random_angle)
#     timmy.speed(30)
#     # timmy.color(random.choice(colours))
#     timmy.color(random_color())

#  # DRAW A SPIROGRAPH

timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        timmy.color(random_color())

        timmy.circle(100)
        timmy.left(size_of_gap)
        timmy.hideturtle()

draw_spirograph(10)
screen = Screen()
screen.exitonclick()
