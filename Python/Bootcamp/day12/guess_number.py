import random
from logo import logo

def check_input(answer, input):
    if input > answer:
        print("Too high.")
    elif input < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")
        return 1
    return 0

def main():
    
    the_number = random.randint(1,100)
    game_modes = {"easy": 10, "hard": 5}
    flag = 0

    print(logo)
    print("Welcome to th Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    #print(f"Pssst, the correct answer is {the_number}")

    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempt = game_modes[user_input]

    # for i in range (0, attempt):
    #     print(f"You have {attempt - i} attempts remaining to guess the number.")
    #     guess = input("Make a guess: ")
    #     flag = check_input(the_number,guess)
    while flag == 0 and attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        flag = check_input(the_number,guess)
        attempt -= 1
    
    if flag == 0:
        print(f"The answer was {the_number}. Better luck next time")



if __name__ == "__main__":
    main()