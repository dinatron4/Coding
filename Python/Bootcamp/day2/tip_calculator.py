#Tip calculator
print("Welcome to the tip calculator!")

bill_to_pay = float(input("What was the total bill? $"))
tip = int(input("How much tip would like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

#Calculating total amount with tip and dividing by the number of people
price_per_person = round(bill_to_pay*(1+tip/100)/people,2)

print(f"Each person should pay: {price_per_person}")