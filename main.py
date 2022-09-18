import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
#Screen listens for player movemement
screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
game_loop = 0
cars = []
scoreboard.display_level()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if game_loop % scoreboard.frequency == 0:
        cars.append(CarManager(level=scoreboard.level))
        print(game_loop)
    for car in cars:
        if car.xcor() > -310:
            car.drive()
        else:
            cars.remove(car)
            car.hideturtle()
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.detect_finish():
        scoreboard.increment_level()
        scoreboard.increase_frequency()
        player.restart()
    game_loop += 1


screen.exitonclick()