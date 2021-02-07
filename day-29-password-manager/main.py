from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(10)]
    password_list += [choice(symbols) for char in range(4)]
    password_list += [choice(numbers) for char in range(4)]

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.insert(0, "timcraig1982@gmail.com")


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="oops", message="Please complete all fields before clicking 'add'")
    else:
        is_ok = messagebox.askokcancel(title=website_entry, message=f"These are the details entered:"
                                                                    f" \nEmail: {email}\n Password: {password} \n"
                                                                    f"Is it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                clear()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=250, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(170, 80, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "timcraig1982@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

window.mainloop()
