import sys

n = int(input())
l = [int(x) for x in input().split()]
separators = []

for i, x in enumerate(l):
    if i + 1 == x:
        separators.append(x)

if len(separators) == 0:
    print(n)
    sys.exit()

filtered_separators = []

for i, sep in enumerate(separators):

    sep_index = sep - 1

    if i == 0:
        for el in range(0, sep_index):
            if l[el] > sep:
                break
        filtered_separators.append(sep)
        break

    prev = separators[i - 1]
    prev_index = prev - 1

    for el in range(prev_index + 1, sep_index):
        if l[el] > sep or l[el] < prev:
            break

    filtered_separators.append(sep)

print(separators)
print(filtered_separators)
cost = 0
for i, sep in enumerate(filtered_separators):
    if i == 0:
        cost += sep - 1

    if i == len(filtered_separators) - 1:
        cost += n - sep

    if 0 < i < len(filtered_separators) - 1:
        cost += sep - filtered_separators[i - 1] - 1

print(cost)
