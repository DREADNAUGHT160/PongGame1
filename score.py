from turtle import Turtle

SCORE_SIZE = 20


class Score(Turtle):
    def __init__(self, x_loc):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(x_loc, 270)
        self.write(f"score :{self.score}", False, "center", font=("Courier", SCORE_SIZE, "normal"))
        self.hideturtle()
        self.game_on = True

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"score :{self.score}", False, "center", font=("Courier", SCORE_SIZE, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=("Courier", 20, "normal"))
        self.game_on = False


