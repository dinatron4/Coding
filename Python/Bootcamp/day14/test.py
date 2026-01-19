# list_fruits = ["banana", "apple", "mango"]
# print(list_fruits[0])
# list_fruits[0], list_fruits[2] = list_fruits[2], list_fruits[0]
# print(list_fruits[0])
from random import randint

def random_celebrity(famous_used):
    """Return a position for a famous that was not used yet in the game"""
    famous_pos = randint(0, 9)
    if famous_pos in famous_used:
        random_celebrity(famous_used)
    famous_used.append(famous_pos)

mylist = []

for i in range (1,50):
    random_celebrity(mylist)
    print(mylist)
