n = int(input())
villages = sorted([int(input()) for _ in range(n)])

smallest = 0
for i, village in enumerate(villages):
    if i == 0 or i == len(villages) - 1:
        continue

    size = (villages[i + 1] - village) / 2 + (village - villages[i - 1]) / 2

    if not smallest or size < smallest:
        smallest = size

print(smallest)
