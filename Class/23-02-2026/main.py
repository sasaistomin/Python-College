list = [1, 2, 3, 4, 5]
summa = 0
for i in list:
    print(i)
    summa += i
print(summa)


colors = ["red", "green", "blue"]
colors.append("orenge")
colors.insert(1, "yellow")
print(colors)
colors.remove('red')
print(colors)

list = [1, 2, 3, 4, 5, 6]
num = int(input("Enter number: "))
count = 0
for i in list:
    if num == i:
        count += 1
print(count)


for i in range(len(list)):
    if num == list[i]:
        print(i)

list = [1, 2, 3, 4, 5, -4, -39]
sum = 0
for i in list:
    if i >= 0:
        sum += i
print(sum)

list = [1, 2, 4, 5, 3, 5, 29, 43, 44, 46]
count = 0
for i in range(len(list)):
    if list[i] % 2 == 0:
        count += 1
    
print(f"Count: {count}\n")  

list = [1, 2, 3, 4, 34, 34, 30, 12, 43, 4]
newList = []

for i in list:
    if i not in newList:
        newList.append(i)

print(list)
print(newList)

import random
list = []

for i in range(20):
    list.append(random.randint(10, 99))

print(list)

sum = 0
for i in list: 
    sum += i
print(sum)

sumP = 0
for i in list:
    if i % 2 == 0:
        sumP += i
print(sumP)

sumNP = 0
for i in list:
    if i % 2 != 0:
        sumNP += i
print(sumNP)

for i in range(len(list)):
    