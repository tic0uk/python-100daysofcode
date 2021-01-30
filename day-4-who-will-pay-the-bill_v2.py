# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#import the random module
import random

# choose a random name from the list
random_name = random.choice(names)

# deliver the result
print(f"{random_name} is going to buy the meal today!")
