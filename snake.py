from turtle import Turtle
startingpositions=[(0,0),(-20,0),(-40,0)]
movedistance=20
up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]
    def createsnake(self):
        for position in startingpositions:
            self.addsegment(position)
    def addsegment(self,position):
        newsegment = Turtle("square")
        newsegment.color("white")
        newsegment.penup()
        newsegment.goto(position)
        self.segments.append(newsegment)

    def extend(self):
        self.addsegment(self.segments[-1].position())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[segnum - 1].xcor()
            newy = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(newx, newy)
        self.head.forward(movedistance)
    def up(self):
        if self.head.heading() !=down:
           self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
           self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
           self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
           self.head.setheading(right)
