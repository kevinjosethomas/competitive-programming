t = int(input())
n = int(input())
d = sorted([int(x) for x in input().split()])
p = sorted([int(x) for x in input().split()])

total = 0

if t == 1:
    for i in range(n):
        total += max(d[i], p[i])
elif t == 2:
    for i in range(n):
        total += max(d[i], p[-i-1])

print(total)