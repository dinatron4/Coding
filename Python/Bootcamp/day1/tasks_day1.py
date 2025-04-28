#Printing string with multiple texts
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
print("------------------------------------------------------------")

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.\n------------------------------------------------------------")

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n"
      "2. Knead the dough for 10 minutes.\n"
      "3. Add 3g of Salt.\n"
      "4. Leave to rise for 2 hours.\n"
      "5. Bake at 200 degrees C for 30 minutes.\n"
      "------------------------------------------------------------")

#Concatenating strings
print("Hello " + "Matheus")
print("------------------------------------------------------------")

#Input function
print ("Hello " + input("What is your name? ") + "!")
print("------------------------------------------------------------")

#Variable
username = input("What is your name? ")
length = len(username)
print("Your name has " + str(length) + " characters")