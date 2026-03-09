# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно
# порахувати, скільки у списку парних і непарних чисел. Результати вивести
# на екран.

# arr = [19, 53, 10, 84, 81, 93, 25, 31, 22, 23, 34, 81, 89, 61, 84, 43, 43, 28, 53, 13]
# countP = 0 
# countNP = 0

# for item in arr:
#     if item % 2 == 0:
#         countP += 1
#     elif item % 2 != 0:
#         countNP += 1

# print(f"Parno: {countP}\nNe parno: {countNP}")

# Завдання 2
# Користувач із клавіатури вводить список цілих чисел. Необхідно
# визначити максимальне і мінімальне значення у списку. Результати
# вивести на екран.

# arr = [19, 53, 10, 84, 81, 93, 25, 31, 22, 23, 34, 81, 89, 61, 84, 43, 43, 28, 53, 13]

# maxNumber = arr[0]
# minNumber = arr[0]

# for item in arr:
#     if maxNumber < item:
#         maxNumber = item
#     elif minNumber > item:
#         minNumber = item

# print(f"Max: {maxNumber}\nMin: {minNumber}")


import random

arr = [random.randint(-99, 99) for i in range(20)]
print(f"Arr: ", end="")
for i in arr:
    print(i, end=" ")

posMaxNumber = arr[0]
posMinNumber = arr[0]

countNegNumber = 0
countPosNumber = 0
countNull = 0

for item in arr:
    if item > 0:
        countPosNumber += 1
        if posMaxNumber < item:
            posMaxNumber = item
    elif item < 0: 
        countNegNumber += 1
        if posMinNumber > item:
            posMinNumber = item
    elif item == 0:
        countNull += 1

print(f"\n\nMax posinive number: {posMaxNumber}\nMin positive number: {posMinNumber}\n")
print(f"Count posistive number: {countPosNumber}\nCount negetive number: {countNegNumber}\nCount noll: {countNull}")
