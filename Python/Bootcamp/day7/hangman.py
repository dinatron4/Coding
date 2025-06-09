import os
import random
import hangman_art, hangman_words

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initializing variables
placeholder = ""
display = ""
lives = 6
guessed_letters =[]
correct_letters = []
# chosen_word = random.choice(hangman_words.one_piece_characters).lower()
name_character = random.choice(list(hangman_words.one_piece_character_hints.keys()))
chosen_word = name_character.lower()
clear_terminal()
# print(chosen_word)

# Creating the word "silhouette"
for letter in chosen_word:
    if letter == " ":
        placeholder += " "
    else:
        placeholder += "_"

print("Guess the One Piece character:")
print(hangman_art.stages[lives])
print(placeholder)

# display = ["_" for _ in chosen_word]

while display != chosen_word and lives != 0:
    guess = input("Guess one letter?\n").lower()
    clear_terminal()
    if guess in guessed_letters:
        print(f"You have tried {guess.upper()} before. Try a new one!")
    else:
        guessed_letters.append(guess)
        display = ""

        for letter in chosen_word:
            if letter == guess: # If user guess a letter right, add to display and correct letters
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters: # Keep track of the correct letters guessed to display
                display += letter
            elif letter == " ": # Checking for spaces, so user does not need to enter it
                display += " "
            else:
                display += "_" # Adding the missing letters

        if guess not in chosen_word: # Guessed wrong, lose one life
            lives -= 1
            hints = hangman_words.one_piece_character_hints[name_character]
            print(f"The letter {guess} is not in this word.")

    print("Guess the One Piece character:")
    print(hangman_art.stages[lives])
    print(f"Letters guessed: {", ".join(guessed_letters)}")
    if lives <= 3:
        print(f"\n----- First apparition: {hints["first_arc"]} -----")
    if lives <= 2:
        print(f"----- Devil Fruit: {hints["devil_fruit"]} -----")
    if lives <= 1:
        print(f"----- Affiliation {hints["affiliation"]} -----")
    print("\n" + display)
    print(f"****************************{lives} LIVES LEFT****************************")

if lives == 0:
    print(f"\nYou lose! The answer was {chosen_word.capitalize()}")
else:
    print(f"\nYou win! You guessed {chosen_word.capitalize()}")

    # print(display)
    # for index, letter in enumerate(chosen_word):
    #     if letter == guess:
    #         display[index] = letter
    # print("".join(display))