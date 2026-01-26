import os

with open(os.getcwd() + "\\Python\\Bootcamp\\day24\\Files\\my_file.txt") as file:
    contents = file.read()
    print(contents)

with open(os.getcwd() + "\\Python\\Bootcamp\\day24\\Files\\my_file.txt", mode="a") as file:
    file.write("\nAppending text")
    print(contents)
