from turtle import Turtle

SCORE_X_AXIS = 0
SCORE_Y_AXIS = 200
FONT = ('Courier', 40, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.color('white')
        self.pu()
        self.score_left = 0
        self.score_right = 0
        self.goto(x=SCORE_X_AXIS, y=SCORE_Y_AXIS)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"{self.score_left} : {self.score_right}", font=FONT, align=ALIGNMENT)

    def add_point_right(self):
        self.clear()
        self.score_right += 1
        self.update_scoreboard()

    def add_point_left(self):
        self.clear()
        self.score_left += 1
        self.update_scoreboard()
