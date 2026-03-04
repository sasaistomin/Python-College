text = input("Введіть текст: ")
count = 0
for i in text:
    if i == "." or i == "!" or i == "?":
        count += 1
print("Кількість речень:", count)



text = input("Введіть рядок: ")
text = text.lower().replace(" ", "")
if text == text[::-1]:
    print("Це паліндром")
else:
    print("Це не паліндром")



text = input("Введіть текст: ")
reserved = ["if", "else", "for", "while", "def", "class"]
words = text.split()
result = ""
for word in words:
    if word in reserved:
        word = word.upper()
    result += word + " "
print("Результат:")
print(result)



text = input("Введіть рядок: ")
a = input("Перший символ: ")
b = input("Другий символ: ")
start = text.find(a)
end = text.find(b)
if start != -1 and end != -1 and start < end:
    result = text[:start] + text[end+1:]
else:
    result = text
print("Результат:", result)