from tkinter import *
from random import choice, randint, shuffle
import pyperclip
import json
from password import *




def generate_and_insert_password():

    password_entry.delete(0,END)
    password = Password()
    params = password.decide_params()
    generated_password = password.generate_password(params)
    password_entry.insert(0,generated_password)
    return







# GUI------------------------------------------------

LIGHT_BLUE = "#C2DEDC"
CREME = "#ECE5C7"
LIGHT_GREY = "#CDC2AE"
KIND_OF_BLUE = "#116A7B"


window = Tk()
window.minsize(width=200, height=200)
window.title("Password Manager")
window.config(padx=55, pady=50, )

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_pic = PhotoImage(file="new.png")
canvas.create_image(100, 100, image=logo_pic, )
canvas.grid(column=1, row=0)

# ----------------------------Labels------------------------------------- #
website_label = Label(text="Website: ", )
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username: ", )
user_label.grid(column=0, row=2)

password_label = Label(text="Password: ", )
password_label.grid(column=0, row=3)

# ----------------------------Entries_____________________________________#

website_entry = Entry(width=33, )
website_entry.focus()  # focus the cursor into the widget when we log in
website_entry.grid(column=1, row=1, padx=2, pady=2)

email_entry = Entry(width=51)
email_entry.insert(0, "urisham@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, padx=2, pady=2)

password_entry = Entry(width=33)

password_entry.grid(column=1, row=3, pady=2)

# ___________________________Buttons_________________________________________#

button_choices = ["Generate Password", "Recall Password"]

generate_button = Button(text="Generate Password", borderwidth=1, highlightthickness=0, command=generate_and_insert_password)
generate_button.grid(column=2, row=3, padx=2, pady=2)

add_button = Button(text="Add", width=44, borderwidth=1, highlightthickness=0,)
add_button.grid(column=1, row=4, columnspan=2, pady=2)

search_button = Button(text="Search",width = 14, borderwidth=1, highlightthickness=0, )
search_button.grid(column=2, row=1 , pady=2)





window.mainloop()
