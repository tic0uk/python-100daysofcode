from tkinter import *
import pandas
import random

current_card = {}
BACKGROUND_COLOR = "#B1DDC6"

# Import French/English csv file

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    french_english_dict = data.to_dict(orient="records")


def remove_flashcard():
    global current_card
    french_english_dict.remove(current_card)
    list_remaining = pandas.DataFrame(french_english_dict)
    list_remaining.to_csv("./data/words_to_learn.csv", index=False)
    choose_card()


def choose_card():
    global timer
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_english_dict)
    french_card_text = current_card["French"]
    canvas.itemconfig(card_image, image=front_card_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_card_text, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=back_card_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# USER INTERFACE

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
canvas = Canvas(width=800, height=526)
back_card_img = PhotoImage(file="./images/card_back.png")
front_card_img = PhotoImage(file="./images/card_front.png")
card_image = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 150, font=("Ariel", 20, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

correct_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_flashcard)
correct_button.grid(column=1, row=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=choose_card)
wrong_button.grid(column=0, row=2)
choose_card()


window.mainloop()