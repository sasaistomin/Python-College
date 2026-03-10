arr = [1, 3, 2, 4, 5]
count = 0

for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        count += 1

print(count)


arr = [1, 2, 2, 3, 4, 4, 5]
newArr = []

for item in arr:
    if arr.count(item) == 1:
        newArr.append(item)
    
print(newArr)


arr = [1, 2, 1, 2, 3, 4, 1]

#

current_seq = [arr[0]]
best_seq = [arr[0]]    


for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        current_seq.append(arr[i])
    else:
        if len(current_seq) > len(best_seq):
            best_seq = current_seq.copy()
        current_seq = [arr[i]]

if len(current_seq) > len(best_seq):
    best_seq = current_seq

print(len(best_seq))
print(best_seq)