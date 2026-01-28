a = "12"
b = "3.5"
c = 2

x = int(a)
y = float(b)
result = x + y + c
print(result, type(result))

name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}!")
print(f"You age {age}")
print(f"{name * 3}")
print(len(name))


a = int(input("Enter number: "))
b = int(input("Enter number: "))

is_equal = a == b
is_a_greater = a > b
is_b_even = b % 2 == 0
in_range = 10 <= a <= 20 and 10 <= b <= 20


x = int(input("Enter number: "))
if x >= 1 and x <= 100:
    print(True)

if x >= 10 and x <= 20:
    print(False)

if x % 3 == 0 and x % 5 == 0:
    print(True)

if x % 3 == 0 and not x % 4 == 0:
    print(True)


x = 10
y = 3

x += y
print(x)

x *= y
print(x)

x -= y
print(x)

x //= y
print(x)

x %= 2
print(x)


score = int(input("Enter score: "))
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 0 and score <= 59:
    print("F")
else:
    print("Invalid")


a = 2
b = 3
c = 4

print(a + b * c) # умножение будет первым потом что он есть пририоретотом
print((a + b) * c) # тут есть скобки и они теперь есть приоритетом
print(a ** b ** 2) # сразу в степень перейдет b и потом a перейдет в степень b
print(not a == 2 or b > 1 and c < 10) # сразу виполняеться not a == 2, далее b > 1 and c < 10 и аж в конце or