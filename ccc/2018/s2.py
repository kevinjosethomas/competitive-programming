n = int(input())
rawgrid = []
for _ in range(n):
    rawgrid.append([int(x) for x in input().split()])


def output(grid):
    for x in grid:
        print(" ".join(list(str(y) for y in x)))


def rotate(grid):
    new_grid = [[0 for __ in range(n)] for _ in range(n)]

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            new_grid[x][n - 1 - y] = val

    return new_grid


def check_validity(grid):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if x == 0 or y == 0:
                continue
            if val < row[x - 1]:
                return False
            if val < grid[y - 1][x]:
                return False

    return True


for _ in range(4):
    rawgrid = rotate(rawgrid)
    if check_validity(rawgrid):
        output(rawgrid)
        break
