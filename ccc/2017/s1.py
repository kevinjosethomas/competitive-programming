n = int(input())
s1 = [int(x) for x in input().split()]
s2 = [int(x) for x in input().split()]

x = 0
y = 0
k = 0

for i in range(len(s1)):
    x += s1[i]
    y += s2[i]

    if x - y == 0:
        k = i+1

print(k)