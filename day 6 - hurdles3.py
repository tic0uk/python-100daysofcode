# solution to code puzzle at
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() is not True:
    if wall_in_front() is not True:
        print("front clear")
        move()   
    else: 
        print("front not clear")   
        hurdle()
