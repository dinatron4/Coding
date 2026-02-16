from tkinter import *
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save_details)
add_button.grid(column=1, row=4, columnspan=2)








window.mainloop()