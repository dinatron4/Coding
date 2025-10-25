# number = int(input("Enter a random number: "))

# if number % 2 == 0:
#     print("Your number is even")
# else:
#     print("Your number is odd")


print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L: ").lower()
value = 0
flag = 0

if size == "s":
    value += 15
    print(f"The small pizza costs U${value},00")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
    if pepperoni == "y":
        value += 2
        print(f"With pepperoni it will be U${value},00")

elif size == "m":
    value += 20
    print(f"The medium pizza costs U${value},00")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
    if pepperoni == "y":
        value += 3
        print(f"With pepperoni it will be U${value},00")
elif size == "l":
    value += 25
    print(f"The large pizza costs U${value},00")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
    if pepperoni == "y":
        value += 3
        print(f"With pepperoni it will be U${value},00")
else:
    print("Sorry, but we don't have this size here.")
    flag = 1
if flag != 1:    
    extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
    if extra_cheese == "y":
        value += 1
        print(f"With extra cheese it will be U${value},00")
    else:
        print(f"So the total price will be U${value},00")


