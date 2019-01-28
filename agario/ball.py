from turtle import *

class Ball(Turtle):
    def __init__(self, x, y, dx, dy, r, color):
        Turtle.__init__(self)
        self.penup()
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shape('circle')
        self.shapesize(self.r/10)
        self.color(color)

    def move(self, screen_width, screen_height):
        current_x = self.xcor()
        new_x = current_x + self.dx
        current_y = self.ycor()
        new_y = current_y + self.dy
        right_ball_side = new_x + self.r
        left_ball_side = new_x - self.r
        up_ball_side = new_y + self.r
        down_ball_side = new_y - self.r
        self.goto(new_x, new_y)
        if right_ball_side >= screen_width:
            self.dx = -self.dx
        if left_ball_side <= -screen_width:
            self.dx = -self.dx
        if up_ball_side >= screen_height:
            self.dy = -self.dy
        if down_ball_side <= -screen_height:
            self.dy = -self.dy

    def new_ball(self, x, y, dx, dy, r, color):
        self.penup()
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shape('circle')
        self.shapesize(self.r/10)
        self.color(color)
