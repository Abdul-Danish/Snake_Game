from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # self.food = self.shape("circle")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_axis = random.randint(-360, 360)
        y_axis = random.randint(-260, 260)
        self.goto(x_axis, y_axis)
