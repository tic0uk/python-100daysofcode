# solution to code puzzle at
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def hurdle():
    turn_left()
    while right_is_clear() is not True:
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear() is True:
        move()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() is not True:
    if wall_in_front() is not True:
        move()   
    else: 
        hurdle()
