my_list_1 = [1, 2, 3, 4, 5]
rev_my_list_1 = my_list_1.reverse() #reverse change the original list and it returns none
print(my_list_1)

list_2 = [5, 10, 15, 20, 25]
rev_list_2 = reversed(list_2)
print(rev_list_2) #reversed return an iterable object. so we have to convert it in expected format like list, tuple, string
rev_list_2 = list(reversed(list_2))
print(rev_list_2)

#reverse a string method 1
my_name = "Zenitsu"
rev_my_name = "".join(reversed(my_name))
print(rev_my_name)

#reverse a string method 2
rev_my_name2 = my_name[::-1]
print(rev_my_name2)

#reverse a string method 3
your_name = "Nezuko"
rev_your_name = ""
for char in your_name:
    rev_your_name = char + rev_your_name
print(rev_your_name)
