from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270.0:
            self.segments[0].setheading(90.0)

    def down(self):
        if self.segments[0].heading() != 90.0:
            self.segments[0].setheading(270.0)

    def left(self):
        if self.segments[0].heading() != 0.0:
            self.segments[0].setheading(180.0)

    def right(self):
        if self.segments[0].heading() != 180.0:
            self.segments[0].setheading(0.0)

    def ret_pos(self):
        return self.segments[0]

    def get_fat(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_x = self.segments[len(self.segments) - 1].xcor()
        new_y = self.segments[len(self.segments) - 1].ycor()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)