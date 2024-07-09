from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete("0", "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    web = wb_input.get().lower()
    email = email_input.get()
    password = password_input.get()

    # json
    new_data = {web: {
        "email": email,
        "password": password
    }}

    def save_old_data():
        global data
        with open("data.json", "r") as file:
            # Reading old data
            data = json.load(file)
            # updating old data with new data
            data.update(new_data)

    def dump_or_create_data(*args):
        with open("data.json", "w") as file:
            # Saving updated data
            json.dump(*args, file, indent=4)

    if len(web) < 3 or len(password) < 3 or len(email) < 3:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            save_old_data()
        except FileNotFoundError:
            dump_or_create_data(new_data)
        else:
            dump_or_create_data(data)
        finally:
            wb_input.delete("0", "end")
            password_input.delete("0", "end")


# ---------------------------- Password search ------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as file:
            loaded_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        web = wb_input.get().lower()
        # check if key is inside of list
        if web in loaded_data:
            for key in loaded_data:
                if key == web:
                    get_password = loaded_data[key]["password"]
                    get_email = loaded_data[key]["email"]
                    messagebox.showinfo(title=web.capitalize(), message=f" Website: {key}\n Email: {get_email}\n "
                                                                        f"Password: {get_password}")
        else:
            messagebox.showwarning(title="No founded", message="No details for the website")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager v2")
window.config(padx=20, pady=20)

# picture
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
wb_lb = Label(text="Website:")
wb_lb.grid(column=0, row=1)

email_lb = Label(text="Email/Username:")
email_lb.grid(column=0, row=2)

password_lb = Label(text="Password:")
password_lb.grid(column=0, row=3)

# inputs
wb_input = Entry(width=35)
wb_input.grid(column=1, row=1)
wb_input.focus()  # automatically focus into this input

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "tayr123@hotmail.com")  # entered automatically text on this input at position 0

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

# button
search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="EW")

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=36, command=add)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
