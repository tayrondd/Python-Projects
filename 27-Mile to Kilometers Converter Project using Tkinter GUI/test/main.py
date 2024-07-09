import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


# label
my_label = tkinter.Label(text="I'm label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop() # keep window open, it has to be at the end of all my script