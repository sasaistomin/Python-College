# f = open('name.txt', 'wt')
# f.write('Hello Wordl')
# f.close()

f = open('text.txt', 'rt')
count = 0 
li = f.readline()
f.close()

world = 'Orange'

for li in li:
    count = count + 1
    if world in li:
        break

print(f'word: {world} in line: {count}')
