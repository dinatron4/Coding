# Types of coffee and price
# Espresso - 50ml Water + 18g Coffee = 1.50
# Latte - 200ml Water + 24g Coffee + 150ml Milk = 2.50
# Cappuccino - 250ml Water + 24g Coffee + 100ml Milk = 3.00
#################################################################
# Initial resources - 300ml Water / 200ml Milk / 100g Coffee
# American coins - Penny = 1 cent / Nickel = 5 cents / Dime = 10 cents / Quarter = 25 cents

from materials import resources, MENU

def check_resources(type_of_coffee, qty_resources, menu):
    """Return True if order can be made, and False if ingredients are insufficient"""
    for item, qty_required in menu[type_of_coffee]["ingredients"].items():
        if qty_resources[item] < qty_required:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def display_report(resources, money):
    for item, qty in resources.items():
        if item != "coffee":
            print(f"{item.title()}: {qty}ml")
        else:
            print(f"{item.title()}: {qty}g")
    print(f"Money: ${money}")
    
def calculate_expense(paid, type_of_coffee, qty_resources, menu):
    """Return the money to add to the machine after a successfull payment"""
    money = 0
    if menu[type_of_coffee]["cost"] > paid:
        print("Sorry that is not enotgh money. Money refunded.")
    else:
        change = round(paid - menu[type_of_coffee]["cost"], 2)
        print(f"Here is ${change} in change")
        print(f"Here is your {type_of_coffee}. Enjoy!")
        money += menu[type_of_coffee]["cost"]
        for item in qty_resources:
            qty_resources[item] -= menu[type_of_coffee]["ingredients"][item]
    return money

machine_on = True
make_coffee = True
money_machine = 0

while machine_on:
    # Ask which type of coffee the user wants
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        machine_on = False
        break
    elif user_input == "report":
        display_report(resources, money_machine)
    else:
        if user_input in MENU:
            make_coffe = check_resources(user_input, resources, MENU)
            # If yes, ask for the money / If no, tell them that we dont have enough resource
            if make_coffe == True:
                num_quarte = int(input("How many quarters?: "))
                num_dime = int(input("How many dimes?: "))
                num_nickle = int(input("How many nickels?: "))
                num_penny = int(input("How many pennies?: "))
                total_money = 0.25*num_quarte + 0.10*num_dime + 0.05*num_nickle + 0.01*num_penny

                # Calculate the money used to pay, and report to the user (change or refund)
                money_machine += calculate_expense(total_money, user_input, resources, MENU)
        else:
            print("Please, enter a valid drink.")


