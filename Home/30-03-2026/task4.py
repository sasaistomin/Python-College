#  Завдання 3
# Напишіть функцію, яка відображає порожній або заповнений квадрат з
# деякого символу. Функція приймає як параметри: довжину сторони
# квадрата, символ і змінну логічного типу:
# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.
def square(d, s, log):
    for i  in range(d):
        if log:
            print((s + ' ') * d)
        else:
            if i == 0 or i == d - 1:
                print((s + ' ') * d)
            else: 
                print(s + ' ' * (2 * d - 3) + s)

square(5, '*', True)
square(3, '*', False)


# Завдання 4
# Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа
# передаються як параметри
def Max(num1, num2, num3, num4, num5):
    arr = [num1, num2, num3, num4, num5]
    maxNumber = 0
    for i in arr:
        if maxNumber < i:
            maxNumber = i
    return maxNumber

print(Max(1, 4, 3, 19, 2))