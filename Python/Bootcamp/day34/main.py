from tkinter import *
import requests
import os
BASE_DIR = os.path.dirname(__file__)


# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     data = response.json()
#     # print(data)
#     canvas.itemconfig(quote_text,text=data["quote"])
#     #Write your code here.

def right():
    pass

def not_right():
    pass


window = Tk()
window.title("Trivia Time")
window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
# canvas.grid(row=0, column=0)


#Buttons
true_image = PhotoImage(file=os.path.join(BASE_DIR, "quizzler-app-start", "images", "true.png"))
true_button = Button(image=true_image, highlightthickness=0, command=right)
true_button.grid(row=1, column=0)

false_image = PhotoImage(file=os.path.join(BASE_DIR, "quizzler-app-start", "images", "false.png"))
false_button = Button(image=false_image, highlightthickness=0, command=right)
false_button.grid(row=1, column=1)


#Python\\Bootcamp\\day34\\quizzler-app-start\\images\\false.png

window.mainloop()