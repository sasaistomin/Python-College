start = int(input("Enter start number: "))
finish = int(input("Enter finish number: "))
for i in range(start, finish+1):
    if i % 7 == 0:
        print(i)


start = int(input("Enter start number: "))
finish = int(input("Enter finish number: "))
for i in range(start, finish+1):
    print(i)
for i in range(finish, start):
    print(i)
for i in range(start, finish+1):
    if i % 7 == 0:
        print(i)
for i in range(start, finish+1):
    count = 0
    if i % 5 == 0:
        count += 1
        print(count)


start = int(input("Enter start number: "))
finish = int(input("Enter finish number: "))
for i in range(start, finish+1):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 != 0 and i % 5 != 0:
        print(i)


start = int(input("Enter start number: "))
finish = int(input("Enter finish number: "))
goToFor = int(input("Enter go to number: "))
print("1) for >")
print("2) for <")
do = int(input("Enter your choice: "))
if do == 1:
    for i in range(start, finish+1, goToFor):
        print(i)
elif do == 2:
    for i in range(finish, start, goToFor):
        print(i)


start = int(input("Enter start number: "))
finish = int(input("Enter finish number: "))
if start > finish:
    start, finish = finish, start
count = 1
found = False
for i in range(start, finish+1):
    if i % 4 == 0 and i % 6 != 0:
        count *= i
        found = True
if found:
    print(count)
else:
    print("Not found")


a = int(input("Enter number: "))
n = int(input("Enter degree: "))
goTo = 1
for i in range(1, n+1):
    goTo *= a
print(f"Result: {goTo}")