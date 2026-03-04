# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# for i in range(num1, num2 + 1):
#     print(i)
#
#
# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# for i in range(num1, num2 + 1):
#     if(i % 2 != 0):
#         print(i)
#
#
# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# i = num1 + num2
# while i >= 0:
#     if i % 2 == 0:
#         print(i)
#     i -= 1
#
#
# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# do = input("Do(1)>, 2) <: ")
# if do == "1" or do == ">":
#     i = 0
#     fNum = num1 + num2
#     while i < fNum:
#         print(i)
#         i += 1
# elif do == "2" or do == "<":
#     i = num1 + (num2 - 1)
#     while i > 0:
#         print(i)
#         i -= 1
#
#
# num = input("Enter number: ")
# count = 0
# summa = 0
# while num:
#     count = count + 1
#     summa = summa + int(num[0])
#     num = num[1:]
# print(f"Sum {summa}\nCount {count}, Av {summa/count}")

l1 = "*"
l2 = "-"
coll = 3
len = 8
heigt = 2

while heigt > 0:
    while coll > 0:
        while len > 0:
            if len % 2 == 0:
                print(l1 * coll, end="")
            else:
                print(l2 * coll, end="")
            len -= 1
        print()
        coll -= 1
    heigt -= 1