from tkinter import *
from random import choice
import pandas
import os
BASE_DIR = os.path.dirname(__file__)
#-------------- CONSTANTS --------------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
current_card = {}

#---------------------------------------------------#
data = pandas.read_csv(os.path.join(BASE_DIR, "data", "italian_words.csv"))
to_learn = data.to_dict(orient="records")

#--------------- FUNCTIONS -------------------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="Italian", fill="black")
    canvas.itemconfig(card_word, text=current_card["Italian"], fill="black")
    canvas.itemconfig(card_image, image=learning_lg_bg)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text="Portuguese", fill= "white")
    canvas.itemconfig(card_word, text=current_card["Portuguese"], fill="white")
    canvas.itemconfig(card_image, image=main_lg_bg)


#---------------------------------------------------#
window = Tk()
window.title("Flash Cards")
window.config(width=900, height=700, padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Canvas for the flash cards
canvas = Canvas(width=800, height=540, background=BACKGROUND_COLOR, highlightthickness=0)

#Defining the images for the flash cards
learning_lg_bg = PhotoImage(file=os.path.join(BASE_DIR, "images", "card_front.png"))
main_lg_bg = PhotoImage(file=os.path.join(BASE_DIR, "images", "card_back.png"))

card_image = canvas.create_image(400,270,image=learning_lg_bg)
card_title = canvas.create_text(400,150, text="Italian",font=(FONT_NAME, 30, "italic"))
card_word = canvas.create_text(400,270, text="word",font=(FONT_NAME, 55, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_image = PhotoImage(file=os.path.join(BASE_DIR, "images", "wrong.png"))
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file=os.path.join(BASE_DIR, "images", "right.png"))
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1,column=1)



known_lg_word = next_card()
mainloop()
