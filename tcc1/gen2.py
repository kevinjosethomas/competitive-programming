import random

n = 1000000
k = 1000000

s = ""
t = " "
for _ in range(n):
    s += str(random.randint(1, k)) + " "

for _ in range(k):
    t += "1 "

with open("input.txt", "w") as f:
    f.write(f"{n} {k}\n")
    f.write(s + "\n")
    f.write(t + "\n")
