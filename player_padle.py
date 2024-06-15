from turtle import Turtle

class padle(Turtle):
    def __init__(self,position,color):
        super().__init__()
        self.color(color)
        self.penup()
        self.shape(name="square")
        self.shapesize(5,1)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(),new_y)