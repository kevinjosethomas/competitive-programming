size = int(input())

while True:
    x = int(input())
    if x >= size:
        break

    size += x
print(size)
