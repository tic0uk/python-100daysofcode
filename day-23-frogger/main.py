import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(key="Up", fun=turtle.up)


game_is_on = True
while game_is_on:


    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if car.distance(turtle) < 17:
            scoreboard.game_over()
            game_is_on = False

    if turtle.is_at_finish_line():
        turtle.reset_position()
        scoreboard.add_point()
        car_manager.speed_up()




screen.exitonclick()