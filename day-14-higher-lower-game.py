def generate_choice():
    from random import choice
    choice = choice(data)
    return choice
def check_answer(choice_a, choice_b):
    if choice_a["follower_count"] > choice_b["follower_count"]:
        return "a" 
    elif choice_a["follower_count"] < choice_b["follower_count"]:
        return "b"
def game(choice_a, choice_b, score):
    # display text for A vs B
    clear()
    print(logo)
    # Don't display score first time around
    if score !=0:
        print(f"You're right! Current score: {score}.")
    print(f'Compare A: {choice_a["name"]}, a {choice_a["description"]}, from {choice_a["country"]}')
    print (vs) 
    print(f'Against B: {choice_b["name"]}, a {choice_b["description"]}, from {choice_b["country"]}')
    # Ask user for answer 
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    check = check_answer(choice_a, choice_b)
    if answer == check:
        score += 1
        # clear screen, copy B to A        
        choice_a = choice_b
        # generate new B
        choice_b = generate_choice()       
        game(choice_a, choice_b, score)
    else:  
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
# print the game art
from art import logo
from art import vs
# import the game_data
from game_data import data
# import the repl clear module
from replit import clear
# set the opening score to 0
score = 0
# generate random A
choice_a = generate_choice()
# generate random B
choice_b = generate_choice()
# begin game
game(choice_a, choice_b, score)
