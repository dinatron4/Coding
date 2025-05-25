import random

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(abc)):
    abc.append(abc[i].upper())
symbols = ["!","@","#","$","%","^","&","*","(",")","<",">",";","?","/","\\"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

character_list = []

for k in range(num_letters):
    character_list.append(abc[random.randint(0, len(abc)-1)])
for j in range(num_symbols):
    character_list.append(symbols[random.randint(0, len(symbols)-1)])
for i in range(num_numbers):
    character_list.append(numbers[random.randint(0, len(numbers)-1)])

print(character_list)
password = []

while character_list is not []:
    password.append(character_list.pop(random.randint(0,len(character_list)-1)))
    if len(character_list) == 0: break

print(password)
password = ''.join(password)
print(password)