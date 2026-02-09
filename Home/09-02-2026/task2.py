start = int(input("Початок діапазону: "))
end = int(input("Кінець діапазону: "))

if start > end:
    start, end = end, start

even_sum = odd_sum = mult9_sum = 0
even_count = odd_count = mult9_count = 0

for i in range(start, end + 1):
    if i % 2 == 0:
        even_sum += i
        even_count += 1
    else:
        odd_sum += i
        odd_count += 1

    if i % 9 == 0:
        mult9_sum += i
        mult9_count += 1

print(f"Парні: сума {even_sum}, середнє {even_sum / even_count if even_count > 0 else 0}")
print(f"Непарні: сума {odd_sum}, середнє {odd_sum / odd_count if odd_count > 0 else 0}")
print(f"Кратні 9: сума {mult9_sum}, середнє {mult9_sum / mult9_count if mult9_count > 0 else 0}")


line_len = int(input("Довжина лінії: "))
char = input("Символ: ")
for _ in range(line_len):
    print(char)


while True:
    num = int(input("Введіть число (7 для виходу): "))
    if num == 7:
        print("Good bye!")
        break
    elif num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")


nums = []
while True:
    num = int(input("Введіть число (7 для виходу): "))
    if num == 7:
        if nums:
            print(f"Sum: {sum(nums)}, Max: {max(nums)}, Min: {min(nums)}")
        print("Good bye!")
        break
    nums.append(num)


n_prime = int(input("Введіть ціле число N: "))
if n_prime <= 1:
    print("Число має бути більшим за 1")
else:
    is_prime = True
    for i in range(2, int(n_prime ** 0.5) + 1):
        if n_prime % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"Число {n_prime} є простим")
    else:
        print(f"Число {n_prime} не є простим")


n_fib = int(input("Введіть ціле число N: "))
a, b = 0, 1
is_fib = False
if n_fib >= 0:
    while a <= n_fib:
        if a == n_fib:
            is_fib = True
            break
        a, b = b, a + b

if is_fib:
    print(f"Число {n_fib} належить послідовності Фібоначчі")
else:
    print(f"Число {n_fib} не належить послідовності Фібоначчі")