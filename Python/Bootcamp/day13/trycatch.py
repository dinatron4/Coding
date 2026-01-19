while(True):
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("\nYou have typed an invalid number. Please try again.")

if age > 18:
    print(f"You can drive at age {age}.")