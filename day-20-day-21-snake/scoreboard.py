from turtle import Turtle

SCORE_X_AXIS = 0
SCORE_Y_AXIS = 440
FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.color('white')
        self.pu()
        self.goto(x=SCORE_X_AXIS, y=SCORE_Y_AXIS)
        self.hideturtle()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
