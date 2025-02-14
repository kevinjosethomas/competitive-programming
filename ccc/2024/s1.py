n = int(input())
hats = [int(input()) for _ in range(n)]

count = 0
for i in range(n // 2):
    if hats[i] == hats[i + (n // 2)]:
        count += 1

print(count * 2)
