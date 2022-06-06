from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
START_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.snake_body()
        self.head = self.segments[0]

    def snake_body(self):
        for position in range(3):
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(STARTING_POSITION[-1])
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.snake_body()

    def extend(self):
        self.add_segment(-1)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            x_axis = self.segments[seg - 1].xcor()      # [seg - 1].xcor() will give X corrdinate of head
            y_axis = self.segments[seg - 1].ycor()      # [seg - 1].ycor() will give Y coordinate of head
            self.segments[seg].goto(x_axis, y_axis)     # Assigning Block apart from head to the position of head
        self.segments[0].forward(START_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
