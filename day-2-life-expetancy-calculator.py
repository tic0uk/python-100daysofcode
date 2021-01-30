# obtain user's age
age = input("What is your current age?")

# assuming user will live to be 90 years old
years = 90 - int(age)

# 365 days in a year (not including leap years)
# 52 weeks in a year
# 12 months in a year
days = int(years) * 365
weeks = int(years) * 52 
months = int(years) * 12

# print the life expectancy of the user if they were to live to 90 years old
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
