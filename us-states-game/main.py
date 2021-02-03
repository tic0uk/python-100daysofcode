import turtle
import pandas


screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

total_states = len(states)
score = 0

correct_answers = []
is_game_on = True

while is_game_on:

    answer_state = screen.textinput(title="Make a guess", prompt=f"{score}/{total_states} States Correct. "
                                                                 "Guess a state!").title()
    if answer_state == "Exit":
        break
    for state in states:
        if answer_state == state and answer_state not in correct_answers:
            correct_answers.append(state)
            score += 1
            answer_row = data[data.state == f"{answer_state}"]
            answer_x = int(answer_row.x)
            answer_y = int(answer_row.y)
            state_text = turtle.Turtle()
            state_text.hideturtle()
            state_text.pu()
            state_text.goto(x=answer_x, y=answer_y)
            state_text.write(f"{state}")
            state_text.color("black")

missing_states = []
for state in states:
    if state not in correct_answers:
        missing_states.append(state)
df = pandas.DataFrame(missing_states, columns=['States_to_learn'])

df.to_csv("states_to_learn.csv")
