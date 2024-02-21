m = int(input())
n = int(input())
k = int(input())
frequency = {}

total = 0

for direction in range(k):
    direction = input()
    if direction in frequency:
        frequency[direction] += 1
    else:
        frequency[direction] = 1

for row in range(1, m + 1):
    for col in range(1, n + 1):
        flips = frequency.get(f"R {row}", 0) + frequency.get(f"C {col}", 0)

        total += 1 if flips % 2 != 0 else 0

print(total)
