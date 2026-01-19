#People list with the number of users in instagram
from game_data import data
from random import randint
from art import logo, versus

def display_logo():
    print(logo)

def display_vs():
    print(versus)

def random_celebrity(famous_used):
    """Return a position for a famous that was not used yet in the game"""
    famous_pos = randint(0, SIZE_OF_DATA-1)
    if famous_pos in famous_used:
        while famous_pos in famous_used:
            famous_pos = randint(0, SIZE_OF_DATA-1)
    famous_used.append(famous_pos)

def check_answer(user_letter, score, celebrities):
    if user_letter == "A":
        if data[celebrities[0]]["follower_count"] >= data[celebrities[-1]]["follower_count"]:
            #If correct, increase the score and play again.
            score += 1
            display_logo()
            print(f"You are right! Current score: {score}")
            return True, score, celebrities
        else:
            return False, score, celebrities
    else:
        if data[celebrities[-1]]["follower_count"] >= data[celebrities[0]]["follower_count"]:
            #If correct, increase the score and play again. Making their celebrity the first one
            score += 1
            display_logo()
            print(f"You are right! Current score: {score}")
            celebrities[0], celebrities[-1] = celebrities[-1], celebrities[0]
            return True, score, celebrities
        else:
            return False, score, celebrities

SIZE_OF_DATA = len(data)
famous_selected = []
score = 0
playing_game = True
random_celebrity(famous_selected) #First famous used in the game
display_logo()

while (playing_game):
    print(f"Famous list: {famous_selected}")
    print(f"\nCompare A: {data[famous_selected[0]]["name"]} {data[famous_selected[0]]["second_name"]}, a {data[famous_selected[0]]["description"].title()}, from {data[famous_selected[0]]["country"].title()}")
    # print(data[famous_selected[0]]["follower_count"])
    display_vs()
    random_celebrity(famous_selected)
    print(f"Compare B: {data[famous_selected[-1]]["name"]} {data[famous_selected[-1]]["second_name"]}, a {data[famous_selected[-1]]["description"].title()}, from {data[famous_selected[-1]]["country"].title()}")
    # print(data[famous_selected[-1]]["follower_count"])
    #Choose one of the two famous
    answer = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()
    print("\n"*100)
    #Compare to see if the answer is right or wrong
    playing_game, score, famous_selected = check_answer(answer, score, famous_selected)
    if score == 59:
        playing_game = False

#If wrong, end game and show score
display_logo()
if score == 59:
    print("You have beaten the game. Congratulations!")
else:
    print(f"Sorry, that's wrong. Final score: {score}")