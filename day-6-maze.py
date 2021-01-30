# solution to code puzzle at
# Write a program using an if/elif/else statement so Reeborg can find the
# exit. The secret is to have Reeborg follow along the right edge of the 
# maze, turning right if it can, going straight ahead if it can’t turn 
# right, or turning left as a last resort.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not wall_in_front():
        move()
    else:
        turn_left()
        
# Same as above but includes debugging to prevent edge-case infinite loop.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

count = 0 
while not at_goal():
    if right_is_clear() and count < 5:
            turn_right()
            move()
            count += 1
    elif not wall_in_front():
        move()
        count=0
    else:
        turn_left()
