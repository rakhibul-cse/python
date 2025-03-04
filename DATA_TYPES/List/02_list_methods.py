numbers = [10, 20, 10, 30, 40, 50]
new_nums = [60, 70]
print(numbers)
numbers.append(60) #append adds number in the last
print(numbers)
# numbers.append(new_nums)
# print(numbers) #[10, 15, 20, 30, 40, 50, 60, [60, 70]]
#to solve this problem use extend
numbers.extend(new_nums)
print(numbers)

numbers.insert(1,15) #insert adds number based on index
print(numbers)

numbers.remove(10) #remove only remove first matching number
print(numbers)

numbers.pop()
print(numbers)

numbers.pop(-1)
print(numbers)


