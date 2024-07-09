from tkinter import *

# http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = Label(text="label 1", font=("Arial", 12, "bold"))
label.grid(column=1, row=1)

button = Button(text="button 1")
button.grid(column=2, row=2)

button = Button(text="button 1")
button.grid(column=3, row=1)

input = Entry(width=50)
input.insert(END, string="Some text to begin with.")
input.grid(column=4, row=3)

window.mainloop()  # keep window open, it has to be at the end of all my script