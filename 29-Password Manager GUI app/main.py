from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    web = wb_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(web) < 3 or len(password) < 3 or len(email) < 3:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"The are the details entered:\nEmail: {email}\n"
                                                          f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write("{\n")
                file.write(f"website: '{web}',\nusername: '{email}',\npassword: '{password}',\n")
                file.write("},\n")
                wb_input.delete("0", "end")
                password_input.delete("0", "end")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
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
wb_input.grid(column=1, row=1, columnspan=2, sticky="EW")
wb_input.focus()  # automatically focus into this input

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "tayr23423@hotmail.com")  # entered automatically text on this input at position 0

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

# button
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=36, command=add)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
