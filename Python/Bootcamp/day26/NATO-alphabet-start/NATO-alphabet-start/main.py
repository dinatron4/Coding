# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

import pandas
import os

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

alphabet_df = pandas.read_csv("Python\Bootcamp\day26\\NATO-alphabet-start\\NATO-alphabet-start\\nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"} letter code
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
character_list = []

for letter in user_input:
    character_list.append(alphabet_dict[letter.upper()])

print(character_list)

