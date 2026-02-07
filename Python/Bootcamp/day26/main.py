import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)

# # Loop through a data frame
# for (key, value) in student_df.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    print(row.student)