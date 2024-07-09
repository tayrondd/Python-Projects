from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
random_word_dict = {}

# ------------------------------------ word list ------------------------------------
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
    word_list = df.to_dict(orient="records")
else:
    word_list = df.to_dict(orient="records")

# ------------------------------------ random word ------------------------------------


def random_word():
    global random_word_dict
    window.after_cancel(window.after(3000, english_card))
    random_word_dict = random.choice(word_list)
    french_card()
    window.after(3000, english_card)  # flip card in 3 sec


def remove_word():
    print(random_word_dict)
    word_list.remove(random_word_dict)
    words_to_learn_list = pd.DataFrame(word_list)
    words_to_learn_list.to_csv("./data/words_to_learn.csv", index=False)
    random_word()


# ------------------------------------ interface ------------------------------------


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

# img
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_img = PhotoImage(file="./images/card_front.png")
flip_img = PhotoImage(file="./images/card_back.png")

# ------------------------------------ flip card ------------------------------------


def english_card():
    en_random_word = random_word_dict["English"]
    canvas.itemconfig(canvas_img, image=flip_img)
    window.after(3000, french_card)  # flip card in 3 sec
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=en_random_word, fill="white")


def french_card():
    fr_random_word = random_word_dict["French"]
    canvas.itemconfig(canvas_img, image=card_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=fr_random_word, fill="black")
# ------------------------------------ flip card ------------------------------------


canvas_img = canvas.create_image(400, 263, image=card_img)

# text
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# btn
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=random_word)
wrong_btn.grid(column=0, row=2)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=remove_word)
right_btn.grid(column=1, row=2)


random_word()
window.after(3000, english_card)  # flip card in 3 sec
window.mainloop()
