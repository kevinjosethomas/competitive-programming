a = input()
b = input()

for char in b:
    if char != "*":
        a = a.replace(char, "", 1)

if b.count("*") == len(a):
    print("A")
else:
    print("N")
