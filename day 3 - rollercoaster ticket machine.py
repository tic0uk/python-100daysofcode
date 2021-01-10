# introduction and ascertain height
print("Welcome to the rollercoaster")
height = int(input("Please enter your height in cm "))
bill = 0

# if the user isn't 120cm tall then print else statement
# otherwise ascertain age and add to bill

if height >= 120:
  print("You are allowed to ride the rollercoaster")
  age = int(input("Please enter your age... "))
  if age < 12:
    print("Child tickets are £5")
    bill += 5
  elif age < 18:
    print("Youth tickets are £7")
    bill += 7
  elif age >= 45 and age <= 55:
    print("Have a free ride on us!")
    bill += 0
  else:
    print("Adult tickets are £12")
    bill += 12
    
# do they want a photo? If so add to bill
  wants_photo = input("Do you want a photo taken? Y or N. ")
  # this is ran as there is no else to it
  if wants_photo == "Y":
    #Add £3 to their bill
    bill += 3

# give the final bill
  print(f"Your bill is £{bill:.2f}")

else:
 print("You are not allow to ride the rollercoaster")
