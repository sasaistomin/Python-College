num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

print("1) +")
print("2) *")
do = int(input("What you want to do: "))
if do == 1:
    print(f"Sum: {num1 + num2 + num3}")
elif do == 2:
    print(f"Product: {num1 * num2 * num3}")
else:
    print("Invalid")


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

print("1) max")
print("2) min")
print("3) ser")
do = int(input("What you want to do: "))

if do == 1:
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num1 and num3 > num2:
        print(num3)
elif do == 2:
    if num1 < num2 and num1 < num3:
        print(num1)
    elif num2 < num1 and num2 < num3:
        print(num2)
    elif num3 < num1 and num3 < num2:
        print(num3)
elif do == 3:
    result = (num1 + num2 + num3) / 3
    print(result)


ots = int(input("Enter ots: "))
if ots == 1:
    print("Дуже погано")
elif ots == 2:
    print("Погано")
elif ots == 3:
    print("Задовільно")
elif ots == 4:
    print("Добре")
elif ots == 5:
    print("Відмінно")


lenght = int(input("Enter lenght: "))
print("1) Convert to one of the units of your choice")
print("2) Convert and print all")
print("3) Convert to kilometers and centimeters")
do = int(input("What you want to do: "))
if do == 1:
    print("1) cute")
    print("2) inches")
    print("3) yard")
    do1 = int(input("What you want to do: "))
    if do1 == 1:
        print(f"Cute: {lenght / 1.609344}")
    elif do1 == 2:
        print(f"Inches: {lenght * 39370.1}")
    elif do1 == 3:
        print(f"Yard: {lenght / 1093.61}")
elif do == 2:
    print(f"Cute: {lenght / 1.609344}\n"
          f"Inches: {lenght * 39370.1}\n"
          f"Yard: {lenght / 1093.61}")
elif do == 3:
    print(f"Centimeter: {lenght * 100000}")


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print("1) +")
print("2) -")
print("3) *")
print("4) /")
print("5) **")
do = int(input("What you want to do: "))

if do == 1:
    print(num1 + num2)
elif do == 2:
    print(num1 - num2)
elif do == 3:
    print(num1 * num2)
elif do == 4:
    print(num1 / num2)
elif do == 5:
    print("1) num1 ** num2")
    print("2) num2 ** num1")
    do5 = int(input("What you want to do: "))
    if do5 == 1:
        print(num1 ** num2)
    elif do5 == 2:
        print(num2 ** num1)



num = int(input("Enter number: "))

num1 = num // 100
num2 = num // 10
num3 = num % 10

if num1 == num2 == num3:
    print("Всі цифри однакові")
else:
    print("Цифри різні")