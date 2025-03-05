#using for loop
numbers = [1, 2, 3, 4]
squared_nums = []
for i in numbers:
    squared_nums.append(i**2)
print(squared_nums)

#list comprehension syntax: new_list = [expression for item in iterable if condition]

#using lis comprehension
my_numbers = [2, 4, 8]
squared_my_nums = [x**2 for x in my_numbers]
print(squared_my_nums)

#list comprehension with range
squared = [y**2 for y in range(10,20,2)]
print(squared)