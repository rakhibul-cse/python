my_numbers = [20, 30, 10, 40, 80, 60, 80]
# my_numbers.reverse()
# print(my_numbers)

# my_numbers.sort()
# print(my_numbers)

# num_count = my_numbers.count(80)
# print(num_count)

num_index = my_numbers.index(30)
print(num_index)

copy_number = my_numbers.copy()
print(copy_number)
print(id(my_numbers))
print(id(copy_number))

print(copy_number)
copy_number.clear()
print(copy_number)