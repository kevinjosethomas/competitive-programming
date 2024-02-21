n = int(input())
boards = [int(x) for x in input().split()]

frequency = {}
sum_frequency = {}

for board in boards:
    x = frequency.get(board)
    if not x:
        frequency[board] = 1
    else:
        frequency[board] = x + 1

keys = list(frequency.keys())

for i, x in enumerate(keys):
    start = i if frequency[x] > 1 else i + 1

    for j in range(start, len(keys)):
        y = keys[j]
        s = x + y
        freq = min(frequency[x], frequency[y])

        if i == j:
            freq = frequency[x] // 2

        z = sum_frequency.get(s)
        if not z:
            sum_frequency[s] = freq
        else:
            sum_frequency[s] = z + freq

highest = 0
count = 0
for x in sum_frequency:
    if sum_frequency[x] > highest:
        highest = sum_frequency[x]
        count = 1
    elif sum_frequency[x] == highest:
        count += 1

print(f"{highest} {count}")
