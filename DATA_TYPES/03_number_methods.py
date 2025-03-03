# Number built in functions

#1. abs(): it returns positive value , but for complex number it returns magnitude. example : √(3² + 4²) = √(9+16) = √25 = 5.0)
print(abs(-10))
print(abs(10))
print(abs(3 + 4j))

#2. pow(): 
print(pow(2,3))
print(pow(2,3,3))

#3. round()
print(round(4.6))   # 5
print(round(4.4))   # 4
print(round(4.5))   # 4  (Even rounding rule)
print(round(5.5))   # 6  (Even rounding rule)

print(round(3.14159, 2))  # 3.14
print(round(3.14159, 3))  # 3.142
print(round(9.8765, 1))   # 9.9


#4. divmod()
print(divmod(10, 3))  # (3, 1)
print(divmod(20, 4))  # (5, 0)
print(divmod(25, 7))  # (3, 4)


#5. max()
numbers = [2,3,4,65]
print(max(numbers))
numbers = [10, 25, 40, 5]
print(max(numbers))  # 40

print(max(3, 7, 2, 9))  # 9
print(max("apple", "banana", "cherry"))  # cherry (অক্ষর অনুযায়ী বড়)


#6. min()
numbers = [10, 25, 40, 5]
print(min(numbers))  # 5

print(min(3, 7, 2, 9))  # 2
print(min("apple", "banana", "cherry"))  # apple


#7. sum():
numbers = [10, 20, 30]
print(sum(numbers))  # 60

print(sum(numbers, 5))  # 60 + 5 = 65
print(sum((1, 2, 3, 4, 5)))  # 15 (টাপলের জন্য)

#8. isinstance():
x = 10
print(isinstance(x, int))  # True
print(isinstance(x, float))  # False
print(isinstance(x, str))  # False
