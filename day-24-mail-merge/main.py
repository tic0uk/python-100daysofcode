with open("./Input/Letters/starting_letter.txt") as letter:
    contents = letter.read()

with open("./Input/Names/invited_names.txt", "r") as names:
    list_of_names = names.readlines()
    for name in list_of_names:
        firstname = name.strip()
        mail_merge = contents.replace("[name]", firstname)
        with open(f"./Output/ReadyToSend/letter_for_{firstname}.txt", "w") as product:
            product.write(mail_merge)
