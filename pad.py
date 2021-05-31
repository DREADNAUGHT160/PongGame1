from turtle import Turtle


class Paddle(Turtle, ):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("blue")
        self.up_start = True
        self.down_start = True

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
