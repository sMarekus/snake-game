from turtle import Turtle

FONT_STYLE = ('Comic Sans MS', 18, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.goto(x=0, y=260)
        self.update_score()
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    # If you want to end the game
    #
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", font=FONT_STYLE, align="center")

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", font=FONT_STYLE, align="center")