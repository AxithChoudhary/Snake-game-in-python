from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.HEAD = self.segments[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_seg(pos)

    def add_seg(self, position):
        snake_seg = Turtle(shape="square")
        snake_seg.color("white")
        snake_seg.penup()
        snake_seg.goto(position)
        self.segments.append(snake_seg)

    def extend_snake(self):
        self.add_seg(self.segments[-1].position())

    def restart(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.HEAD = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=new_x, y=new_y)

        self.HEAD.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.HEAD.heading() != DOWN:
            self.HEAD.setheading(UP)

    def move_down(self):
        if self.HEAD.heading() != UP:
            self.HEAD.setheading(DOWN)

    def move_right(self):
        if self.HEAD.heading() != LEFT:
            self.HEAD.setheading(RIGHT)

    def move_left(self):
        if self.HEAD.heading() != RIGHT:
            self.HEAD.setheading(LEFT)


