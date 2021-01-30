from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # reverse stretching so it gets smaller by half/half
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-450, 450)
        random_y = random.randint(-450, 450)
        self.goto(x=random_x, y=random_y)
