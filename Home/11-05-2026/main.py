import os
import re
from collections import Counter

def task_1():
    lines = []
    for i in range(3):
        line = input(f"Введіть рядок {i+1}: ")
        lines.append(line + '\n')
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)

def task_2():
    filename = 'data.txt'
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for index in range(1, len(lines), 2):
                print(f"Рядок {index + 1}: {lines[index].strip()}")

def task_3():
        with open('data.txt', 'r', encoding='utf-8') as f_in:
            python_lines = [line for line in f_in if "Python" in line]
        with open('filtered.txt', 'w', encoding='utf-8') as f_out:
            f_out.writelines(python_lines)

def task_4():
        with open(name, 'r', encoding='utf-8') as file:
            content = file.read()
        cleaned = "".join([c for c in content if not c.isdigit()])
        with open('cleaned.txt', 'w', encoding='utf-8') as file:
            file.write(cleaned)

def task_5():
    if not os.path.exists('log.txt'):
        with open('log.txt', 'w', encoding='utf-8') as f:
            f.write("error info error debug error warning info debug debug info")
    
        with open('log.txt', 'r', encoding='utf-8') as file:
            words = re.findall(r'\w+', file.read().lower())
        stats = Counter(words).most_common(10)
        with open('word_stats.txt', 'w', encoding='utf-8') as file:
            for word, count in stats:
                file.write(f"{word}: {count}\n")

def task_6():
        with open('data.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open('reversed.txt', 'w', encoding='utf-8') as file:
            for line in reversed(lines):
                if not line.endswith('\n'):
                    line += '\n'
                file.write(line)

def main():
    tasks = {
        "1": task_1, "2": task_2, "3": task_3,
        "4": task_4, "5": task_5, "6": task_6
    }
    
    while True:
        print("1-6: Виконати завдання")
        print("0: Вихід")
        choice = input("Оберіть номер: ")
        
        if choice == "0":
            break
        elif choice in tasks:
            tasks[choice]()

if __name__ == "__main__":
    main()