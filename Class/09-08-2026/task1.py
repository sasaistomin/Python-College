# fruits = ("banana", "apple", "pear", "peach", "pineaple", "banana")
# examination = "banana"
# count = 0
# for i in fruits:
#     if examination in i:
#         count += 1

# print(count)

# manufacturers = (
#     "Toyota", "BMW", "Ford", "Honda", "Audi",
#     "Toyota", "Mercedes", "Nissan", "Kia", "Hyundai",
#     "BMW", "Mazda", "Volkswagen", "Ford", "Skoda",
#     "Peugeot", "Renault", "Toyota", "Audi", "Chevrolet"
# )
# w = input("Enter auto: ")
# word = input("Enter word: ")
# for i in manufacturers:
#     if w in i:
#         print(word)
#     else:
#         print(i)

import random

random.seed(42)
digits = [random.randint(1, 999) for i in range(100)]
print(digits)

countOne = 0
countTwo = 0
countThee = 0

for digit in digits:
    if len(str(digit)) == 1:
        countOne += 1
    elif len(str(digit)) == 1:
        countTwo += 1
    elif len(str(digit)) == 1:
        countThee += 1

