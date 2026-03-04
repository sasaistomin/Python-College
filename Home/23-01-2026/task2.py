a = 7
b = 2.5
c = a + b
print(c)
print(type(c)) # тип изменился потому-что b это float и он не может убрать число после точки и он будет float


x = "10"
y = "20"
print(int(x) + int(y))


price = float(input("Enter price: "))
whole = int(price)
rounded = round(price)
print(whole) # будет челое число, integer это чисто без точки
print(rounded) # если число 1.2 то будет 1 если чесло больше или есть 1.5 то будет 2


a = 0
b = 1
c = ""
d = "0"
print(bool(a)) # False
print(bool(b)) # True
print(bool(c)) # False
print(bool(d)) # True


n = int(input("Enter number: "))
if n % 2 == 0 and n >= 10:
    print(True)
else:
    print(False)
if n <= 0 and n >= 100:
    print(True)
else:
    print(False)
if not n % 3 == 0:
    print(True)
else:
    print(False)


login = input("Enter login: ")
password = input("Enter password: ")
if login == "adnim" and password == "qwerty":
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")


t = float(input("Enter temperature: "))

if t <= 0:
    print("FREEZING")
elif 0 < t < 10:
    print("COLD")
elif 10 <= t < 25:
    print("OK")
elif t >= 25:
    print("HOT")