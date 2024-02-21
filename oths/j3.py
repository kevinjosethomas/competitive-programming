n, d = [int(x) for x in input().split()]
heights = [int(x) for x in input().split()]

graphs = []
current = []
for i, bomb in enumerate(heights):
    if i == 0:
        current.append(bomb)
        continue

    if abs(bomb - heights[i - 1]) <= d:
        current.append(bomb)
    else:
        graphs.append(current)
        current = [bomb]
graphs.append(current)

print(len(graphs))
print(len(sorted(graphs, key=lambda x: len(x))[-1]))
