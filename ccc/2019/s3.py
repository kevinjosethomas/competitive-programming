import copy

total_missing = 0
grid = []
for _ in range(3):
    raw = input().split()
    row = []
    for x in raw:
        if x == "X":
            total_missing += 1
            row.append(None)
            continue
        row.append(int(x))
    grid.append(row)


def pprint(grid):
    for row in grid:
        print(" ".join([str(r) for r in row]))


def count_remaining(grid):
    count = 0
    for row in grid:
        count += row.count(None)

    return count


def find_replacement_index(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "X":
                return x, y


def find_missing_value_1x(index, neighbours):
    before, after = neighbours

    if before.count(None) or after.count(None):
        return None

    if index == 0:
        increment = after[1] - after[0]
        return after[0] - increment
    elif index == 1:
        increment = (after[0] - before[0]) // 2
        return after[0] - increment
    elif index == 2:
        increment = before[1] - before[0]
        return before[1] + increment


def find_missing_value(g, r, x, y):
    x_neighbours = [[], []]
    y_neighbours = [[], []]

    if x == 0:
        x_neighbours[1] = r[1:]
    if x == 1:
        x_neighbours[0].append(r[0])
        x_neighbours[1].append(r[2])
    if x == 2:
        x_neighbours[0] = r[:2]

    value = find_missing_value_1x(x, x_neighbours)
    if value is not None:
        return value

    if y == 0:
        y_neighbours[1].append(g[y + 1][x])
        y_neighbours[1].append(g[y + 2][x])
    if y == 1:
        y_neighbours[0].append(g[y - 1][x])
        y_neighbours[1].append(g[y + 1][x])
    if y == 2:
        y_neighbours[0].append(g[y - 2][x])
        y_neighbours[0].append(g[y - 1][x])

    value = find_missing_value_1x(y, y_neighbours)

    return value


def parse_obvious_values(gridcopy, remaining):
    while remaining:
        previously_remaining = remaining

        for y, r in enumerate(gridcopy):
            for x, c in enumerate(r):
                if c is not None:
                    continue

                value = find_missing_value(gridcopy, r, x, y)

                if value is None:
                    continue

                gridcopy[y][x] = value
                remaining -= 1

        if remaining == previously_remaining:
            break

    return gridcopy


queue = []
remaining = total_missing
new_grid = grid
while remaining:
    new_grid = copy.deepcopy(new_grid)
    node = 0

    # print(remaining)
    # print_grid(new_grid)
    # print(queue)

    if queue:
        node = queue.pop(0)
        coords = find_replacement_index(new_grid)

        if not coords:
            break

        new_grid[coords[1]][coords[0]] = node

    new_grid = parse_obvious_values(new_grid, remaining)
    now_remaining = count_remaining(new_grid)

    # print(now_remaining)
    # print_grid(new_grid)
    # print("\n")

    if now_remaining == 0:
        break
    else:
        queue.append(node + 1)


pprint(new_grid)
