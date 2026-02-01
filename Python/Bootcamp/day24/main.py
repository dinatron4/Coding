

with open("Python/Bootcamp/day24/Input/Letters/starting_letter.txt", "r") as file:
    letter_context = file.readlines()

with open("Python/Bootcamp/day24/Names/invited_names.txt", "r") as file:
    names = file.readlines()

print(names)

for name in names:
    aux = []
    aux = letter_context.copy()
    name = name.replace("\n", "")
    # print(name)
    # print(type(name))
    aux[0] = aux[0].replace("[name]", name)
    with open("Python/Bootcamp/day24/Output/ReadyToSend/" + name + ".txt", "w+") as file:
        # print(aux)
        file.writelines(aux)