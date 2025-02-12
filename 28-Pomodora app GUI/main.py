from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global reps
    global check_count
    reps = 0
    check_count = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # If it's the 8th reps
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        # If it's the 2nd/4th/6th reps
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        # If it's the 1st/3rd/5th/7th reps
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check_count

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        if reps % 2 == 0:
            check_count += 1
            checkmark_label.config(text="✔" * check_count)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# label 1
timer_label = Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)
# tomato pic
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# buttons
start_button = Button(text="Start", command=start_time)
start_button.grid(column=1, row=3)
# buttons 2
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)
# label 2
checkmark_label = Label(font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=2, row=4)
window.mainloop()
