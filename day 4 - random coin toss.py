# random Coin toss Generator 

# first import random module
import random

#generate random number between 0 and 1
result = random.randint(0,1)

#heads is 0 and tails is 1
if result == 1:
  print("Heads")
else:
  print("Tails")
