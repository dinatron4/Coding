import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

alphabet_df = pandas.read_csv("Python\Bootcamp\day26\\NATO-alphabet-start\\NATO-alphabet-start\\nato_phonetic_alphabet.csv")
is_valid_word = False

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"} letter code
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while not is_valid_word:
    user_input = input("Enter a word: ").upper()
    try:
        character_list = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(character_list)
        is_valid_word = True

