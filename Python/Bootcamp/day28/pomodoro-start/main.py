from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_minute = math.floor(count/60)
    count_second = count % 60
    if count_minute < 10:
        count_minute = "0" + str(count_minute)
    if count_second < 10:
        count_second = "0" + str(count_second)

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        window.after(1000,count_down, count-1)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="./Python/Bootcamp/day28/pomodoro-start/tomato.png")
canvas.create_image(105,112, image=photo_image)
timer_text = canvas.create_text(105,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Labels
timer_layer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), justify="center", bg=YELLOW, fg=GREEN)
timer_layer.grid(column=1, row=0)

check_layer = Label(text="✔", font=(FONT_NAME, 12, "bold"), justify="center", bg=YELLOW, fg=GREEN, pady=20)
check_layer.grid(column=1, row=2)

#Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)












window.mainloop()