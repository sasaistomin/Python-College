t1 = (1, 2, 3, 4, 5)
t2 = (10, 2, 8, 4, 0)
t3 = (1, 2, 7, 4, 9)

result = []

for a, b, c in zip(t1, t2, t3):
    if a == b == c:
        result.append(a)

print("Однакові елементи на однакових позиціях:", tuple(result))