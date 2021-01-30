# replicating a game called fizzbuzz that children play;

for i in range(1,101):

# if number is divisible by both 3 or 5 say "fizzbuzz"
  if (i % 3 == 0 and i % 5 == 0):
    print ("fizzbuzz")

# if number is divisible by 3 say "fizz"
  elif i % 3 == 0:
    print ("fizz")

# if number is divisible by 5 say "buzz"
  elif i % 5 == 0:
    print ("buzz")

# otherwise display the number as usual
  else: 
    print (i)  
