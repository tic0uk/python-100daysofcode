from turtle import Turtle
FONT = ("Courier", 16, "bold")
SCORE_X_AXIS = -200
SCORE_Y_AXIS = 250
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color('black')
        self.goto(SCORE_X_AXIS, SCORE_Y_AXIS)
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", font=FONT, align=ALIGNMENT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)