# my_numbers = [1, 2, 3, 4]
# new_numbers = ([n + 1 for n in my_numbers])
# print(new_numbers)

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