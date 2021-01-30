from turtle import Turtle, Screen
from random import randint

background = 'racetrack.png'
my_window = Screen()
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
my_window.bgpic(background)
choice = my_window.textinput(title="Welcome to turtle races!", prompt="Which turtle will win the race? Enter a "
                                                                      "colour: ")

my_window.screensize(500, 400)
x_axis = -400
y_axis = -550
list_of_turtles = []
for turtle_index in range(len(colours)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.turtlesize(2)
    new_turtle.pu()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=x_axis, y=y_axis)
    new_turtle.speed("fastest")
    y_axis += 220
    list_of_turtles.append(new_turtle)

is_race_on = True
while is_race_on:

    for turtle in list_of_turtles:
        if turtle.xcor() > 300:
            is_race_on = False
            if choice == turtle.pencolor():
                print(f"The winning turtle is {turtle.pencolor()}. You win!")
                break
            else:
                print(f"The winning turtle is {turtle.pencolor()}. You lose!")
                break

        distance = randint(0, 10)
        turtle.forward(distance)

my_window.exitonclick()
