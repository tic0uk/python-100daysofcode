# rock paper scissors game

# set ascii art for each choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# import random module
import random

game_images = [rock, paper, scissors]
# obtain user selection between 0 and 3
selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if selection >= 3 or selection <0:
  print ("You typed an invalid number, you lose")
else:
  # randomly selected choice between 0 and 3
  computer_selection = random.randint(0,2)

  # show the corresponding image to the number they chose
  print ("\n You chose:")
  print(game_images[selection])

  print ("\n The computer chose:")
  print(game_images[computer_selection])

  # same item is draw
  # rock 0 beats scissors 2 
  # paper 1 beats rock 0
  # scissors 2 beats paper 1
  # anything else loses

  if selection == computer_selection:
    print ("It's a draw!")
  elif (selection == 0) and (computer_selection == 2):
    print ("You win")
  elif (selection == 1) and (computer_selection == 0):  
    print ("You win")
  elif (selection == 2) and (computer_selection == 1):  
    print ("You win")
  else:
    print("You lose")
