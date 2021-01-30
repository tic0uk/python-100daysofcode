# obtain user height and wight.
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# convert input into float
float_height = float(height)
float_weight = float(weight)

# caculate the BMI (bmi = weight/height2).
result = int(float_weight/float_height ** 2)

# Display the result on the screen.
print (result)
