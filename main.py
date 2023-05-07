import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()

init = True
while init:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move, 'Up')
    if player.ycor() == player.finish_y:
        player.goto(player.start)
        score.increase_level()
        car.speed_increment()
    car.create_car()
    car.move()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            score.game_over()
            init = False

screen.exitonclick()
