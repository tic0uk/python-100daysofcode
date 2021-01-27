# The following uses the turtle module to draw a Damien Hirst style painting
# (e.g. http://www.damienhirst.com/artworks/catalogue?category=1)
from turtle import Turtle, Screen
from random import choice
color_list = [(131, 164, 204), (228, 149, 99), (30, 44, 64), (166, 58, 48), (202, 135, 147), (237, 212, 85),
              (41, 101, 150), (135, 183, 161), (150, 62, 71), (52, 42, 45), (159, 33, 31), (219, 82, 73),
              (238, 165, 155), (58, 117, 99), (60, 49, 45), (173, 29, 31), (231, 163, 168), (35, 61, 56),
              (15, 96, 71), (33, 60, 107), (170, 188, 222), (188, 101, 111), (104, 126, 161), (14, 85, 109),
              (174, 200, 188), (33, 151, 211)]


my_screen = Screen()
my_screen.colormode(255)

timmy = Turtle()

timmy.color("green")
timmy.pu()
timmy.setpos(-450, -500)
timmy.speed("fastest")
timmy.hideturtle()


for _ in range(10):
    for _ in range(10):
        timmy.dot(50, choice(color_list))
        timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)
    timmy.setx(-450)
    timmy.right(90)

my_screen.exitonclick()
