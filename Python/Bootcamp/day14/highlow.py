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
    famous_pos = randint(0, SIZE_OF_DATA)
    if famous_pos in famous_used:
        random_celebrity(famous_used)
    famous_used.append(famous_pos)
    return famous_pos

SIZE_OF_DATA = len(data)
famous_selected = []
pos = random_celebrity(famous_selected) #First famous used in the game

while (True):
    display_logo()
    print(f"\nCompare A: {data[pos]["name"]} {data[pos]["second_name"]}, a {data[pos]["description"].title()}, from {data[pos]["country"].title()}")
    display_vs()
    pos = random_celebrity(famous_selected)
    print(f"Compare B: {data[pos]["name"]} {data[pos]["second_name"]}, a {data[pos]["description"].title()}, from {data[pos]["country"].title()}")
    #Choose one of the two famous
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    #Compare to see if the answer is right or wrong
    # if data[pos]["follower_count"] > data[pos]["follower_count"]:

    #If correct, increase the score and play again. Making their celebrity the first one

    #If wrong, end game and show score