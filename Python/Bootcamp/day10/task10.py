def calculator(first, second, op):
    """Take the numbers inputed by the user and do a math operation
    +: add
    -: substract
    *: multiply
    /: divide"""
    match op:
        case "+":
            result = first + second
        case "-":
            result = first - second
        case "*":
            result = first * second
        case "/":
            result = first / second
    return result

def main():
    quit = "y"
    while quit == "y":
        flag = "y"
        first_number = int(input("What's the first number?: "))
        print("+\n-\n*\n/")
        while flag == "y":
            operation = input("Pick an operation: ")
            second_number = int(input("What's the next number?: "))
            result = calculator(first_number, second_number, operation)
            print(f"{first_number} {operation} {second_number} = {result}")
            flag = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()
            first_number = result
        quit = input("Type 'y' to start calculating, or 'n' to quit: ")
        print("\n"*100)
    print("Thanks for calculating with us")



if __name__ == "__main__":
   main() 