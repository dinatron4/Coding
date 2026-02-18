from tkinter import *
from tkinter import messagebox
from  random import randint, choice, shuffle

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

    password_entry.insert(END, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Missing fields", message="Make sure all the fields are populated.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                    f"Email: {email}\nPassword: {password}\nIs it ok to save?")
        
        if is_ok:
            with open("./Python/Bootcamp/day29/password-manager-start/password_manager.csv","a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas for the picture
canvas = Canvas(width=200, height=200)
photo_image = PhotoImage(file="./Python/Bootcamp/day29/password-manager-start/logo.png")
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
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
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








window.mainloop()