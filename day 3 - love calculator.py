# based off a childs game to give a score of whether two names are a good romantic match
# sirst ascertain names 
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# concat the names and convert to lowercase
combined_name = name1 + name2
lower_combined_name = combined_name.lower()

# take both people's names and check for the number of times the letters in the word TRUE occurs.
# then check for the number of times the letters in the word LOVE occurs

score = 0 
t = lower_combined_name.count("t")
r = lower_combined_name.count("r")
u = lower_combined_name.count("u")
e = lower_combined_name.count("e")
true = t + r + u + e
l = lower_combined_name.count("l")
o = lower_combined_name.count("o")
v = lower_combined_name.count("v")
e = lower_combined_name.count("e")
love = l + o + v + e

# concat the two results to make a 2 digit number. 
truelove = int(str(true) + str(love))

# print the results
if truelove < 10 or truelove > 90: 
  print(f"Your score is {truelove}, you go together like coke and mentos.")
elif truelove >= 40 and score <= 50:
  print(f"Your score is {truelove}, you are alright together.")
else: 
  print(f"Your score is {truelove}")
