t1 = (1, 2, 3, 4, 5)
t2 = (3, 4, 5, 6, 7)
t3 = (5, 4, 8, 9, 1)

result = []
for item in t1:
    if item in t2 and item in t3:
        if item not in result: 
            result.append(item)
print("Спільні елементи:", tuple(result))




t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
t3 = (1, 7, 8, 9)

unique_t1 = [x for x in t1 if x not in t2 and x not in t3]
unique_t2 = [x for x in t2 if x not in t1 and x not in t3]
unique_t3 = [x for x in t3 if x not in t1 and x not in t2]

print(f"Тільки в 1-му: {tuple(unique_t1)}")
print(f"Тільки в 2-му: {tuple(unique_t2)}")
print(f"Тільки в 3-му: {tuple(unique_t3)}")