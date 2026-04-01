# Завдання 1
# Напишіть функцію, яка відображає на екран форматований текст,
# зазначений нижче:
# "Don't compare yourself with anyone in this world…
#   if you do so, you are insulting yourself."
#       Bill Gates
def printQuote():
    # Потрійні лапки зберігають форматування (переноси та відступи)
    return """\"Don't compare yourself with anyone in this world...
    if you do so, you are insulting yourself.\"
        Bill Gates"""

print(printQuote())
# Завдання 2
# Напишіть функцію, яка приймає два числа як параметр і відображає всі
# парні числа між ними.
def ParNumder(num1, num2):
    for i in range(num1, num2+1):
        if i % 2 == 0:
            print(i)
ParNumder(1, 10)