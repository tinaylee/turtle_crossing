from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270, 260)
        self.frequency = 6

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increment_level(self):
        self.level += 1
        self.display_level()

    def game_over(self):
        self.penup()
        self.home()
        self.write("Game Over", align="center", font=FONT)

    def increase_frequency(self):
        if self.frequency > 0:
            self.frequency -= 1