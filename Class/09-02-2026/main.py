# for i in range(1, 10):
#     if i % 2 != 0:
#         print(i)
#
#
# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))
# if start > end:
#     start, end = end, start
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         print(i)

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
if start > end:
    start, end = end, start

for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)

for i in range(end, start-1):
    if i % 2 != 0:
        print(i)

for i in range(start, end, -1):
    if i % 2 != 0:
        print(i)