#1 
name = 'Sasha'
age = 17
city = 'Odesa'
isStudent = True

#2
number1 = int(input('Enter number1: '))
number2 = int(input('Enter number2: '))
print(f'number1 + number2 = {number1 + number2} \nnumber1 - number2 = {number1 - number2} \nnumber1 * number2 = {number1 * number2} \nnumber1 / number2 = {number1 / number2}')

#3
a = int(input('Enter a: '))
b = int(input('Enter b: '))
h = int(input('Enter h: '))

v = a * b * h
print(v)

#4
num = input('Enter number: ')
print(f'Int: {int(num)}\nFloat: {float(num)}')

#5
num1 = 5
num2 = 10
num1, num2 = num2, num1
print(f'num1 = {num1}, num2 = {num2}')

#6
age = int(input('Enter age: '))

if age >= 18 and not age < 17:
    print('adult')
else: 
    print('You are not adult')
    

#7
num = int(input('Enter number: '))
if num > 0:
    print('number potive')
elif num < 0:
    print('number nagative')
else: 
    print('number = 0')
    
#8
num = int(input('Enter number: '))
if num % 2 == 0:
    print('num is par')
else: 
    print('num isn`t par')
    
#9
num1 = 10
num2 = 123
if num1 > num2:
    print('num1 > num2')
elif num2 > num1:
    print('num1 < num2')
else:
    print('num1 = num2')
    
#10
grade = 43
if grade >= 80 and grade <= 100:
    print('Graed high')
elif grade >= 60 and grade <= 80:
    print('Grade sufficient')
elif grade >= 40 and grade <= 60:
    print('Grade average')
elif grade >= 20 and grade <= 40:
    print('Grade low')
elif grade >= 0 and grade <= 20:
    print('Grade very low')
else:
    print('Erorr')
    
#11
num = 25
if num >= 10 and num <= 50:
    print(f'10 < {num} < 50')
else:
    print('Erorr')

#12
login = 'admin'
password = 1234

if login == 'admin' and password == 1234:
    print('you are in sistem')
else:
    print('Erorr')
    

#13
for i in range(1, 20+1):
    print(i)
    
#14
for i in range(1, 30+1):
    if i % 2 == 0:
        print(i)
        
# 15
sum = 0
numRange = 34
for i in range(1, numRange+1):
    sum += i
print(sum)

#16
num = 4
for i in range(1, 10+1):
    print(f'{num} * {i} = {num * i}')
    
# 17
num = 5
f = 1
for i in range(1, num+1):
    f *= i
    
#18
num = input('Enter num: ')
print(f'Count num: {len(num)}')

# 19
arr = [1, 2, 3, 4, 5]
print(arr[0])
print(arr[4])
print(arr[2] + arr[4])

#20
arr = [1, 2, 3, 4, 5]
num = 3
for i in arr:
    if num in arr:
        print(True)
    else:
        print(False)

# 21
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in arr:
    if i > 5:
        print(i)

# 22
line = 'Hello'
print(len(line))
print(line[0])
print(line[-1])

#23
text = 'Hello '
print(text.upper())
print(text.lower())

# 24
text = 'аавцкуеекАІАУЙЦНЕАП'
golos = 'аеєиіїоуюяАЕЄИІЇОУЮЯ'
count = 0 
for i in text:
    if i in golos:
        count += 1
print(count)