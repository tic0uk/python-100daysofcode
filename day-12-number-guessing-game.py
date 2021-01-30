# A number guessing game. Slightly different to teachers version but works fine so I'll keep up 
# and learn lessons for future

import random 
from art import logo #separate file not included


def start_game():
    print(logo) #separate file not included
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5

def guess():
    if lives == 0:
        print("You've run out of guesses, you lose.")
        return True
    print(f"You have {lives} attempts remaining to guess the number.")
    print("Guess again.")
    guess = int(input("Make a guess: "))
    if guess == answer:
        print("You've won the game!")
        return True
    elif guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low")
        return False

lives = start_game()
answer = random.randint(1,100)

end_game = False
while not end_game:
    end_game = guess()
    if not end_game:
        lives -= 1
