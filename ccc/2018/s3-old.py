import time

CONVEYORS = ["L", "R", "U", "D"]

rows, cols = [int(x) for x in input().split()]
factory = []
starting_position = (0, 0)
cells = {}

for r in range(rows):
    row = list(input())
    factory.append(row)

    if "S" in row:
        starting_position = (row.index("S"), r)

t = time.time()


def traverse(start, target, previous):
    steps = []
    prev = start
    while prev is not None:
        steps.append(prev)
        prev = previous.get(prev)

    if steps[-1] == target:
        return len(steps) - 1


def pathfinder(initial):
    queue = [initial]
    traversed = [initial]
    previous = {}

    while queue:
        x, y = queue.pop(0)

        if factory[y][x] == ".":
            cells[(x, y)] = traverse((x, y), initial, previous)

        neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for neighbour in neighbours:
            node = factory[neighbour[1]][neighbour[0]]

            if node in traversed:
                continue

            if node in CONVEYORS:
                traversed.append(neighbour)
                if node == "L":
                    neighbours.append((neighbour[0] - 1, neighbour[1]))
                elif node == "R":
                    neighbours.append((neighbour[0] + 1, neighbour[1]))
                elif node == "U":
                    neighbours.append((neighbour[0], neighbour[1] - 1))
                elif node == "D":
                    neighbours.append((neighbour[0], neighbour[1] + 1))

        for neighbour in neighbours:
            node = factory[neighbour[1]][neighbour[0]]

            if node == "W" or node == "S":
                continue

            if neighbour not in traversed:
                queue.append(neighbour)
                traversed.append(neighbour)
                previous[neighbour] = (x, y)


for y, row in enumerate(factory):
    for x, cell in enumerate(row):
        if cell == "C":
            factory[y][x] = "W"
            surrounding = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for i, s in enumerate(surrounding):
                node = factory[s[1]][s[0]]
                if node == ".":
                    factory[s[1]][s[0]] = "X"
                elif node == "S":
                    factory[s[1]][s[0]] = "Z"
                elif node in CONVEYORS:
                    if i == 0:  # left
                        while True:
                            next_shift = (s[0] - 1, s[1])
                            try:
                                node = factory[next_shift[1]][next_shift[0]]
                            except IndexError:
                                break
                            if node in CONVEYORS:
                                continue
                            elif node == ".":
                                factory[next_shift[1]][next_shift[0]] = "X"
                            break
                    elif i == 1:  # right
                        while True:
                            next_shift = (s[0] + 1, s[1])
                            try:
                                node = factory[next_shift[1]][next_shift[0]]
                            except IndexError:
                                break
                            if node in CONVEYORS:
                                continue
                            elif node == ".":
                                factory[next_shift[1]][next_shift[0]] = "X"
                            break
                    elif i == 2:  # up
                        while True:
                            next_shift = (s[0], s[1] - 1)
                            try:
                                node = factory[next_shift[1]][next_shift[0]]
                            except IndexError:
                                break
                            if node in CONVEYORS:
                                continue
                            elif node == ".":
                                factory[next_shift[1]][next_shift[0]] = "X"
                            break
                    elif i == 3:  # down
                        while True:
                            next_shift = (s[0], s[1] + 1)
                            try:
                                node = factory[next_shift[1]][next_shift[0]]
                            except IndexError:
                                break
                            if node in CONVEYORS:
                                continue
                            elif node == ".":
                                factory[next_shift[1]][next_shift[0]] = "X"
                            break


pathfinder(starting_position)

impossible = factory[starting_position[1]][starting_position[0]] == "Z"

t = time.time() - t
output = []

for y, row in enumerate(factory):
    for x, col in enumerate(row):
        if col == ".":
            if impossible:
                output.append(-1)
            else:
                output.append(cells.get((x, y), -1))
        elif col == "X":
            if impossible:
                output.append(-1)
            else:
                output.append(-1)

with open("output.txt", "w") as f:
    f.write("\n".join(str(x) for x in output))

print(t)
