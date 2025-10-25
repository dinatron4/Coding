programming_dictionary = {
    "Bug": "An error in a program",
    "Function": "A piece of code that ...",
    }

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

# empty_dictionary = {}

# programming_dictionary = {}

programming_dictionary["Bug"] = "It is an insect"

print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nested list in dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print(travel_log["France"][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    }
}

print(travel_log["Germany"]["cities_visited"][2])
print(travel_log["Germany"]["total_visits"])

