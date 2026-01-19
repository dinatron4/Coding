import logo
import random

def sum(cards_in_hand):
    total = 0
    for element in cards_in_hand:
        total += element
    return total

def dealing_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return cards[random.choice(cards)]

choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while choice == 'y':
    flag = 1
    extra_card = 'y'
    print(logo.logo)
    user_hand =[dealing_cards(), dealing_cards()]
    computer_hand = [dealing_cards()]

    while extra_card == 'y':
        user_total = sum(user_hand)
        computer_total = sum(computer_hand)
        print(f"\tYour cards: {user_hand}, current score: {user_total}")
        print(f"\tComputer's first card: {computer_hand[0]}")
        extra_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if extra_card == 'n':
            print(f"\tYour cards: {user_hand}, current score: {user_total}")
            break
        user_hand.append(dealing_cards())
        user_total = sum(user_hand)
        if user_total> 21:
            flag = 0
            break
    
    while computer_total < 17 and computer_total < 22 and flag == 1 and computer_total < user_total:
        computer_hand.append(dealing_cards())
        computer_total = sum(computer_hand)
        print(f"\tComputer's cards: {computer_hand}, current score: {computer_total}")
    
    print(f"\tYour final hand: {user_hand}, current score: {user_total}")
    print(f"\tComputer's final hand: {computer_hand}, final score: {computer_total}")
    if flag == 0: print("You went over. You lose :(")
    elif computer_total > 21: print("Computer went over. You win :)")
    elif computer_total >= user_total: print("You lose.")
    else: print("You win.")
        
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    print("\n"*100)



    