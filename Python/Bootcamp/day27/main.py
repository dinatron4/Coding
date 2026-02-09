from tkinter import *

def button_clicked():
    temp_f = entry.get()
    temp_f = int(temp_f)
    temp_c = round((temp_f - 32)*5/9,2)
    output.config(text=temp_c)

window = Tk()
window.title("Fahrenheit to Celsius")
window.minsize(width=300, height=100)
window.config(padx=55, pady=20)

#Fixed labels
label1 = Label(text="°F", font=("Arial", 12))
label1.grid(column=2, row=0)
label2 = Label(text="is equal to", font=("Arial", 12))
label2.grid(column=0, row=1)
label3 = Label(text="°C", font=("Arial", 12))
label3.grid(column=2, row=1)
label3.config(pady=15)


#Output Label
output = Label(font=("Arial", 12))
output.grid(column=1,row=1)

#Button

button1 = Button(text="Calculate", command=button_clicked)
button1.grid(column=1, row=2)

#Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)




window.mainloop()