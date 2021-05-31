from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1
