PLACEHOLDER = "[name]"

with open("./Python/Bootcamp/day24/Names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()

with open("./Python/Bootcamp/day24/Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Python/Bootcamp/day24/Output/ReadyToSend/{stripped_name}.txt", "w+") as complete_letter:
            complete_letter.write(new_letter)