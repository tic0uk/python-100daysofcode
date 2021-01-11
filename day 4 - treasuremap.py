# Place an X on the treasure map

# first create the map as a list
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

# output to screen
print(f"{row1}\n{row2}\n{row3}")

# get two coordinates as a single number (e.g. 23)
position = input("Where do you want to put the treasure? ")

# split out horizontal row number
horizontal = int(position[0])

# split out vertical row number

vertical = int(position[1])

# place an X on the map using above coordinates
map[horizontal -1][vertical -1] = "X"

# show the updated map
print(f"{row1}\n{row2}\n{row3}")
