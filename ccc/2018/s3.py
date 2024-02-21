import sys
import heapq

CONVEYORS = ["U", "D", "L", "R"]
input = sys.stdin.readline


rows, cols = [int(x) for x in input().split()]
factory = tuple(tuple(input().strip()) for _ in range(rows))

starting_position = None
adj = [[] for _ in range(rows * cols)]
camera_invalid = set([])
distances = {}


def parse_index(row, col):
    return (row * cols) + col


def parse_camera(row, col):
    camera_invalid.add(parse_index(row, col))

    top_row = row
    while True:
        top_row -= 1
        top_node = factory[top_row][col]

        if top_node == "W":
            break

        if top_node == "S" or top_node == ".":
            camera_invalid.add(parse_index(top_row, col))

    bottom_row = row
    while True:
        bottom_row += 1
        bottom_node = factory[bottom_row][col]

        if bottom_node == "W":
            break

        if bottom_node == "S" or bottom_node == ".":
            camera_invalid.add(parse_index(bottom_row, col))

    left_col = col
    while True:
        left_col -= 1
        left_node = factory[row][left_col]

        if left_node == "W":
            break

        if left_node == "S" or left_node == ".":
            camera_invalid.add(parse_index(row, left_col))

    right_col = col
    while True:
        right_col += 1
        right_node = factory[row][right_col]

        if right_node == "W":
            break

        if right_node == "S" or right_node == ".":
            camera_invalid.add(parse_index(row, right_col))


for row, x in enumerate(factory):

    if row == 0 or row == rows - 1:
        continue

    for col, cell in enumerate(x):

        if col == 0 or col == cols - 1:
            continue

        node = factory[row][col]
        index = parse_index(row, col)

        if node == "W":
            continue
        elif node == "C":
            parse_camera(row, col)
            continue
        elif node == "S":
            starting_position = (row, col)
        elif node == ".":
            distances[index] = -1

        top = (row - 1, col)
        bottom = (row + 1, col)
        left = (row, col - 1)
        right = (row, col + 1)

        if node == "U":
            surrounding = [top]
        elif node == "D":
            surrounding = [bottom]
        elif node == "L":
            surrounding = [left]
        elif node == "R":
            surrounding = [right]
        else:
            surrounding = [top, bottom, left, right]

        for cord in surrounding:
            child = factory[cord[0]][cord[1]]

            if child == "W":
                continue

            child_index = parse_index(cord[0], cord[1])
            adj[index].append(cord)

visited = set([])
queue = [(0, starting_position)]
heapq.heapify(queue)

if parse_index(starting_position[0], starting_position[1]) in camera_invalid:
    queue = None

while queue:
    distance, cords = heapq.heappop(queue)
    node = factory[cords[0]][cords[1]]
    index = parse_index(cords[0], cords[1])

    for child_cord in adj[index]:

        child = factory[child_cord[0]][child_cord[1]]
        if child == "W" or child == "S" or child == "C":
            continue

        child_index = parse_index(child_cord[0], child_cord[1])
        if child_index in visited or child_index in camera_invalid:
            continue

        if child == ".":
            distances[child_index] = distance + 1
            child_distance = distance + 1
        else:
            child_distance = distance

        visited.add(child_index)

        heapq.heappush(queue, (child_distance, child_cord))

for x in distances:
    print(distances[x])
