from tkinter import *
from random import choice
import pandas
#-------------- CONSTANTS --------------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

#---------------------------------------------------#
data = pandas.read_csv("Python\Bootcamp\day31\data\italian_words.csv")
to_learn = data.to_dict(orient="records")

#--------------- FUNCTIONS -------------------------#
def next_card():
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="Italian")
    canvas.itemconfig(card_word, text=current_card["Italian"])
    




#---------------------------------------------------#
window = Tk()
window.title("Flash Cards")
window.config(width=900, height=700, padx=50, pady=50, bg=BACKGROUND_COLOR)


#Canvas for the flash cards
canvas = Canvas(width=800, height=540, background=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./Python/Bootcamp/day31/images/card_front.png")
canvas.create_image(400,270,image=front_image)
card_title = canvas.create_text(400,150, text="Italian",font=(FONT_NAME, 30, "italic"))
card_word = canvas.create_text(400,270, text="word",font=(FONT_NAME, 55, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

back_card = Canvas(width=800, height=540, background=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file="./Python/Bootcamp/day31/images/card_back.png")
back_card.create_image(400,270,image=back_image)

#Label
# language_entry = Label(text="Italian",font=(FONT_NAME, 30, "italic"), justify="center",bg="white")
# language_entry.place(x=360,y=130)
# word_entry = Label(text="pizza",font=(FONT_NAME, 55, "bold"), justify="center",bg="white")
# word_entry.place(x=340,y=230)

#Buttons
wrong_image = PhotoImage(file="./Python/Bootcamp/day31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="./Python/Bootcamp/day31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1,column=1)



next_card()
mainloop()
