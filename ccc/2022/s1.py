n = int(input())
count = 0

for i in range(0, n + 1, 5):
    if (n - i) % 4 == 0:
        count += 1

print(count)
