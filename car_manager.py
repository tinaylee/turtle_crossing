from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x= 280, y=random.randint(-250, 250))
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.move_distance = (level-1) * MOVE_INCREMENT + STARTING_MOVE_DISTANCE


    def drive(self):
        self.forward(self.move_distance)



