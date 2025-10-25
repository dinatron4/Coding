def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    should_accumulate = True
    n1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    while should_accumulate:
        op = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        answer = operations[op](n1,n2)
        print(f"{n1} {op} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()

def main():
    calculator()


if __name__ == "__main__":
    main()