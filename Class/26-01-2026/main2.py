# Користувач вводить з клавіатури число. Необхідно перевірити його на парність і непарність.
# Якщо число парне потрібно вивести на екран число і напис "Even number". Якщо число непарне виведіть на екран число і напис "Odd number".

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# Користувач вводить із клавіатури число. Необхідно перевірити його на кратність 7. Якщо число кратне потрібно вивести на екран число і напис "Number is multiple 7".
# Якщо число не кратне виведіть на екран число і напис "Number is not multiple 7".

num = int(input("Enter a number: "))
if num % 7 == 0:
    print("7 even number")
else:
    print("odd number")

# Користувач вводить з клавіатури два числа. Необхідно знайти максимум з двох чисел і показати його на екран.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print("=")

# Користувач вводить з клавіатури два числа. Необхідно знайти мінімум з двох чисел і показати його на екран.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    print(num2)
elif num1 < num2:
    print(num1)
else:
    print("=")

# Користувач вводить з клавіатури два числа. Залежно від вибору користувача потрібно показати суму двох чисел, різницю двох чисел, середньоарифметичне
# або добуток двох чисел.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
do = input("Enter do: ")

if do == "+":
    print(num1 + num2)
elif do == "-":
    print(num1 - num2)
elif do == "*":
    print(num1 * num2)
elif do == "/":
    print(num1 / num2)


# Користувач вводить із клавіатури суму в доларах, потім обирає валюту, у яку хоче перевести цю суму: євро (EUR), фунти (GBP) або єни (JPY).
# Після вибору валюти програма запитує курс обраної валюти по відношенню до долара. Програма повинна розрахувати і вивести суму в обраній валюті.

