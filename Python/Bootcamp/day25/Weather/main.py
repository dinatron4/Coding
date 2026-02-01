# import csv

# with open("./Python/Bootcamp/day25/Weather/weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []    
#     for row in data:
#         if len(row[1]) == 2:
#             temperature.append(int(row[1]))

#     print(temperature)

import pandas

# data = pandas.read_csv("./Python/Bootcamp/day25/Weather/weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data["temp"].to_list()

# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())

# #Selecting columns
# print(data["condition"])
# print(data.condition)

#Selecting rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp*9/5+32
# print(monday_temp_F)

# print(monday.condition)

#Create a datafram from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("./Python/Bootcamp/day25/Weather/new_data.csv")