text = input("Введіть текст: ")
symbols = input("Введіть символи: ")
words = text.split()
result = ""
for word in words:
    delete = False
    for s in symbols:
        if s in word:
            delete = True
    if not delete:
        result += word + " "
print("Результат:", result)



text = input("Введіть текст: ")
words = text.split()
result = ""
for i in range(len(words)-1, -1, -1):
    result += words[i] + " "
print("Результат:", result)



text = input("Введіть рядок: ")
result = ""
for i in text:
    result = i + result
print("Результат:", result)



text = input("Введіть рядок: ")
search = input("Введіть слово: ")
words = text.split()
count = 0
for word in words:
    if word == search:
        count += 1
print("Кількість:", count)