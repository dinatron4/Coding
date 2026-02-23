from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    """Clean the password entry, and add a new  password"""

    password_entry.delete(0,END)

    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(abc)):
        abc.append(abc[i].upper())
    symbols = ["!","@","#","$","%","^","&","*","(",")","<",">",";","?","/","\\"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    # list_comp = [new_item for item in list]
    _letters = [choice(abc) for _ in range(randint(6,8))]
    _symbols = [choice(symbols) for _ in range(randint(2,4))]
    _numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = _letters + _symbols + _numbers
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Missing fields", message="Make sure all the fields are populated.")
    else:
        try:
            with open("./Python/Bootcamp/day30/JsonPassword/password_manager.json","r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("./Python/Bootcamp/day30/JsonPassword/password_manager.json","w") as file:
                json.dump(new_data, file, indent=2)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("./Python/Bootcamp/day30/JsonPassword/password_manager.json","w") as file:
                #Saving updated data
                json.dump(data,file, indent=2)            
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="Missing Website", message="Please, enter a website.")
    else:
        try:
            with open("./Python/Bootcamp/day30/JsonPassword/password_manager.json","r") as file:
                data = json.load(file)
        except (FileNotFoundError,KeyError):
            messagebox.showwarning(title="Missing Website", message="Website not registered.")
        else:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas for the picture
canvas = Canvas(width=200, height=200)
photo_image = PhotoImage(file="./Python/Bootcamp/day30/JsonPassword/logo.png")
canvas.create_image(100,100,image=photo_image)
canvas.grid(column=1, row=0)


#Labels
website_label = Label(text="Website:", font=(FONT_NAME, 8), justify="center")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=(FONT_NAME, 8), justify="center")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=(FONT_NAME, 8), justify="center")
password_label.grid(column=0, row=3)

#Entries
# website_entry = Entry(width=50)
# website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
# email_entry = Entry(width=50)
# email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
# password_entry = Entry(width=21)
# password_entry.grid(column=1, row=3, sticky="w")
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)
email_entry = Entry(width=52)
email_entry.insert(END, string="mdinato30@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3,sticky="w")

#Buttons
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save_details)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", command=search,width=15)
search_button.grid(column=2,row=1)








window.mainloop()