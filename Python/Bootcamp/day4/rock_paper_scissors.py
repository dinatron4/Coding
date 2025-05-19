import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0,2)
action_list = [rock, paper, scissors]

print(action_list[user_choice])
print(f"Computer chose:\n{action_list[computer_choice]}")

# Rock > Scissors || Scissors > Paper || Paper > Rock

if (user_choice == 0 and computer_choice == 2 or
user_choice == 2 and computer_choice == 1 or
user_choice == 1 and computer_choice == 0):
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
else:
    print("You lose!")