import random
import pandas as pd

my_numbers = [1, 2, 3, 4]
new_numbers = [n + 1 for n in my_numbers]
print(new_numbers)

name = "Angela"
letters_list = [letter for letter in name if letter != "a"]
print(letters_list)
print(type(letters_list))
separator = ''
join_list = separator.join(letters_list)
print(join_list)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

# Conditional List Comprehension
name_list = ["Bayo", "Joshua", "Beth", "Alex", "Jossy"]
short_name = [name for name in name_list if len(name) < 5]
cap_name = [name.upper() for name in name_list]
print(cap_name)

# Dictionary Comprehension
students_score = {student:random.randint(1, 100) for student in name_list if random.randint(1, 100) > 50}
print(students_score)

# Iterate over Pandas Dataframe.

student_dict = {
    "student": ["Bayo", "Joshua", "Beth", "Alex", "Jossy"],
    "scores": [56, 76, 96, 84, 61]
}
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)
for(index, row) in student_data_frame.iterrows():
    if row.student == "Bayo":
        print(row.student)
        print(row.scores)
