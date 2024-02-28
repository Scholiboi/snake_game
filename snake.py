from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.seg = []
        self.createsnake()
        self.head = self.seg[0]
        self.head.color("green")
        self.head.shapesize(stretch_wid=1.5, stretch_len=1.5)
        
    def createsnake(self):
        x_coords = 0
        for n in range(3):
            t = Turtle(shape="square")
            t.speed("fastest")
            t.color("white")
            t.penup()
            t.teleport(x=x_coords, y=0)
            x_coords -= 20
            self.seg.append(t)

    def restartgame(self):
        for seg in self.seg:
            seg.goto(2000,2000)
        self.seg.clear()
        self.createsnake()
        self.head = self.seg[0]
        self.head.color("green")
        self.head.shapesize(stretch_wid=1.5, stretch_len=1.5)

    def extendseg(self):
        t = Turtle(shape="square")
        t.speed("fastest")
        t.color("white")
        t.penup()
        t.goto(self.seg[-1].pos())
        self.seg.append(t)

    def move(self):
        for n in range(len(self.seg) - 1, 0, -1):
            self.seg[n].goto(self.seg[n - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)
            