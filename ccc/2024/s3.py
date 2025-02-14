length = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

moves = []

for i in range(length):
    current = a[i]
    target = b[i]

    if current == target:
        continue

    if i != 0:
        if a[i - 1] == target:
            try:
                a[i] = a[i - 1]
                if moves[-1][0] == "R" and moves[-1][2] == i - 1:
                    moves.append(["R", moves[-1][1], i])
                    moves.pop(-2)
                else:
                    moves.append(["R", i - 1, i])

                if a[i + 1] != b[i + 1] and current == a[i + 1]:
                    a[i + 1] = current
                    moves.insert(-2, ["R", i, i + 1])
            except IndexError:
                moves.append(["R", i - 1, i])
            continue

    if i != length - 1:
        try:
            next_occurence = a[i:length].index(target)
        except ValueError:
            print("NO")
            exit()

        for j in range(i, i + next_occurence):
            a[j] = a[i + next_occurence]

        moves.append(["L", i, i + next_occurence])
        continue
    else:
        print("NO")
        exit()

print("YES")
print(len(moves))
for move in moves:
    for char in move:
        print(char, end=" ")
    print()
