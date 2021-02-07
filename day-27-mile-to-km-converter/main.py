# Miles to Km Converter
from tkinter import *


def button_clicked():
    miles = float(num_miles.get())
    result = miles * 1.609
    num_km.config(text=f"{result}")


window = Tk()
window.config(padx=20, pady=20)
window.title("Mile to Km Converter")

text_is_equal_to = Label(text="is equal to")
text_is_equal_to.grid(column=0, row=1)
text_is_equal_to.config(padx=10, pady=10)

text_miles = Label(text="Miles")
text_miles.grid(column=2, row=0)
text_miles.config(padx=10, pady=10)

num_km = Label(text="0")
num_km.grid(column=1, row=1)
num_km.config(padx=10, pady=10)

text_km = Label(text="Km")
text_km.grid(column=2, row=1)
text_km.config(padx=10, pady=10)

num_miles = Entry(width=10)
num_miles.grid(column=1, row=0)

calculate_button = Button(text="calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=10, pady=10)

window.mainloop()
