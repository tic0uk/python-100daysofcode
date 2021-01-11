# random generator to work out who will pay the bill

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#import the random module
import random

# count the number of items in the list
num_list_items = len(names)

# generate a random number between 0 and count of items (take off one for 0 offset)
random_number = random.randint(0,num_list_items - 1)

# choose the name
random_name = names[random_number] 

# deliver the result
print(f"{random_name} is going to buy the meal today!")
