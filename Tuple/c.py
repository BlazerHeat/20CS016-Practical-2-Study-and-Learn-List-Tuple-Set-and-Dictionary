number_tuple = (1, 2, 3, 4, 5, 6)
print(f"Number tuple before adding: {number_tuple}")

number_list = list(number_tuple) # making list from tuple
number_list.append(7) # adding element

number_tuple = tuple(number_list) # making tuple from list

print(f"Number tuple after adding: {number_tuple}")
