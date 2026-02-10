from tkinter import *

window = Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

#Button
def button_clicked():
    entry_input = entry.get()
    my_label.config(text=entry_input)

button = Button(text="Click me", command=button_clicked)
button.pack()

#Entry
entry = Entry(width=20)
entry.insert(END, string="Enter your name") #Add some text to begin
entry.pack()

#Text
text = Text(height=5, width=30)
text.focus() #Put cursor in textbox
text.insert(END, "Example of\nmulti-line text entry")
print(text.get("1.8", END)) # X.Y = Text starting from X line, and character Y
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    #Called with current scale value
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(check_state.get())

check_state = IntVar() #Variable to hold on to checked state, 0 is off, 1 is on
checkbutton = Checkbutton(text="Is On?", variable=check_state, command=checkbutton_used)
check_state.get()
checkbutton.focus()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()