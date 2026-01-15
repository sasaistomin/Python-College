# print("Hello World")

# name = input("Enter name: ")
# print("Hello world \nMy name: " + name)
# Канкатенація - складання рядків
# input() не явне очікування

# age = input("Entre age: ")
# print("My age is: " + age)

# Переміні(Veriable)
# 1) nostylecase = 0 # No style
# 2) camelCaseStyle = 1 # Camel case
# 3) kebab-case-style = 2 # Kebab case, не підтримується в python
# 4) snake_style = 3 # Snake style
# На початку зміної можна літеру, але не можна число

# Типи даниих
# str string - рядок # використовуємо лапки "Hello" або 'Hello' # name = 'Sasha'
# int integer - число # 5 10 # number = 1
# float float - дроб # 5.0 # heigh = 1.76
# bool boolean - правда або не правда # True False # is_student = True
# print(name, number, heigh, is_student)
# Те що мі пишем в рядкаж рахується як символ
# print("{}".format(name)) - в {} будет писать зміна та що йде в format. Тобто якщо ("{} {} {}".format(name, age, is_studing)), то в перших {} буде імʼя, а в інших буде так далі

# print(name, number, haigh, is_student)
# print(name + ' ' + str(number) + ' ' + str(haigh) + ' ' + str(is_student))
# print("{} {} {} {}".format(name, number, haigh, is_student))
# print(f"{name} {number} {haigh} {is_student}")

name = "Sasha"
age = 17
haigh = 1.74
is_student = True

print(f"My name is {name} and my age is {age} and my haigh is {haigh} and my is_student is {is_student}")
print("My name is", name, "and my age is", age, "and my haigh is", haigh, "and my is_student is", is_student)
print("My name is " + name + " and my age is " + str(age) + " and my haigh is " + str(haigh) + " and my is_student is " + str(is_student))
print("My name is {} and my age is {} and my haigh is {} and my is_student is {}".format(name, age, haigh, is_student))