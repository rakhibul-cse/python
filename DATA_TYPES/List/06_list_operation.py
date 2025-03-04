import sys
basket_1 = ["apple", "orange", "banana"]
basket_2 = ["date", "lichi", "grape", "guava"]
# print(sys.getsizeof(basket_1))
# print(sys.getsizeof(basket_2))

#concatenation
basket3 = basket_1 + basket_2
print(basket3)

#replication
basket_4 = basket_1 * 3
print(basket_4)

print("lichi" in basket_2)
print("watermelon" not in basket_2)