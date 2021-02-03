# create a CSV from the attached squirrel data csv
# The new csv should give a total count of squirrels with a particular colour fur
# e.g. grey, cinnamon, black

# primary fur color

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur_colour = data["Primary Fur Color"]
counts = primary_fur_colour.value_counts()

counts.to_csv("count.csv")

# alternative method
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

squirrels = {
    "Fur Colour": ["Grey", "Red", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels],
}

squirrel_count = pandas.DataFrame(squirrels)

squirrel_count.to_csv("count2.csv")
