from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(entry.get())
    km_result.config(text=round(miles * 1.609344, 2))


entry = Entry(width=10)
entry.insert(END, string="") # insert text at the end of the entered characters
entry.grid(column=2, row=1)

text_font = ("Arial", 12)
miles_label = Label(text="Miles", font=text_font)
miles_label.grid(column=3, row=1)

equal_label = Label(text="is equal to", font=text_font)
equal_label.grid(column=1, row=2)

km_label = Label(text="Km", font=text_font)
km_label.grid(column=3, row=2)

km_result = Label(text="0", font=text_font)
km_result.grid(column=2, row=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)

window.mainloop()  # keep window open, it has to be at the end of all my script