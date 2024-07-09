from tkinter import *

# http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I'm label", font=("Arial", 24, "bold"))
my_label.pack()


# entry box
input = Entry(width=10, )
input.pack()


# button
def button_clicked():
    my_label.config(text=input.get())


button = Button(text="I'm a button", command=button_clicked)
button.pack()

window.mainloop()  # keep window open, it has to be at the end of all my script
