from collections import deque

possible = False
rows = int(input())
cols = int(input())
grid = []
cache = {}
visited = {}

for r in range(rows):
    raw = [int(x) for x in input().split()]

    for c in range(cols):
        col = raw[c]
        visited[(r + 1) * (c + 1)] = False
        if col in cache:
            cache[col].append((r + 1, c + 1))
        else:
            cache[col] = [(r + 1, c + 1)]

queue = deque([(rows, cols)])

while queue:
    node = queue.popleft()
    product = (node[0]) * (node[1])
    paths = cache.get(product)

    if not paths:
        continue

    for path in paths:
        if path == (1, 1):
            possible = True
            queue = []
            break

        if visited.get(path[0] * path[1]):
            continue

        queue.appendleft(path)
        visited[path[0] * path[1]] = True

print("yes" if possible else "no")
