#Password Generator Project

#import random module

import random

#define password characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# welcome and find out many characters for letters/symbols/numbers
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Version 1
# non randomised

# create a new list and add randomly chosen characters from each list above
password = []
password.extend(random.choices(letters, k=nr_letters))
password.extend(random.choices(numbers, k=nr_symbols))
password.extend(random.choices(symbols, k=nr_numbers))

# turn the list into a string and print on the screen
new_password = ""
for i in password:
  new_password += i
print (f"Here is your password: {new_password}")

# Follows on from above code but randomises the order of final password string:
new_password = ""
random.shuffle(password)
for i in password:
  new_password += i
print (f"Here is your shuffled password: {new_password}")


# Version #2
# non randomised
random_character = ""
# use a range on your for loop to set amount of interations
for char in range(1, nr_numbers +1):
  random_character += random.choice(numbers)
for char in range(1, nr_letters +1):
  random_character += random.choice(letters)
for char in range(1, nr_symbols +1):
  random_character += random.choice(symbols)
print(f"Here is your password: {random_character}")


# randomised version
password_list = []
for char in range(1, nr_numbers +1):
  password_list.append(random.choice(numbers))
for char in range(1, nr_letters +1):
  password_list.append(random.choice(letters))
for char in range(1, nr_symbols +1):
  password_list.append(random.choice(symbols))
new_password = ""
random.shuffle(password_list)
for i in password_list:
  new_password += i
print (f"Here is your shuffled password: {new_password}")
