# FileNotFound
# with open("file.txt", "r") as file:
#     file.read()

# KeyError
# my_dict = {"key": "value"}
# value = my_dict["not_a_key"]

# IndexError
# my_list = [1,2,3]
# print(my_list[5])

# TypeError
# text = "abc"
# print(text + 5)

#TRY
#Something that might cause an exception
#EXCEPT
#Do this if there was an exception
#ELSE
#Do this if there were no exceptions
#FINALLY
#Do this no matter what happens

try:
    file = open("./Python/Bootcamp/day30/errors/file.txt")
    my_dict = {"key": "value"}
    print(my_dict["key"])
except FileNotFoundError:
    open("./Python/Bootcamp/day30/errors/file.txt", "w")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")