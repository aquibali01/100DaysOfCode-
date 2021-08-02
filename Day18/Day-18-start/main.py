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

for sides in range(3, 11):
    timmy.pencolor(random.choice(colours))
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)

screen = Screen()
screen.exitonclick()
