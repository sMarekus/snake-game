from turtle import Turtle

FONT_STYLE = ('Comic Sans MS', 18, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(x=0, y=260)
        self.write(f"Home = {self.score}", font=FONT_STYLE, align="center")
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT_STYLE, align="center")

    def update_score(self):
        self.clear()
        self.write(f"Home = {self.score}", font=FONT_STYLE, align="center")